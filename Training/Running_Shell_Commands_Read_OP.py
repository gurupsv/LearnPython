
import subprocess

process = subprocess.Popen('dir',
                           shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
for line in process.stdout:
    print(line.decode(), end="")