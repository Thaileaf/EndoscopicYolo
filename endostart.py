import subprocess

command = "python detect.py --weights ./bestModels/best.pt --source 0"

subprocess.run(command, shell=True)