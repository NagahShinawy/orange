"""
entry point of the app
"""
from cli import CLI
from constants import CLOSE, END


# todo : 1- tests (unittest)
# todo : 2- pylint
# todo : 3- black
# todo : 4- oop
# todo : 5- docs
# todo : 6- isort


def main():
    """
    app entry point
    :return: None
    """
    cli = CLI()
    while cli != CLOSE:
        pass

    print(END)


if __name__ == "__main__":
    main()
