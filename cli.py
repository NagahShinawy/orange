"""
command line interface
"""
from constants import AVAILABLE_COMMANDS, SUBNET_OR_VLAN
from validation import MenuValidator, SubnetVlanValidator


class CLI:
    """
    handle user interacting with terminal
    """

    USER_ACTIONS = ("l", "a", "u", "d", "s", "r")

    SUBNET = "subnet"
    VLAN = "vlan"

    SUBNET_VLAN = (SUBNET, VLAN)

    def __init__(self):
        self.subnet_or_vlan = input(SUBNET_OR_VLAN)
        self.command = input(AVAILABLE_COMMANDS)

    def __repr__(self):
        """
        for obj debugging representation
        :return:
        """
        return f"{self.__class__.__name__}({self.command})"

    def __setattr__(self, prop, value):
        """
        set and check command value
        :param prop: property name. ex: command
        :param value: command value. ex: a for add, l for list ....
        :return: validated command value ex: (a, l, d, u, r, s ... )
        """

        value = value.lower()

        if prop == "subnet_or_vlan":
            value = SubnetVlanValidator(value).validate()

        if prop == "command":
            value = MenuValidator(value).validate()

        return super().__setattr__(prop, value)

    def __eq__(self, other) -> bool:
        """
        easy comparison between CLI obj and str obj
        :param other: str obj to compare with CLI obj
        :return: bool True for match user input and validate command.
        """
        return self.command == other
