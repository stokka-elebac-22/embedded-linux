#!/usr/bin/env python
"""abstract_server.py: Abstract class for communication server."""
__author__ = "Asbjørn Stokka"
__copyright__ = "Copyright 2022, ELEBAC"
__credits__ = ["Asbjørn Stokka"]
__license__ = "Apache-2.0"
__version__ = "0.1.0"
__maintainer__ = "Asbjørn Stokka"
__email__ = "asbjorn@maxit-as.com"
__status__ = "Testing"

from abc import (ABC, abstractmethod,)

class BasicServer(ABC):
  def __init__(self):
    pass # print("Initialized server object")

  @abstractmethod
  def start(self):
    pass # print("start server!")

  @abstractmethod
  def stop(self):
    pass # print("Stopping server!")
    
  @abstractmethod
  def send_to_all(self, message):
    pass # print("Send message to all!")

  @abstractmethod
  def get_next_message(self):
    pass # print("Get next available message!")
