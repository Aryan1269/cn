import socket

def client_prog():
    host=socket.gethostname() # find the host name since both progs are running on the same pc
    port=5000
    
    client_sc=socket.socket() # instantiate socket
    client_sc.connect((host,port))
    try:
        
        while 1:
            data=client_sc.recv(1024).decode()
            print("Data= ",data)
            if(data=="END"):
                break
            rec="Acknowledgment for data-"+data
            client_sc.send(rec.encode())
    except:
        print("Connection Failed")
            
    client_sc.close()
if __name__=="__main__":
    client_prog()
        