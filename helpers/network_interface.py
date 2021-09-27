""" Module with Network Interface Resource."""

from helpers.ec2_resource import Ec2Resource


class NetworkInterface(Ec2Resource):
    """ Wrapper class for NetworkInterface."""

    def __init__(self, eni_id: str):
        """ A resource representing EC2 NetworkInterface.

        :param eni_id:                 network interface id.
        :param self.status: status:    start/stop/reboot/terminate.
        :param self.interface_type:    type of interface.
        :param self.private_ip:        private ip address.
        :param self.mac_address:       network interface mac address.
        :param self.availability_zone: availability zone.
        :param self.groups:            groups for instance.
        """
        self.eni_id = eni_id
        super(NetworkInterface, self).__init__()
        network_interface = self.resource.NetworkInterface(eni_id)
        self.groups = network_interface.groups
        self.status = network_interface.status
        self.interface_type = network_interface.interface_type
        self.private_ip = network_interface.private_ip_address
        self.mac_address = network_interface.mac_address
        self.availability_zone = network_interface.availability_zone
        self.network_interface = network_interface
