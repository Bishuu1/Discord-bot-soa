import socket
import os
import json
import urllib
import urllib.parse
import urllib.request

def genPrefix(largo):
    num=str(largo+5)
    while(len(num)<5):
        num= "0"+num
    return num+"imagr"

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5000        # Port to listen on (non-privileged ports are > 1023)

url="http://api.giphy.com/v1/gifs/random"
tag=""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(b'00010sinitimagr')
    s.recv(4096)
    print('Servicio iniciado')
    while True:
        data = s.recv(4096)
        tag = data[10:].decode()
        print(tag)
        params= urllib.parse.urlencode({
            "api_key": "sGAOAt7SKuGziFtXE2UurgXIGEKQShw1",
            "tag": tag
        })
        print(params)
        with urllib.request.urlopen(url+"?"+params) as response:
            data = json.loads(response.read())
        if (data['data']!=[]):
            link=data['data']['embed_url']
        else:
            link="No hubo resultados asociados a la busqueda"
        prefix=genPrefix(len(link))
        print(prefix+link)
        s.send((prefix+link).encode("utf-8"))