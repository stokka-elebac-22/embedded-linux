"""defines.py: Class for enums to ensure consistency in values across platforms."""
__author__ = "Asbjørn Stokka"
__copyright__ = "Copyright 2022, ELEBAC"
__credits__ = ["Asbjørn Stokka"]
__license__ = "Apache-2.0"
__version__ = "0.1.0"
__maintainer__ = "Asbjørn Stokka"
__email__ = "asbjorn@maxit-as.com"
__status__ = "Testing"

from enum import Enum

class Position(Enum):
    BACK_RIGHT = 0
    FRONT_RIGHT = 1
    BACK_LEFT = 2
    FRONT_LEFT = 3

class Message_Id(Enum):
    CAN_MOTOR_DATA_ID = 16       # 0x010
    CAN_LIGHT_CONTROL_ID = 17    # 0x011
    CAN_BLINK_CONTROL_ID = 18    # 0x012
    CAN_SENSOR_DATA_ID = 48      # 0x030
    CAN_TEST_MSG_ID = 80         # 0x050
    CAN_DEVICE_SETTINGS_ID = 96  # 0x060

if __name__ == "__main__":
    test = Position(3)
    print("current position is " + test.name)
    test = Position.BACK_LEFT
    print("current position is " + test.name)
    message = Message_Id.CAN_TEST_MSG_ID
    print("CAN message Id: " + message.name + " value: " + hex(message.value))
