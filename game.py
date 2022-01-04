import socket
import os
import json
import urllib
import urllib.parse
import urllib.request
import random

def genPrefix(largo):
    num=str(largo+5)
    while(len(num)<5):
        num= "0"+num
    return num+"games"

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5000        # Port to listen on (non-privileged ports are > 1023)

#url="http://api.giphy.com/v1/gifs/random"
juego = ""
choice = ""
minimo = 1
maximo = 6

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(b'00010sinitgames')
    s.recv(4096)
    print('Servicio Juegos iniciado')
    while True:
        data = s.recv(4096)
        juego = data[10:].decode() #obtenemos el juego que quiere usar + opcion
        minimo = 1
        maximo = 6
        print (juego)
        if "ppt" in juego.lower():
            juego, choice = juego.split() #separamos juego y opcion
            print ("Juego:", juego, "Elección:",choice)
            CHOICES = 'rps'
            diccionario = {'piedra':"r",'tijera':"s",'papel':"p"}
            inverse={"r":'piedra',"s":'tijera',"p":'papel'}
            def get_player_choice(choice): #opción de jugador
                choice = diccionario[choice]
                player_choice = choice
                return player_choice
            
            def get_computer_choice():#opción del bot
                computer_choice = random.randint(0, 2)
                computer_choice = CHOICES[computer_choice]
                return computer_choice

            
            def is_draw(player_choice, computer_choice): #en caso de empate
                if player_choice == computer_choice:
                    return True


            def print_winner(player_choice, computer_choice):#ganadores
                if player_choice == 'r' and computer_choice == 's':
                    print('Jugador gana!')
                    return ('Jugador gana!')
                elif player_choice == 's' and computer_choice == 'p':
                    print('Jugador gana!')
                    return ('Jugador gana!')
                elif player_choice == 'p' and computer_choice == 'r':
                    print('Jugador gana!')
                    return ('Jugador gana!')

                else:
                    print('Bot gana!')

                    print('%s beats %s' % (inverse[computer_choice], inverse[player_choice]))
                    return ('Bot gana!')
            
            def play_game(choice):#main, juego.
                player_choice = get_player_choice(choice)
                computer_choice = get_computer_choice()
                player_option=inverse[player_choice]
                computer_option=inverse[computer_choice]
                if is_draw(player_choice, computer_choice):
                    print("Es un empate, ambos eligieron %s " % player_option)
                    return("Es un empate, ambos eligieron %s " % player_option)
                else:
                    print("El bot eligio: %s" % computer_option)
                    print("Jugador eligio: %s" % player_option)

                    return print_winner(player_choice, computer_choice)      
            resultado = play_game(choice)
            prefix = genPrefix(len(resultado))
            s.send((prefix+resultado).encode("utf-8"))

        if "dados" in juego.lower():#juego de dados
            if len(juego) > 5:
                maximo=int(juego.split()[1])
            roll = random.randint(minimo,maximo)
            roll = "El dado rolleo: " + str(roll)
            prefix = genPrefix(len(roll))
            s.send((prefix+roll).encode("utf-8"))