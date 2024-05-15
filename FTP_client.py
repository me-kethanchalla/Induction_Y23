import socket
import threading


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IPA = socket.gethostbyname(socket.gethostname())
port = 5500

ADDR = (IPA, port)
client.connect(ADDR)

while True :
    message = client.recv(1024).decode()
    print(message)
    USERNAME = input()
    client.send(USERNAME.encode())
    message = client.recv(1024).decode()
    if (message == "Enter Password Command") :
        while True :
            print(message)
            PASSWORD = input()
            client.send(PASSWORD.encode())
            message = client.recv(1024).decode()
            if (message == "Incorrect Password.\nEnter the password again") :
                print(message)
                continue
            else :
                print(message)
                break
        break

    else : 
        print(message)
        continue



def allcommands () :
    try :
        message = input()
        breakwords = message.split()

        if (breakwords[0]=="LIST") :
            client.send("LIST".encode())
            data = client.recv(1024).decode()
            fileslist = list(map(int, data.split(',')))
            print(fileslist)

        elif(breakwords[0]=="STOR") :
            file_content = open( breakwords[1], 'rb').read()
            file_name = breakwords[1]
            client.send(f"STOR {file_name} {file_content}")
        
        elif(breakwords[0]=="RETR") :
            file_name = breakwords[1]
            client.send(f"RETR {file_name}")
            file_content = b""
            while True:
                data = client.recv(1024)
                if not data:
                    break
                file_content += data
        
            open(breakwords[1], 'wb').write(file_content)
        
        elif(breakwords[0]=="QUIT") :
            pass
        elif(breakwords[0]=="ADDUSER") :
            client.send(message.encode())
        elif(breakwords[0]=="DELUSER") :
            client.send(message.encode())
        elif(breakwords[0]=="BAN") :
            client.send(message.encode())
        elif(breakwords[0]=="UNBAN") :
            client.send(message.encode())    


    
    except :
        print("An Error Occured")
        client.close()



THE_thread = threading.Thread(target=allcommands)

THE_thread.start()