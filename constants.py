"""
store app constants values
"""

USER_ACTIONS = ("l", "a", "u", "d", "s", "r")

AVAILABLE_COMMANDS = """
Select 'l' for 'list'
Select 'a' for 'add'
Select 'u' for 'update'
Select 'd' for 'delete'
Select 's' for 'search'
Select 'r' for 'read' : 
"""

INVALID_COMMAND = "Invalid command '{command}'\n" + AVAILABLE_COMMANDS
