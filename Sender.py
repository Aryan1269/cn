import socket

def server_prog():
    host=socket.gethostname()
    port=5000
    
    sr=socket.socket()
    sr.bind((host,port))
    
    sr.listen(2)
    print("Listening...")
    
    
    conn,adress=sr.accept()
    print("Connection Established")
    print(adress)
    try:
        while 1:
            data=input("Enter the data:- ")
            conn.send(data.encode())
            
            print("Rec:- ",conn.recv(1024).decode())
    except:
        print("Connection Failed")
        
        
        
        
if __name__ == '__main__':
    server_prog()
        