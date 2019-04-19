
import subprocess
process1 = subprocess.Popen('dir',
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE )
process2=subprocess.Popen('findstr ".py"',
    shell=True,
    stdin=process1.stdout,
    stdout=subprocess.PIPE,
   stderr=subprocess.PIPE
    )
for line in process2.stdout:
    print(line.decode(),end="")