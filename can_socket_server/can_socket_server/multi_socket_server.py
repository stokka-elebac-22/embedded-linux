#!/usr/bin/env python
"""multi_socket_server.py: Multithread socket server for passing through CAN bus data from Embedded Linux."""
__author__ = "Asbjørn Stokka"
__copyright__ = "Copyright 2022, ELEBAC"
__credits__ = ["Asbjørn Stokka"]
__license__ = "Apache-2.0"
__version__ = "0.1.0"
__maintainer__ = "Asbjørn Stokka"
__email__ = "asbjorn@maxit-as.com"
__status__ = "Testing"

import socket
import time
import queue
import os
from _thread import *
from abstract_server import BasicServer

class multi_socket_server(BasicServer):
    def __init__(self):
        self.ServerSideSocket = socket.socket()
        self.host = '10.0.10.95'
        self.port = 2004
        self.ThreadCount = 0
        self.running = False
        self.clients = []
        self.incoming_data  = queue.Queue()

    def start(self):
        try:
            self.ServerSideSocket.bind((self.host, self.port))
        except socket.error as e:
            print(str(e))
        print('Socket is listening..')
        self.ServerSideSocket.listen(5)
        self.running = True
        start_new_thread(self.run_socket, () )
  
    def stop(self):
        self.running = False

    def run_socket(self):
        while self.running:
            Client, address = self.ServerSideSocket.accept()
            print('Connected to: ' + address[0] + ':' + str(address[1]))
            start_new_thread(self.multi_threaded_client, (Client, ))
            self.clients.append(Client)
            self.ThreadCount += 1
            print('Thread Number: ' + str(self.ThreadCount))
        self.ServerSideSocket.close()

    def multi_threaded_client(self, connection):
        connection.send(str.encode('Server is working:'))
        while True:
            try:
                data = connection.recv(2048)
                response = 'Server message: ' + data.decode('utf-8')
            except socket.error as e:
                self.ThreadCount -= 1
                print('Thread Number: ' + str(self.ThreadCount))
                print(str(e))
                self.clients.remove(connection)
                break
            if not data:
                break
            self.incoming_data.put(data)
            connection.sendall(str.encode(response))
        connection.close()

  
    def send_to_all(self, message):
        if message == None:
            return 
        for connection in self.clients:
            try:
                connection.sendall(message)
            except socket.error as e:
                continue
        print("Send:")
        print(message)

    def get_next_message(self):
        if not self.incoming_data.empty():
            return self.incoming_data.get()

if __name__ == "__main__":
    """Receive message from socket, send message to all connected clients, and sleep."""
    # This is meant for basic testing of server/client functionality by enabling basic transfer.
    print("Starting init")
    socket_server = multi_socket_server()
    print("Created object")
    socket_server.start()
    print("Started server")
    while True:
        print("Get next available message, if any!")
        print(socket_server.get_next_message())  
        print("Sending test message to any connected client")  
        socket_server.send_to_all("test-message")
        print("Sleeping")
        time.sleep(1)
