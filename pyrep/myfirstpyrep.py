import requests
import sys

sys.path.append("/Users/guruprasadsv/PycharmProjects/LearnPython/pyrep")
from pytestng import report


@report
def mytest():
    print("Running mytest")
    assert 1 == 2

@report
def mytest2():
    print("Running mytest2")
    assert 1==1

url = "https://reqres.in/api/users?page=2"
@report
def mytest3():
    print("Running mytest3")
    response=requests.get(url)
    t=requests.Response()
    t.status_code=300
    print(response)
    print(t)
    assert t.status_code == response.status_code

mytest()
mytest2()
#mytest3()
