import socket

def client_prog():
    host=socket.gethostname() # find the host name since both progs are running on the same pc
    port=5000
    
    client_sc=socket.socket() # instantiate socket
    try:
        client_sc.connect((host,port))
    
    
        while 1:
            msg=input("Enter the input:- ")
            client_sc.send(msg.encode())
            
            if msg=="END":
                client_sc.close()
                print("Connection Closed")
                break
    except:
        print("Connection failed")

if __name__=="__main__":
    client_prog()
        