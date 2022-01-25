import socket
import json

HOST='127.0.0.1'
PORT=65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    print("[*] In ascolto su %s:%d"%(HOST,PORT))
    clientsocket, address=s.accept() #accetta la connessione del socket
    with clientsocket as cs:
        print("Connessione da ",address)
        contatore=0
        while True:
            data=cs.recv(1024)
            # if len(data)==0:
            if not data:
                break
            data=data.decode()
            data=json.loads(data)
            messaggio=data['messaggio']
            c=str(contatore)
            ris=messaggio+ ' ' + c
            contatore=contatore+1
            cs.sendall(ris.encode("UTF-8"))