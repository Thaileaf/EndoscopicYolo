import subprocess

command = "python detect.py --weights ./bestModels/best.pt --source 1 --nosave"

subprocess.run(command, shell=True)