import subprocess

process = subprocess.Popen('dir',
                           shell=True,
                           stdout=open("output.txt", "w"),
                           stderr=open("error.txt", "w")
                           )

