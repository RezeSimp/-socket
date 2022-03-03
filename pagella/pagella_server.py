from fileinput import close
from posixpath import split
import socket
import json

HOST='127.0.0.1'
PORT=22004

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    print("[*] In ascolto su %s:%d"%(HOST,PORT))
    clientsocket, address=s.accept() #accetta la connessione del socket
    with clientsocket as cs:
        print("Connessione da ",address)
        studenti= {
            'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7.5,4),("Storia",7.5,4),("Geografia",5,7)],
            'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9.5,0),("Storia",8,2),("Geografia",8,1)],
            'Nicola Spina':[("Matematica",7.5,2),("Italiano",6,2),("Inglese",4,3),("Storia",8.5,2),("Geografia",8,2)]
        }
        while True:
            data=cs.recv(1024)
            # if len(data)==0:
            if not data:
                break
            data=data.decode()
            data=json.loads(data)
            comando=data['comando']
            
            if comando == '#list':
                serialized_dict = json.dumps(studenti)
                cs.sendall(serialized_dict.encode("UTF-8"))
            
            if comando[0:4] == '#set':
                studente= comando.split('#set /')
                studenti.update({studente[1]:['',0,0]})
                ris="Inserimento avvenuto con successo"
                cs.sendall(ris.encode("UTF-8"))

            if comando[0:4] == '#put':
                comando=comando.split('#put /')
                studente=comando[1].split('/')
                studenti.update({studente[0]:[studente[1],int(studente[2]),int(studente[3])]})
                ris="Inserimento avvenuto con successo"
                cs.sendall(ris.encode("UTF-8"))

            if comando[0:4] == '#get':
                studente= comando.split('#get /')
                ris=studenti[studente[1]]
                serialized_dict = json.dumps(ris)
                cs.sendall(serialized_dict.encode("UTF-8"))

            if comando[0:5] == '#exit':
                s.close
            



