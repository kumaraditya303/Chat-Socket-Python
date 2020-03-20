# Python Socket Based Chat made by Kumar Aditya


import time
import socket
import sys
import os
from colorama import *

os.system('cls')
title = "\t\t\tPython Socket Based Chat\n"
print(title)
print("Enter same IP address as other user!")
server_host = input("Enter IP address: ")
name = input("Enter your name: ")
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1234
soc.bind((server_host, port))
soc.listen(1)
connection, addr = soc.accept()
client_name = connection.recv(1024).decode()
connection.send(name.encode())
time.sleep(1)
os.system("cls")
print(title)
print(f"Me : {name}\t\t\t You : {client_name}\n")
print("Enter Bye to close the chat!\n")
while True:
    message = input(Fore.RED+'Me > ')
    if(message.upper() == 'BYE'):
        sys.exit()
    connection.send(message.encode())
    message = connection.recv(1024)
    message = message.decode()
    if(message.upper() == 'BYE'):
        sys.exit()
    print(Fore.GREEN+client_name, '>', message)
