from email.message import Message
import socket
import json
HOST="127.0.0.1"
PORT=65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:  #indica il tipo di protocollo utilizzato, sock stram indica il tipo di connessione. with tiene aperto il socket dandogli il nome di s, una volta eseguito il codice chiude automaticamente il socket
    s.connect((HOST,PORT))
    while True:
        messaggio=input("Inserisci il messaggio, KO per uscire")
        if messaggio=="KO":
            s.close
            break
        messaggio={'messaggio':messaggio}
        messaggio=json.dumps(messaggio) #trasformiamo l'oggetto in una stringa
        s.sendall(messaggio.encode("UTF-8")) #invia il vettore di byte
        data=s.recv(1024)
        print("Risultato: ",data.decode())
