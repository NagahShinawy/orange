"""
input validation for example IP validation
class BaseValidator:
"""
from abc import ABC
from constants import INVALID_COMMAND, INVALID_CHOOSE
from logs import logger


class BaseValidator(ABC):
    """
    base validation class
    """

    def __init__(self, value):
        self.value = value

    def validate(self):
        pass


class MenuValidator(BaseValidator):
    USER_ACTIONS = ("l", "a", "u", "d", "s", "r", "q")

    def validate(self):
        while self.value not in self.USER_ACTIONS:
            logger.error(f"invalid command '%s'", self.value)
            self.value = input(INVALID_COMMAND.format(command=self.value))
        return self.value


class SubnetVlanValidator(BaseValidator):

    SUBNET = "subnet"
    VLAN = "vlan"

    SUBNET_VLAN = (SUBNET, VLAN)

    def validate(self):
        while self.value not in self.SUBNET_VLAN:
            logger.error(f"invalid choose '%s'", self.value)
            self.value = input(INVALID_CHOOSE.format(command=self.value))
        return self.value


