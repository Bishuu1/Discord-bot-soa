import discord
from discord import message
from discord import guild
from discord import client
from discord.ext import commands
from discord.player import FFmpegAudio
from discord.utils import get
import socket
from yt_dlp import YoutubeDL
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5000        # Port to listen on (non-privileged ports are > 1023)
sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
sock.connect((HOST,PORT))


bot = commands.Bot(command_prefix='?') #Prefijo


def genPrefix(largo, servicio):
    num=str(largo+5)
    while(len(num)<5):
        num= "0"+num
    return num+servicio

print("Cliente corriendo")

@bot.command(pass_context = True)
async def imagr(ctx):

        texto = str(ctx.message.content)[7:]
        print(texto+" imagr")
        texto_enviar = genPrefix(len(texto), "imagr") + texto
        texto_enviar = texto_enviar.encode("utf-8")
        sock.send(texto_enviar)
        data = sock.recv(4096)
        Respuesta = data.decode()[12:]
        print("Respondiendo solicitud imagen: "+ texto)
        await ctx.send(Respuesta)

@bot.command(pass_context = True)
async def helpa(ctx):
        await ctx.send("Comandos disponibles: ?play, ?imagr, ?games, ?rol")


@bot.command(pass_context = True, name = "play")
async def ytser(ctx):

        cancionactiva = os.path.isfile("cancion.mp3")
        try:
            if cancionactiva:
                os.remove("cancion.mp3")
        except PermissionError:
            await ctx.send("Espera a que la canción termine")
            return
        canal = get(ctx.guild.voice_channels, name='Pastos')
        voz = get(bot.voice_clients, guild = ctx.guild)
        
        if voz is None or not voz.is_connected():
            await canal.connect()
            voz = get(bot.voice_clients, guild = ctx.guild)
        ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors':[{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                }],
        }

        texto = str(ctx.message.content)[6:]
        print(texto+" ytser")
        texto_enviar = genPrefix(len(texto), "ytser") + texto
        texto_enviar = texto_enviar.encode("utf-8")
        sock.send(texto_enviar)
        data = sock.recv(4096)
        Respuesta = data.decode()[12:]
        print("Respondiendo solicitud musica : "+ texto)
       
        with YoutubeDL(ydl_opts) as ydl:
                ydl.download (["https://www.youtube.com/watch?v=" + Respuesta])
        for file in os.listdir("./"):
                if file.endswith(".mp3"):
                        os.rename(file, "cancion.mp3")
        voz.play(discord.FFmpegPCMAudio("cancion.mp3"))
        
        


@bot.command(pass_context = True, name = "games")
async def games(ctx):

        texto = str(ctx.message.content)[7:]
        print(texto+" games")
        texto_enviar = genPrefix(len(texto), "games") + texto
        texto_enviar = texto_enviar.encode("utf-8")
        print (texto_enviar)
        sock.send(texto_enviar)
        data = sock.recv(4096)
        Respuesta = data.decode()[12:]
        print (Respuesta)
        print("Respondiendo solicitud juego: "+ texto)
        await ctx.send(Respuesta)

@bot.command(pass_context = True, name = "rolxd")

async def rolxd(ctx):
        client=discord.Client()
        texto = str(ctx.message.content)[5:]
        print(texto+"roles")
        texto_enviar = genPrefix(len(texto), "rolxd") + texto
        texto_enviar = texto_enviar.encode("utf-8")
        sock.send(texto_enviar)
        print (texto_enviar)
        member=ctx.message.author
        role=get(member.guild.roles,name=texto)
        data=sock.recv(4096)
        respuesta=data.decode()[12:]
        print(respuesta)
        await member.add_roles(member,role)
        
bot.run(TOKEN)