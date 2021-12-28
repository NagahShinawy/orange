"""
handle network logic
"""


class CRUDMixin:
    """
    generic class for crud operations add/list/get/delete/update
    """

    def add(self):
        """
        add subnet or vlan
        :return:
        """

    def delete(self, _id):
        """
        delete subnet or vlan
        :return:
        """

    def update(self, _id):
        """
        update subnet or vlan
        :return:
        """

    def get(self, _id):
        """
        get details subnet or vlan
        :return:
        """


class Subnet(CRUDMixin):
    """
    class for subnet operations
    """


class VLAN:
    """
        class for VLAN operations
    """

    def __init__(self, subnet):
        self.subnet = subnet
