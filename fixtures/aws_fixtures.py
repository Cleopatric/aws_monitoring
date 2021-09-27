import yaml
import pytest
import os.path
import logging

from helpers.instance_resource import Instance

CONFIG_FILE = 'config.yaml'


@pytest.fixture(scope='module')
def config(request) -> dict:
    """Give data from config .yaml file.

    :param request: pytest request.
    :return:        dict from config file
    """
    filename = f"{str(request.fspath.dirname)}/{CONFIG_FILE}"
    if not os.path.exists(filename):
        logging.info(f'No such file or directory:{filename}')
    else:
        with open(filename) as file:
            config = yaml.safe_load(file)
        return config


@pytest.fixture(scope='module')
def aws_instance(expected_instance_id: str):
    """Give instance by instance_id.

    :param expected_instance_id: instance_id.
    :return:                     instance.
    """
    instance = Instance(expected_instance_id)
    return instance


@pytest.fixture(scope='module')
def expected_instance_id(config: dict) -> str:
    """Give value by "instance_id" key.

    :param config: dict from config file.
    :return:       instance_id.
    """
    return config.get('instance_id')


@pytest.fixture(scope='module')
def expected_state(config: dict) -> str:
    """Give value by "state" key.

    :param config: dict from config file.
    :return:       state.
    """
    return config.get('state')


@pytest.fixture(scope='module')
def instance_type(config: dict) -> str:
    """Give value by "instance_type" key.

    :param config: dict from config file.
    :return:       instance_type.
    """
    return config.get('instance_type')


@pytest.fixture(scope='module')
def expected_network_interfaces_number(config: dict) -> int:
    """Give value by "network_interfaces_number" key.

    :param config: dict from config file.
    :return:       network_interfaces_number.
    """
    return config.get('network_interfaces_number')


@pytest.fixture(scope='module')
def expected_network_interface_ip(config: dict) -> str:
    """Give value by "network_interface_ip" key.

    :param config: dict from config file.
    :return:       network_interface_ip.
    """
    return config.get('network_interface_ip')


@pytest.fixture(scope='module')
def expected_network_interface_subnet(config: dict) -> str:
    """Give value by "network_interface_subnet" key.

    :param config: dict from config file.
    :return:       network_interface_subnet.
    """
    return config.get('network_interface_subnet')


@pytest.fixture(scope='module')
def expected_device_size(config: dict) -> int:
    """Give value by "device_size" key.

    :param config: dict from config file.
    :return:       device_size.
    """
    return config.get('device_size')


@pytest.fixture(scope='module')
def expected_root_block_device_type(config: dict) -> str:
    """Give value by "root_block_device_type" key.

    :param config: dict from config file.
    :return:       root_block_device_type.
    """
    return config.get('root_block_device_type')


@pytest.fixture(scope='module')
def expected_instance_ssh_key_name(config: dict) -> str:
    """Give value by "instance_ssh_key_name" key.

    :param config: dict from config file.
    :return:       instance_ssh_key_name.
    """
    return config.get('instance_ssh_key_name')


@pytest.fixture(scope='module')
def expected_instance_tags_count(config: dict) -> int:
    """Give value by "instance_tags_count" key.

    :param config: dict from config file.
    :return:       instance_tags_count.
    """
    return config.get('instance_tags_count')


@pytest.fixture(scope='module')
def expected_instance_tag_name(config: dict) -> str:
    """Give value by "instance_tag_name" key.

    :param config: dict from config file.
    :return:       instance_tag_name.
    """
    return config.get('instance_tag_name')


@pytest.fixture(scope='module')
def expected_availability_zone(config: dict) -> str:
    """Give value by "availability_zone" key.

    :param config: dict from config file.
    :return:       availability_zone.
    """
    return config.get('availability_zone')


@pytest.fixture(scope='module')
def expected_interfaces_id(config: dict) -> str:
    """Give value by "interfaces_id" key.

    :param config: dict from config file.
    :return:       interfaces_id.
    """
    return config.get('interfaces_id')


@pytest.fixture(scope='module')
def expected_tags(config: dict) -> list:
    """Give value by "tags" key.

    :param config: dict from config file.
    :return:       tags.
    """
    return config.get('tags')
