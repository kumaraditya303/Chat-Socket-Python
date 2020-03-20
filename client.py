# Python Socket Based Chat made by Kumar Aditya


import socket
import sys
import os
import time
from colorama import *
os.system('cls')
title = "\t\t\tPython Socket Based Chat\n"
print(title)
print("Enter same IP address as other user!")
server_host = input("Enter IP address: ")
name = input("Enter your name: ")
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1234

soc.connect((server_host, port))
soc.send(name.encode())
server_name = soc.recv(1024).decode()
time.sleep(1)
os.system("cls")
print(title)
print(f"Me : {name}\t\t\t You : {server_name}\n")
print("Enter Bye to close the chat!\n")
while True:
    message = soc.recv(1024)
    message = message.decode()
    if(message.upper() == 'BYE'):
        sys.exit()
    print(Fore.GREEN+server_name, ">", message)
    message = input(Fore.RED+"Me > ")
    if(message.upper() == 'BYE'):
        sys.exit()
    soc.send(message.encode())
