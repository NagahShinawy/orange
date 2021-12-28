"""
input validation for example IP validation
class BaseValidator:
"""
from abc import ABC

from constants import INVALID_CHOOSE, INVALID_COMMAND
from logs import logger


class BaseValidator(ABC):
    """
    base validation class
    """

    OPTIONS = ()
    ERROR = "unknown error.Try again!"

    def __init__(self, value):
        self.value = value

    def validate(self):
        while self.value not in self.OPTIONS:
            logger.error(f"invalid command '%s'", self.value)
            self.value = input(self.ERROR.format(command=self.value))
        return self.value


class MenuValidator(BaseValidator):
    ERROR = INVALID_COMMAND
    OPTIONS = ("l", "a", "u", "d", "s", "r", "q")


class SubnetVlanValidator(BaseValidator):

    SUBNET = "subnet"
    VLAN = "vlan"

    ERROR = INVALID_CHOOSE
    OPTIONS = (SUBNET, VLAN)
