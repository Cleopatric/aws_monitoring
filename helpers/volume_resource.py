""" Module with Volume Resource."""
from helpers.ec2_resource import Ec2Resource


class Ec2Volume(Ec2Resource):
    """ A resource wrapper representing EC2 Volume."""

    def __init__(self, volume_ids):
        """ Crate volume wrapper by volume id.

        :param volume_ids:       volume id.
        :param self.volume:      volume instance.
        :param self.size: device size.
        :param self.attachments: volume attachments.
        :param self.snapshots:   all snapshots.
        :param self.create_time: volume create_time.
        :param self.snapshot_id: volume snapshot id.
        """
        Ec2Resource.__init__(self)
        self.volume_id = volume_ids[0]
        self.volume = self.resource.Volume(self.volume_id)
        self.size = self.volume.size
        self.attachments = self.volume.attachments
        self.snapshot_id = self.volume.snapshot_id
        self.snapshots = self.volume.snapshots
        self.create_time = self.volume.create_time
