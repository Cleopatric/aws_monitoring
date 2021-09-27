""" Module with Instance Resource."""

from botocore.exceptions import ClientError
from nested_lookup import nested_lookup

from helpers.ec2_resource import Ec2Resource
from helpers.volume_resource import Ec2Volume


class Instance(Ec2Resource):
    """ Wrapper class for EC2."""

    def __init__(self, instance_ids: str):
        """ Crate instance wrapper by instance id.

        :param instance_ids: id of necessary instance.
        """
        Ec2Resource.__init__(self)
        self.instance_ids = instance_ids
        instance = self.get_instance_attributes()
        self.private_ip = instance.private_ip_address
        self.tags = instance.tags
        self.ssh_key_name = instance.key_name
        self.subnet_id = instance.subnet_id
        self.network = instance.network_interfaces_attribute
        self.availability_zone = instance.subnet.availability_zone
        self.state = instance.state
        self.instance_type = instance.instance_type
        self.interfaces_id = instance.network_interfaces[0].id
        self.device_type = instance.root_device_type
        self.devise_size = instance
        self.volume_ids = self.get_volume_id(instance)
        self.volume = Ec2Volume(self.volume_ids)
        self.size = self.volume.size

    def get_instance_attributes(self):
        """ Get all instance data by id for attributes.

        :return: instance by id.
        """
        return self.resource.Instance(self.instance_ids)

    def run_instances(self, dry_run=False):
        """ Start an Amazon EBS-backed AMI.

        :param dry_run: param for to verify permissions.
        """
        try:
            self.client.start_instances(InstanceIds=self.instance_ids.split(), DryRun=dry_run)
        except ClientError as exp:
            print(exp)

    def stopping_instances(self, dry_run=False):
        """ Stop an Amazon EBS-backed instance using stop_instances.

        :param dry_run: param for to verify permissions.
        """
        try:
            self.client.stop_instances(InstanceIds=self.instance_ids.split(), DryRun=dry_run)
        except ClientError as exp:
            print(exp)

    def rebooting_instances(self, dry_run=False):
        """ Request a reboot of one or more instances using reboot_instances.

        :param dry_run: param for to verify permissions.
        """
        self.client.reboot_instances(InstanceIds=self.instance_ids.split(), DryRun=dry_run)

    def get_instances_ids(self) -> list:
        """ Get all instances ids from boto_project.

        :return: list with instances ids.
        """
        return [instance.id for instance in self.resource.instances.all()]

    def get_instances(self) -> list:
        """ Get all instances.

        :return: list with instances.
        """
        instances = list(self.resource.instances.all())
        return instances

    def get_volume_id(self, instance) -> str:
        """ Get volume id by instance.

        :param instance: instance with necessary id.
        :return:         volume id.
        """
        volume_id = nested_lookup('VolumeId', instance.block_device_mappings)
        return volume_id
