#!/usr/bin/env python
"""can_handler.py: Class for handling CAN communication."""
__author__ = "Asbjørn Stokka"
__copyright__ = "Copyright 2022, ELEBAC"
__credits__ = ["Asbjørn Stokka"]
__license__ = "Apache-2.0"
__version__ = "0.1.0"
__maintainer__ = "Asbjørn Stokka"
__email__ = "asbjorn@maxit-as.com"
__status__ = "Testing"

import can
import time
import queue
from can.bus import BusState
from _thread import *

class canbus_handler():
    def __init__(self):
        """Receives all messages and prints them to the console until Ctrl+C is pressed."""
        self.host = "10.0.10.95" #socket.gethostname()
        self.port = 5000  # initiate port no above 1024
        self.running = False
        self.incoming_data  = queue.Queue()

    def start(self):
        self.running = True
        start_new_thread(self.run_server, ())

    def run_server(self):
        self.bus = can.Bus(interface='socketcan', channel='can0', receive_own_messages=True)
        try:
            while self.running:
                print("CAN bus connected ...")
                msg = self.bus.recv(2)
                if msg is not None:
                    print("Received data ...")
                    print(msg.data)
                    print(msg.arbitration_id)
                    a_id = bytearray(0)
                    a_id.append(msg.arbitration_id)
                    my_bytes = bytearray(a_id + msg.data) 
                    print(my_bytes)
                    self.incoming_data.put(my_bytes)

        except KeyboardInterrupt:
            pass  # exit

    def send_to_all(self, message):
        msg = can.Message(arbitration_id=message[0], is_extended_id=False, data=[message[1], message[2], message[3]])
        self.bus.send(msg, timeout=0.2)

    def stop(self):
        self.running = False

    def get_next_message(self):
        if not self.incoming_data.empty():
            return self.incoming_data.get()

if __name__ == '__main__':
    pass
