from email.message import Message
import socket
import json
HOST="127.0.0.1"
PORT=65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:  #indica il tipo di protocollo utilizzato, sock stram indica il tipo di connessione. with tiene aperto il socket dandogli il nome di s, una volta eseguito il codice chiude automaticamente il socket
    s.connect((HOST,PORT))
    while True:
        primoNumero=input("Inserisci il primo numero. exit() per uscire")
        if primoNumero=="exit()":
            break
        primoNumero=float(primoNumero)
        operazione=input("Inserisci l'operazione (+,-,*,/,%)")
        secondoNumero=float(input("Inserisci il secondo numero"))
        messaggio={'primoNumero':primoNumero,
        'operazione':operazione,
        'secondoNumero':secondoNumero}
        messaggio=json.dumps(messaggio) #trasformiamo l'oggetto in una stringa
        s.sendall(messaggio.encode("UTF-8")) #invia il vettore di byte
        data=s.recv(1024)
        print("Risultato: ",data.decode())
