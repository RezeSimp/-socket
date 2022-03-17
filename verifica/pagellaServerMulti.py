#nome del file : pagellaServerMulti.py

import socket
from threading import Thread
import json


SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22225

#Versione 1 
def ricevi_comandi1(sock_service,addr_client):
    while True:
        data=sock_service.recv(1024)
        if not data: 
            break
        data=data.decode()
        data=json.loads(data)  
        #1. recuperare dal json studente, materia, voto e assenze
        cognome=data['cognome']
        materia=data['materia']
        voto=data['voto']
        assenze=data['assenze']
        #2. restituire un messaggio in json contenente studente, materia e una valutazione testuale :
        # voto < 4 Gravemente insufficiente
        # voto [4..5] Insufficiente
        # voto = 6 Sufficiente
        # voto = 7 Discreto 
        # voto [8..9] Buono
        # voto = 10 Ottimo
        
        if voto<4:
            valutazione="Gravemente insufficiente"
        elif voto==4 or voto==5:
            valutazione="Insufficiente"
        elif voto==6:
            valutazione="Sufficiente"
        elif voto==7:
            valutazione="Discreto"
        elif voto==8 or voto==9:
            valutazione="Buono"
        elif voto==10:
            valutazione="Ottimo"
        messaggio={'cognome':cognome,
            'materia':materia,
            'valutazione':valutazione}
        messaggio=json.dumps(messaggio)
        sock_service.sendall(messaggio.encode("UTF-8"))
    sock_service.close()

#Versione 2 
def ricevi_comandi2(sock_service,addr_client):
    while True:
        data=sock_service.recv(1024)
        if not data: 
                break
        data=data.decode()
        data=json.loads(data)
        cognome=data[0]
        media=0
        assenze=0
        print(cognome)
        for i in range(len(data[cognome])):
            media+=data[cognome][i][1]
            assenze+=data[cognome][i][2]
        media=media/5
        print(media,assenze)
        messaggio={'cognome':cognome,
            'media':media,
            'assenze':assenze}
        messaggio=json.dumps(messaggio)
        sock_service.sendall(messaggio.encode("UTF-8"))
    sock_service.close()
  
  #1.recuperare dal json studente e pagella
  #2. restituire studente, media dei voti e somma delle assenze :
  

#Versione 3
def ricevi_comandi3(sock_service,addr_client):
  #....
  #1.recuperare dal json il tabellone
  #2. restituire per ogni studente la media dei voti e somma delle assenze :
  pass


def ricevi_connessioni(sock_listen):
    while True:
        sock_service, addr_client = sock_listen.accept()
        print("\nConnessione ricevuta da " + str(addr_client))
        print("\nCreo un thread per servire le richieste ")
        try:
            Thread(target=ricevi_comandi1,args=(sock_service,addr_client)).start()
            Thread(target=ricevi_comandi2,args=(sock_service,addr_client)).start()
        except:
            print("il thread non si avvia")
            sock_listen.close()
        
def avvia_server(SERVER_ADDRESS,SERVER_PORT):
    sock_listen=socket.socket()
    sock_listen.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sock_listen.bind((SERVER_ADDRESS,SERVER_PORT))
    sock_listen.listen(5)
    print("Server in ascolto su %s." %str((SERVER_ADDRESS,SERVER_PORT)))
    ricevi_connessioni(sock_listen)

if __name__=='__main__':
    avvia_server(SERVER_ADDRESS,SERVER_PORT)
    