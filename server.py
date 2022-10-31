import socket

def server_prog():
    host=socket.gethostname()
    port=5000
    
    sr_socket=socket.socket()
    sr_socket.bind((host,port))
    
    sr_socket.listen(1)
    print("Listening...")
    try:
        conn,address=sr_socket.accept()
        print("Connection from: "+str(address))
        
        while True:
            data=conn.recv(1024).decode()
            
            if not data:
                break
            print("Print Data:- "+str(data))
            
        conn.close()
    except:
        print("Connection Failed")
        
if __name__ == '__main__':
    server_prog()
        