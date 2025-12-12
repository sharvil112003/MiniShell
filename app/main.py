import sys
from app.functions import echo
import shutil
import os
import subprocess
# import readline
import shlex

def main():
    # TODO: Uncomment the code below to pass the first stage
    cmds = ['exit', 'type', 'echo', 'pwd','cd']
    while True:
        # print(os.environ["PATH"])
        sys.stdout.write("$ ")
        home_path = os.environ.get('HOME')
        command = input() 
        cmd = command.split(" ")
        token = shlex.split(command)
        if cmd[0] == "exit":
            break

        if cmd[0] == "echo":
            print(" ".join(token[1:]))
            continue
        
        if cmd[0] == "type":
            for prog in cmd[1:]:
                if prog in cmds:
                    print(f"{prog} is a shell builtin")
                elif shutil.which(prog) is not None:
                    path  = shutil.which(prog)
                    print(f"{prog} is {path}")
                else:
                    print(f"{prog}: not found")

            continue

        if cmd[0] == "pwd":
           print(os.getcwd())

        if cmd[0] not in cmds:
            exe = token[0]
            args = token[1:]

            if shutil.which(exe) is not None or os.path.exists(exe):
                subprocess.run([exe, *args])

            else:
                print(f"{cmd[0]}: not found")

        if cmd[0] == "cd":
            if os.path.exists(cmd[1]):
                os.chdir(cmd[1])
            elif cmd[1] == '~' and home_path is not None:
                os.chdir(home_path)
            else:
                print(f"cd: {cmd[1]}: No such file or directory")    
        pass
    return 0


if __name__ == "__main__":
    main()
