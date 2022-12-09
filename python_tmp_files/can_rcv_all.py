#!/usr/bin/env python
"""
Receives messages via polling.
"""
import can
import time
from can.bus import BusState

def receive_all():
    """Receives all messages and prints them to the console until Ctrl+C is pressed."""
    # this uses the default configuration (for example from environment variables, or a
    # config file) see https://python-can.readthedocs.io/en/stable/configuration.html
    with can.Bus(interface='socketcan', channel='can0', receive_own_messages=True) as bus:
        prevTime = time.time()
        try:
            while True:
                msg = bus.recv(1)
                if msg is not None:
                    print(msg)
                if (time.time() - prevTime > 10):
                    prevTime = time.time()
                    message = can.Message(arbitration_id=11, is_extended_id=False, timeout=1, data=[0x11, 0x22, 0x33])
                    bus.send(message, timeout=0.2)
        except KeyboardInterrupt:
            pass  # exit normally


if __name__ == "__main__":
    receive_all()
