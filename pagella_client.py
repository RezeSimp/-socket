from email.message import Message
import socket
import json
HOST="127.0.0.1"
PORT=65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:  #indica il tipo di protocollo utilizzato, sock stram indica il tipo di connessione. with tiene aperto il socket dandogli il nome di s, una volta eseguito il codice chiude automaticamente il socket
    s.connect((HOST,PORT))
    while True:
        comando=input("Inserisci il comando: ")
        comando={'comando':comando}
        comando=json.dumps(comando) #trasformiamo l'oggetto in una stringa
        s.sendall(comando.encode("UTF-8")) #invia il vettore di byte
        data=s.recv(1024)
        data.decode()
        if comando == "#list":
            deserialized_dict=json.loads(data)
            print(deserialized_dict)
        elif comando == "#list":
            deserialized_dict=json.loads(data)
            print(deserialized_dict)
        else:
            print(data)
