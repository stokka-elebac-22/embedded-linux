#!/usr/bin/env python
"""__init__.py: CAN bus Socket communication server."""
__author__ = "Asbjørn Stokka"
__copyright__ = "Copyright 2022, ELEBAC"
__credits__ = ["Asbjørn Stokka"]
__license__ = "Apache-2.0"
__version__ = "0.1.0"
__maintainer__ = "Asbjørn Stokka"
__email__ = "asbjorn@maxit-as.com"
__status__ = "Testing"

from multi_socket_server import multi_socket_server as socket_handler
from can_handler import canbus_handler

socket_server = socket_handler()
socket_server.start()
canbus = canbus_handler()
canbus.start()
while True:
    try:
        msg = canbus.get_next_message()
        socket_server.send_to_all(msg)
        print("CANBus: " + msg)
    except: 
        pass
    try:
        msg = socket_server.get_next_message()
        canbus.send_to_all(msg)
        print("Socket: " + msg)
    except: 
        pass
