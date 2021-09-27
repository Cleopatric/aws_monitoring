""" Module that create wrapper for Ec2Resource."""

import boto3


class Ec2Resource:
    """ Ec2Resource class for creating ec2 wrapper."""

    def __init__(self):
        """ Create a resource service/low-level service clients.

        :param self.resource: resource service client.
        :param self.client: service client.
        """
        self.resource = boto3.resource('ec2')
        self.client = boto3.client('ec2')

    def get_instances_data(self) -> dict:
        """ Get data from all instances.

        :return: dict with data from all instances.
        """
        response = self.client.describe_instances()
        return response
