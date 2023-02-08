import socket, threading
from colorama import Fore

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket initialization
client.connect(('127.0.0.1', 9339))

def receive():
    while True: #making valid connection
        try:
            global message
            message = client.recv(1024).decode('ascii')
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
            else:
                print(message)

        except:
            print(Fore.RED + "An error occured!")
            client.close()
            break

def write():
    while True:
        message = '{}: {}'.format(nickname, input('')) #HTTP_API
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive) #receiving multiple messages
receive_thread.start()
write_thread = threading.Thread(target=write) #sending messages 
write_thread.start()