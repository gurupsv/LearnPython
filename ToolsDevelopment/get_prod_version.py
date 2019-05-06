import json
import requests
import sys

proper_args=sys.argv[1:]
if (len(proper_args) < 1):
        print ("Syntax is \"python get_production_version.py 18.1.6 BDCSCE\"")
        exit ()

#service_version=sys.argv[1]
service_name=sys.argv[1]
service_reg_list=""
def getServices(string):
        li = list(string.split(","))
        return li

for service in getServices(service_name):
        response = requests.get('http://idoru.oraclecorp.com:8080/v1/services/'+service+'/versions?version=*&sort-order=desc&sort-field=release&size=20&target-maturity=production&page=1&release=*')
        data = response.json()
        print(data)
        #print (service+":"+data['versions'][0]['version'])
        #print (data['versions'][0]['maven_base']+";dummyuser;dummypwd;"+service+":"+data['versions'][0]['version']+"&&")
        service_reg_list=service_reg_list+data['versions'][0]['maven_base']+";dummyuser;dummypwd;"+service+":"+data['versions'][0]['version']+"&&"

service_reg_list=service_reg_list[:-2]
print (service_reg_list)