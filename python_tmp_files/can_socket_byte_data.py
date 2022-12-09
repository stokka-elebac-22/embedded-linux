import can
import time
import socket
from can.bus import BusState

def server_program():
    """Receives all messages and prints them to the console until Ctrl+C is pressed."""
    # this uses the default configuration (for example from environment variables, or a
    # config file) see https://python-can.readthedocs.io/en/stable/configuration.html
    # get the hostname
    host = "10.0.10.95" #socket.gethostname()
    port = 5000  # initiate port no above 1024
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address) + " - Starts listening on CAN bus.")

    with can.Bus(interface='socketcan', channel='can0', receive_own_messages=True) as bus:
        try:
            while True:
                print("ready/starting")
                msg = bus.recv(1)
                if msg is not None:
                    print("sending data ...")
                    my_bytes = bytearray()
                    my_bytes.append(msg.arbitration_id)
                    my_bytes += msg.data
                    conn.send(my_bytes)
                    # conn.send("{}".format(msg).encode())
                # send a message
                # message = can.Message(arbitration_id=5, is_extended_id=False, data=[0x11, 0x22, 0x33])
                # bus.send(message, timeout=0.2)
        except KeyboardInterrupt:
            pass  # exit normally

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()