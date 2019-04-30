#!/usr/bin/python
import xml.dom.minidom
# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("data1.xml")
root = DOMTree.documentElement
if root.hasAttribute("org"):
   print(root.getAttribute("org"))
if root.hasAttribute("session"):
   print(root.getAttribute("session"))
userList=root.getElementsByTagName("user")
for user in userList:
    id=user.getAttribute("id")
    fname=user.getElementsByTagName("fname")[0]
    lname=user.getElementsByTagName("lname")[0]
    print(id ,
            fname.childNodes[0].data,
            lname.childNodes[0].data)