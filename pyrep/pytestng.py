import requests
import sys
import contextlib
from datetime import datetime
import os

print (os.getcwd())
print(os.path.dirname(os.path.realpath(__file__)))

def report(a):
    def genreport(*b,**c):
        try:
            with open(a.__name__, 'w') as f:
                start=datetime.now()
                f.write(f"Start time : {start}\n")
                with contextlib.redirect_stdout(f):
                    a(*b,**c)
                    f.write(f"End time : {start}\n")

        except AssertionError:
            now=datetime.now()
            print()
            print(f"[{now}] [{a.__name__}] : Assert Failure : {sys.exc_info()[0]}\n")
        except :
            now = datetime.now()
            print (f"[{now}] [{a.__name__}] : General Failure {sys.exc_info()[1]}")
        else:
            now = datetime.now()
            print(f"[{now}] [{a.__name__}] : Passed")
    return genreport
