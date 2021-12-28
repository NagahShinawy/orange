"""
command line interface
"""
from constants import USER_ACTIONS, INVALID_COMMAND, AVAILABLE_COMMANDS


class CLI:
    """
    handle user interacting with terminal
    """

    COMMANDS = USER_ACTIONS  # valid user actions

    def __init__(self):
        self.command = input(AVAILABLE_COMMANDS).lower()

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
        :return: validated command value from (a, l, d, u, r, s )
        """
        while value not in self.COMMANDS:
            value = input(INVALID_COMMAND.format(command=value))

        return super().__setattr__(prop, value)

    def __eq__(self, other) -> bool:
        """
        easy comparison between CLI obj and str obj
        :param other: str obj to compare with CLI obj
        :return: bool True for match user input and validate command.
        """
        return self.command == other
