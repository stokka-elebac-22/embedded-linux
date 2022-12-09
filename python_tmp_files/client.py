import socket
from defines import *

def client_program():
    host = "10.0.10.95" #socket.gethostname()  # as both code is running on same pc
    port = 2004  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = " "  # take input

    while message.lower().strip() != 'bye':
        #client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024) # .decode()  # receive response
        if not data == None:
            #print('Received from server: ' + data.hex())  # show in terminal
            try:
                if (Message_Id(data[0]) == Message_Id.CAN_SENSOR_DATA_ID):
                    print(Message_Id(data[0]).name + " " + Position(data[1]).name + " - Sensor value: " + str(data[8]))
                elif (Message_Id(data[0]) == Message_Id.CAN_TEST_MSG_ID):
                    print("Test message received")
                else:
                    for x in range(len(data)):
                        print(data[x]) 
            except:
                pass
            #print(hex(data[1]))
            #print(''.join('{:02x}'.format(x) for x in data))
        

        # message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()