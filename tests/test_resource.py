import logging


def test_init(aws_instance, expected_instance_id):
    logging.info('Test init')
    actual_result = aws_instance.instance_ids
    assert actual_result == expected_instance_id, \
        f"Actual result {actual_result} is not equal to " \
        f"expected result {expected_instance_id}."


def test_private_ip(aws_instance, expected_network_interface_ip):
    logging.info('Test private_ip')
    actual_result = aws_instance.private_ip
    assert actual_result == expected_network_interface_ip,        \
        f"Actual result {actual_result} is not equal to " \
        f"expected result {expected_network_interface_ip}."


def test_ssh_key_name(aws_instance, expected_instance_ssh_key_name):
    logging.info('Test ssh_key_name')
    actual_result = aws_instance.ssh_key_name
    assert actual_result == expected_instance_ssh_key_name,        \
        f"Actual result {actual_result} is not equal to " \
        f"expected result {expected_instance_ssh_key_name}."


def test_subnet_id(aws_instance, expected_network_interface_subnet):
    logging.info('Test subnet_id')
    actual_result = aws_instance.subnet_id
    assert actual_result == expected_network_interface_subnet,        \
        f"Actual result {actual_result} is not equal to " \
        f"expected result {expected_network_interface_subnet}."


def test_instance_type(aws_instance, instance_type):
    logging.info('Test instance_type')
    actual_result = aws_instance.instance_type
    assert actual_result == instance_type,        \
        f"Actual result {actual_result} is not equal to " \
        f"expected result {instance_type}."


def test_availability_zone(aws_instance, expected_availability_zone):
    logging.info('Test availability_zone')
    actual_result = aws_instance.availability_zone
    assert actual_result == expected_availability_zone,        \
        f"Actual result {actual_result} is not equal to " \
        f"expected result {expected_availability_zone}."


def test_network_interfaces_number(aws_instance, expected_network_interfaces_number):
    logging.info('Test network_interfaces_number')
    actual_result = len(aws_instance.network)
    assert actual_result == expected_network_interfaces_number,        \
        f"Actual result {actual_result} is not equal to " \
        f"expected result {expected_network_interfaces_number}."


def test_interfaces_id(aws_instance, expected_interfaces_id):
    logging.info('Test interfaces_id')
    actual_result = aws_instance.interfaces_id
    assert actual_result == expected_interfaces_id,        \
        f"Actual result {actual_result} is not equal to " \
        f"expected result {expected_interfaces_id}."


def test_device_type(aws_instance, expected_root_block_device_type):
    logging.info('Test device_type')
    actual_result = aws_instance.device_type
    assert actual_result == expected_root_block_device_type,        \
        f"Actual result {actual_result} is not equal to " \
        f"expected result {expected_root_block_device_type}."


def test_tags_count(aws_instance, expected_instance_tags_count):
    logging.info('Test ags_count')
    actual_result = len(aws_instance.tags)
    assert actual_result == expected_instance_tags_count,        \
        f"Actual result {actual_result} is not equal to " \
        f"expected result {expected_instance_tags_count}."


def test_block_device_size(aws_instance, expected_device_size):
    logging.info('Test block_device_size')
    actual_result = aws_instance.size
    assert actual_result == expected_device_size,        \
        f"Actual result {actual_result} is not equal to " \
        f"expected result {expected_device_size}."


def test_state(aws_instance, expected_state):
    logging.info('Test state')
    actual_result = aws_instance.state.get('Name')
    assert actual_result == expected_state,        \
        f"Actual result {actual_result} is not equal to " \
        f"expected result {expected_state}."


def test_tags(expected_tags, aws_instance):
    logging.info('Test tags')
    actual_result = [tag.get('Value') for tag in aws_instance.tags]
    expected_result = list(expected_tags.values())
    assert actual_result == expected_result, \
        f"Actual result {actual_result} is not equal to " \
        f"expected result {expected_result}."
