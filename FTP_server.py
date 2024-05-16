import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
lock = threading.Lock()


IPA = socket.gethostbyname(socket.gethostname())
port = 5500


ADDR = (IPA, port)
server.bind(ADDR)

users = {}
admin = {'qwerty' : '123456'}
clients = []
ban =[]
fileslist= []




def acceptor () :

    server.listen(5)
    print("SERVER IS RUNNING")
    client, addr = server.accept()
    clients.append(client)
    while True :    
        

        client.send("Welcome to the server\nEnter Username Command".encode())
        message =  client.recv(1024).decode()
        words = message.split()

        if words[1] in ban :
            client.send("You were Banned from the server".encode())

        else :    
             
            if (words[1]=='qwerty') :
                client.send("Enter Password Command".encode())
                message =  client.recv(1024).decode()
                words1 = message.split()

                if (words1[1] == '123456') :
                        
                        client.send("Admin Authentication Successful".encode())
                        thr = threading.Thread(target=handle_admin, args=(client,  ))
                        thr.start()
                else :
                        while (words1[1] != 'Admin@123') :
                            client.send("Incorrect Password.\nEnter the password again".encode())
                            message  = client.recv(1024).decode()
                            words1 = message.split() 

                        thr = threading.Thread(target=handle_client, args=(client,  ))
                        thr.start()


            elif words[1] in users :
                client.send("Enter Password Command".encode())
                message =  client.recv(1024).decode()
                words1 = message.split()
                
                if (words1[1] == users[words[1]]) :
                        client.send("User Authentication Successful".encode())
                        thr = threading.Thread(target=handle_client, args=(client,  ))
                        thr.start()
                else :
                        while (words1[1] != users[words[1]]) :
                            client.send("Incorrect Password.\nEnter the password again".encode())
                            message  = client.recv(1024).decode()
                            words1 = message.split() 

                        thr = threading.Thread(target=handle_client, args=(client,  ))
                        thr.start()
            

            else :
                client.send("Username not found or Incorrect".encode())
                


     

def handle_admin(client) :
    while True :
        try:    
            message = client.recv(1024).decode()
            words = message.split()
            command = words[0]
            if (command == "LIST") :
               info_str = ','.join(map(str, fileslist))
               client.sendall(info_str.encode())
            elif(command == "RETR") :
               file_Name = words[1]
               file_Content = open( words[1], 'rb').read()
               client.send(file_Content)
            elif(command == "STOR") :
               file_Name = words[1]
               file_Content = words[2].encode()
               with lock:
                    open(file_Name, 'wb').write(file_Content)
                    fileslist[file_Name] = file_Name
            elif(command == "QUIT") :
                 pass
            elif(command == "ADDUSER") :
                 users[words[1]]=words[2]
                 print(f"{words[1]} user added successfully")
            elif(command == "DELUSER") :
                 del users[words[1]]
                 print(f"{words[1]} user was removed")
            elif(command == "BAN") :
                 ban.append(words[1])
                 print(f"{words[1]} user was banned")
            elif(command == "UNBAN") :
                 ban.remove(words[1])
                 print(f"{words[1]} user was unbanned")
        
        except :
            print("An ERROR OCCURED")
            clients.remove(client)
            client.close()
            break
    


def handle_client (client,) :

    while True:
        try:    
            message = client.recv(1024).decode()
            words = message.split()
            command = words[0]
            
            if (command == "LIST") :
               info_str = ','.join(map(str, fileslist))
               client.sendall(info_str.encode())

            elif(command == "RETR") :
               file_Name = words[1]
               file_Content = open( words[1], 'rb').read()
               client.send(file_Content)
            
            elif(command == "STOR") :
               file_Name = words[1]
               file_Content = words[2].encode()
               with lock:
                    open(file_Name, 'wb').write(file_Content)
                    fileslist[file_Name] = file_Name

            elif(command == "QUIT") :
                 pass

        except:
           
            clients.remove(client)
            client.close()
            break
        

acceptor()