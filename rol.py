import socket
import os
import json
import urllib
import urllib.parse
import urllib.request
import random
import discord
from discord import client
from discord.ext import commands
from discord.utils import get

def genPrefix(largo):
    num=str(largo+5)
    while(len(num)<5):
        num= "0"+num
    return num+"roles"

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5000        # Port to listen on (non-privileged ports are > 1023)

#url="http://api.giphy.com/v1/gifs/random"
tag=""
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(b'00010sinitrol')
    s.recv(4096)
    print('Servicio Rol iniciado')
    while True:
        data = s.recv(4096)
        tag = data[7:].decode() #obtenemos el rol que quiere usar + opcion
        print (tag)
        print ("Rol:" ,tag)
        if "admin" in tag.lower():
            mensaje="No se puede otorgar este rol"
            prefix = genPrefix(len(mensaje))
            s.send((prefix+mensaje).encode("utf-8"))

