import socket
import sys


def create_socket():
  try:
      global host
      global port
      global soc
      host = ""
      port = 1104
      soc = socket.socket()
   except socket.errror as msg:
    try:
        global host
        global port
        global soc
        
        print("Binding the port" + str(port))
        
        soc.bind((host,port))
        s.listen(2)
        
    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying....")
        bind_socket()
