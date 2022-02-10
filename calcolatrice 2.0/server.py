import socket
import json
from threading import Thread
from traceback import print_tb

HOST='127.0.0.1'
PORT=22004
#funziona che riceve i comandi dal client
def ricevi_comandi(sock_service,addr_client):
    print("avviato per servire", addr_client)
    while True:
        #riceve i dati
        data=sock_service.recv(1024)
        # if len(data)==0:
        if not data:
            break
        #decodifica i dati
        data=data.decode()
        data=json.loads(data)
        #esecuzione dei comandi
        primoNumero=data['primoNumero']
        operazione=data['operazione']
        secondoNumero=data['secondoNumero']
        ris=""
        if operazione=="+":
            ris=primoNumero+secondoNumero
        elif operazione=="-":
            ris=primoNumero-secondoNumero
        elif operazione=="*":
            ris=primoNumero*secondoNumero
        elif operazione=="/":
            if secondoNumero==0:
                ris="Non puoi dividere per 0"
            else:
                ris=primoNumero/secondoNumero
        elif operazione=="%":
            ris=primoNumero%secondoNumero
        else:
            ris="Operazione non riconosciuta"
            ris=str(ris)
        ris=str(ris)
        sock_service.sendall(ris.encode("UTF-8"))
#ricezione connessioni dal parte dei client
def ricevi_connessioni(sock_listen):
    while True:
        sock_service, addr_client = sock_listen.accept()
        print("\nConnessione ricevuta da " + str(addr_client))
        print("\nCreo un thread per servire le richieste ")
        try:
            #esecuzione thread che riceve i comandi
            Thread(target=ricevi_comandi, args=(sock_service,addr_client)).start()
        except:
            print("Il thread non si avvia")
            sock_listen.close()
#avvio del server
def avvia_server(address,port):
    sock_listen=socket.socket()
    sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_listen.bind((address,port))
    sock_listen.listen(5)
    print("Server in ascolto su %s." % str((address,port)))
    ricevi_connessioni(sock_listen)

if __name__=="__main__":
    avvia_server(HOST,PORT)