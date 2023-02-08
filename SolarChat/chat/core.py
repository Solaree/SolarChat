import socket, threading
from colorama import Fore

host = '127.0.0.1'
port = 9339

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):                                         
    while True:
        try:   #recieving valid messages from client
            message = client.recv(1024)
            broadcast(message)

        except: #removing clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

def receive(): #accepting multiple clients
    while True:
        client, address = server.accept()
        print(Fore.GREEN + '[DEBUG] ' + Fore.WHITE + 'Connected with {}'.format(str(address)))       
        client.send('NICKNAME'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        print(Fore.GREEN + '[DEBUG] ' + Fore.WHITE + 'Nickname is {}'.format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()