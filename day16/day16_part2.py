RUN_TEST = False
TEST_SOLUTION = 7
# Test cases vary by type. Check https://adventofcode.com/2021/day/16 for
# different test cases and expected outputs.
TEST_INPUT_FILE = "test_input_day_16.txt"
INPUT_FILE = "input_day_16.txt"

ARGS = []

from functools import reduce
from day16_part1 import read_packet_header, parse_literal_packet


def parse_operator_packets(binary_string: str, index: int) -> tuple:
    # Operator packet. Read the next bit as operator length ID type.
    # If operator length ID type is 0 read the next 15 bits as the length.
    # If operator length ID type is 1 read the next 11 bits as the number
    # of sub-packets.
    packet_versions = []
    packet_datas = []
    operator_length_id = binary_string[index]
    if operator_length_id == "0":
        index += 1
        operator_length = int(binary_string[index : index + 15], 2)
        index += 15
        reading_length_index = index
        reading_length_delta = index - reading_length_index
        header_size = 6
        while reading_length_delta < operator_length - header_size:
            parsed_packet_versions, parsed_packet_datas, index = read_packet(
                binary_string, index
            )
            reading_length_delta = index - reading_length_index
            packet_versions.extend(parsed_packet_versions)
            packet_datas.extend(parsed_packet_datas)
    elif operator_length_id == "1":
        index += 1
        operator_length = int(binary_string[index : index + 11], 2)
        index += 11
        for _ in range(operator_length):
            parsed_packet_versions, parsed_packet_datas, index = read_packet(
                binary_string, index
            )
            packet_versions.extend(parsed_packet_versions)
            packet_datas.extend(parsed_packet_datas)
    return packet_versions, packet_datas, index


def preform_operator(operator_type: int, packet_datas: list) -> list:
    if operator_type == 0:
        return [sum(packet_datas)]
    elif operator_type == 1:
        return [reduce(lambda x, y: x * y, packet_datas)]
    elif operator_type == 2:
        return [min(packet_datas)]
    elif operator_type == 3:
        return [max(packet_datas)]
    elif operator_type == 5:
        return [int(packet_datas[0] > packet_datas[1])]
    elif operator_type == 6:
        return [int(packet_datas[0] < packet_datas[1])]
    elif operator_type == 7:
        return [int(packet_datas[0] == packet_datas[1])]
    else:
        raise ValueError(f"Unknown operator type {operator_type}")


def read_packet(binary_string: str, index: int) -> tuple:
    packet_versions = []
    packet_datas = []
    packet_version, packet_type, index = read_packet_header(binary_string, index)
    packet_versions.append(packet_version)
    if packet_type == 4:
        packet_data, index = parse_literal_packet(binary_string, index)
        packet_datas.append(packet_data)
    else:
        parsed_packet_versions, parsed_packet_datas, index = parse_operator_packets(
            binary_string, index
        )
        packet_versions.extend(parsed_packet_versions)
        operated_data = preform_operator(packet_type, parsed_packet_datas)
        packet_datas.extend(operated_data)

    return packet_versions, packet_datas, index


def main_part2(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 16 Part 2 - Packet decoder, with operator handling.
    #
    # Literal values (type ID 4) represent a single number as described above.
    # The remaining type IDs are more interesting:
    #
    # Packets with type ID 0 are sum packets - their value is the sum of the
    # values of their sub-packets. If they only have a single sub-packet, their
    # value is the value of the sub-packet.
    #
    # Packets with type ID 1 are product packets - their value is the result of
    # multiplying together the values of their sub-packets. If they only have a
    # single sub-packet, their value is the value of the sub-packet.
    #
    # Packets with type ID 2 are minimum packets - their value is the minimum
    # of the values of their sub-packets.
    #
    # Packets with type ID 3 are maximum packets - their value is the maximum
    # of the values of their sub-packets.
    #
    # Packets with type ID 5 are greater than packets - their value is 1 if the
    # value of the first sub-packet is greater than the value of the second
    # sub-packet; otherwise, their value is 0. These packets always have
    # exactly two sub-packets.
    #
    # Packets with type ID 6 are less than packets - their value is 1 if the
    # value of the first sub-packet is less than the value of the second
    # sub-packet; otherwise, their value is 0. These packets always have
    # exactly two sub-packets.
    #
    # Packets with type ID 7 are equal to packets - their value is 1 if the
    # value of the first sub-packet is equal to the value of the second
    # sub-packet; otherwise, their value is 0. These packets always have
    # exactly two sub-packets.

    # Parse the input string into a binary number
    binary_string = ""
    for char in lines[0]:
        binary_string += bin(int(char, 16))[2:].zfill(4)

    # Parse the binary string into a list of packets.
    packet_versions = []
    packet_datas = []
    index = 0

    _, parsed_packet_datas, _ = read_packet(binary_string, index)
    packet_datas.extend(parsed_packet_datas)

    solution = packet_datas[0]
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part2(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part2(INPUT_FILE, *ARGS)
        print(solution)
