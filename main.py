import flask
import requests
import yaml
import simplejson
from flask import request
from flask import Flask, Response
from flask import jsonify
from flask import make_response
from cryptography.fernet import Fernet as fn
from cryptography.fernet import Fernet as ft
###############Below section is for encryption and decrytion method defining###############

def generatekey() :
     test_key = fn.generate_key()
     #print(test_key)
     file = open('test_key.key', 'wb')
     file.write(test_key)
     file.close()

def encryptmessage(teststr):
    message = teststr.encode()
    file = open('test_key.key', 'rb')
    key = file.read()
    f = ft(key)
    encrypted_message = f.encrypt(message)
    return encrypted_message

def decryptmessage(encrypted_message):
    message = encrypted_message.encode()
    file = open('test_key.key', 'rb')
    key = file.read()
    f = ft(key)
    decrypted_message = f.decrypt(message)
    file.close()
    return decrypted_message

generatekey()


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/health', methods=['GET'])
def health():
    return "Healthy"

@app.route('/api/encrypt', methods=['GET', 'POST'])
def encryptdata():
    print (request.is_json)
    app.config['JSON_SORT_KEYS'] = False
    content = request.get_json()
    #generatekey()
    encryptres = encryptmessage(content['Input'])
    print(encryptres)
    invalue = content['Input']
    data = {'Input': invalue, 'Output': encryptres, 'Status': 'success', 'Message': ''}
    return data

@app.route('/api/decrypt', methods=['GET', 'POST'])
def decryptdata():
    print (request.is_json)
    app.config['JSON_SORT_KEYS'] = False
    content = request.get_json()
    #generatekey()
    decryptres = decryptmessage(content['Input'])
    print(decryptres)
    invalue = content['Input']
    data = {'Input': invalue, 'Output': decryptres, 'Status': 'success', 'Message': ''}
    #res = json_response("Input"=invalue, Output=encryptres, Status=success, Message="")
    return data

  
app.run(host='0.0.0.0')


