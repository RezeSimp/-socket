from audioop import add
from email.message import Message
import socket
import json
HOST="127.0.0.1"
PORT=22004
#invio dei comandi
def invia_comandi(sock_service):
    while True:
        primoNumero=input("Inserisci il primo numero. exit() per uscire: ")
        if primoNumero=="exit()":
            break
        primoNumero=float(primoNumero)
        operazione=input("Inserisci l'operazione (+,-,*,/,%): ")
        secondoNumero=float(input("Inserisci il secondo numero: "))
        messaggio={'primoNumero':primoNumero,
        'operazione':operazione,
        'secondoNumero':secondoNumero}
        messaggio=json.dumps(messaggio)
        #invio del messaggio al server
        sock_service.sendall(messaggio.encode("UTF-8"))
        #ricezione del risultato
        data=sock_service.recv(1024)
        #output risultato dei dati decodificati
        print("Risultato: ",data.decode())
#connessione al server
def connessione_server(address,port):
    sock_service= socket.socket()
    sock_service.connect((address,port))
    print("Connesso a " + str((address,port)))
    invia_comandi(sock_service)
    
if __name__=='__main__':
    connessione_server(HOST,PORT)

