"""Module with S3 Resource."""
import boto3


class S3Resource:
    """ Wrapper class for S3."""

    def __init__(self):
        """ Create a S3 resource.

        :param self.resource: resource service client.
        :param self.client: service client.
        """
        self.resource = boto3.resource('s3')
        self.client = boto3.client('s3')

    def get_buckets(self) -> list:
        """ Get list of all buckets.

        :return: list of buckets names.
        """
        buckets = [bucket.name for bucket in self.resource.buckets.all()]
        return buckets

    def get_bucket_items(self, bucket_name: str) -> list:
        """ Get all items in bucket by backet name.

        :param bucket_name: name of the backet.
        :return:            list of items.
        """
        if bucket_name in self.get_buckets():
            bucket = self.resource.Bucket(name=bucket_name)
            items = [bucket_object for bucket_object in bucket.objects.all()]
            return items

    def list_bucket_contents(self, bucket_name: str) -> list:
        """ List with all bucket nesting.

        :param bucket_name: name of the backet.
        :return:            list with bucket nesting.
        """
        objects = [object for object in
                   self.client.list_objects_v2(Bucket=bucket_name)]
        return objects
