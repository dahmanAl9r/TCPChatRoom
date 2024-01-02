import socket
import threading
import tkinter.messagebox as msgb

client_name = input("Enter Your Name Here >>> ")

ip_address = "127.0.0.1"
port = 9999

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip_address,port))

def receiving():
    while True:
        try:
            message = s.recv(2048).decode('ascii')
            if message == "NICK":
                s.send(client_name.encode('ascii'))
            else:
                print(message)
        except:
            print("An Error Occured !")
            s.close()
            break

def writing():
    while True:
        message = '{}: {}'.format(client_name, input(''))
        s.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receiving)
receive_thread.start()

write_thread = threading.Thread(target=writing)
write_thread.start()