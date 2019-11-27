import jwt
import json

def myfunc():
    return "MyString123"

def getJWT(payload, secret):
    return jwt.encode({"name":"UltraPayer","sub":"123456"}, secret, algorithm='HS256')