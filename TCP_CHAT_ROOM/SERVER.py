import socket
import threading

ip_address = "127.0.0.1"
port = 9999

print("Start Running The TCP Server...")
print("Listening On Port 9999...")

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((ip_address,port))
s.listen()

print("The Server Is Listening...")

clients = []
client_names = []

def broad_cast(message):
    for client in clients:
        client.send(message)

def handling(client):
    while True:
        try:
            received_client_messages = client.recv(2048)
            broad_cast(received_client_messages)
        except:
            index = clients.index(client)
            clients.remove(client)
            client_name = client_names[index]
            broad_cast('{} Left The Chat Room !'.format(client_name).encode('ascii'))
            client_names.remove(client_name)
            break

def receiving():
    while True:
        client, address = s.accept()
        print(f"Connect With Address {str(address)}.")

        client.send('NICK'.encode('ascii'))
        client_name = client.recv(2048).decode('ascii')
        clients.append(client)
        client_names.append(str(client_name))

        print(f"Client Name Is {client_name}")
        broad_cast("{} Has Joined !".format(client_name).encode('ascii'))
        client.send('SuccessFully Connect To Server'.encode('ascii'))

        thread = threading.Thread(target=handling, args=(client,))
        thread.start()

print("Waiting For Any Incoming TCP Connection...")
receiving()