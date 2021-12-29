RUN_TEST = False
TEST_SOLUTION = 16
# Test cases vary by type. Check https://adventofcode.com/2021/day/16 for
# different test cases and expected outputs.
TEST_INPUT_FILE = "test_input_day_16.txt"
INPUT_FILE = "input_day_16.txt"

ARGS = []


def read_packet_header(binary_string: str, index: int) -> tuple:
    packet_version = int(binary_string[index : index + 3], 2)
    index += 3
    packet_type = int(binary_string[index : index + 3], 2)
    index += 3
    return packet_version, packet_type, index


def parse_literal_packet(binary_string: str, index: int) -> int:
    # Literal packet. Read every 5 bits, until the first bit is 0.
    # Parse the last 4 bits as a number and add it to the list.
    packets = ""
    next_bit_group = binary_string[index : index + 5]
    while next_bit_group[0] == "1":
        number = next_bit_group[1:]
        packets += str(number)
        index += 5
        next_bit_group = binary_string[index : index + 5]
    number = next_bit_group[1:]
    packets += str(number)
    index += 5
    return int(packets, 2), index


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
        packet_datas.extend(parsed_packet_datas)

    return packet_versions, packet_datas, index


def main_part1(
    input_file,
):
    with open(input_file) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))

    # Day 16 Part 1. Packet decoder. Input is a hex string. Convert to binary,
    # then read the bits based on the following rules:
    #
    # Every packet begins with a standard header: the first three bits encode
    # the packet version, and the next three bits encode the packet type ID.
    # These two values are numbers; all numbers encoded in any packet are
    # represented as binary with the most significant bit first. For example, a
    # version encoded as the binary sequence 100 represents the number 4.
    #
    # Packets with type ID 4 represent a literal value. Literal value packets
    # encode a single binary number. To do this, the binary number is padded
    # with leading zeroes until its length is a multiple of four bits, and then
    # it is broken into groups of four bits. Each group is prefixed by a 1 bit
    # except the last group, which is prefixed by a 0 bit. These groups of five
    # bits immediately follow the packet header.
    #
    # Every other type of packet (any packet with a type ID other than 4)
    # represent an operator that performs some calculation on one or more
    # sub-packets contained within.
    #
    # An operator packet contains one or more packets. To indicate which
    # subsequent binary data represents its sub-packets, an operator packet can
    # use one of two modes indicated by the bit immediately after the packet
    # header; this is called the length type ID:
    #
    # If the length type ID is 0, then the next 15 bits are a number that
    # represents the total length in bits of the sub-packets contained by this
    # packet.
    #
    # If the length type ID is 1, then the next 11 bits are a number that
    # represents the number of sub-packets immediately contained by this
    # packet.
    #
    # Finally, after the length type ID bit and the 15-bit or 11-bit field, the
    # sub-packets appear.
    #
    # Decode the structure of your hexadecimal-encoded BITS transmission; what
    # do you get if you add up the version numbers in all packets?

    # Parse the input string into a binary number
    binary_string = ""
    for char in lines[0]:
        binary_string += bin(int(char, 16))[2:].zfill(4)

    # Alternately convert it into a bit stream so that we can parse actual bits
    # instead of string segments
    # https://pypi.org/project/bitstream/
    # bit_stream = BitStream(bin=binary_string)

    # Parse the binary string into a list of packets.
    packets = ""
    packet_versions = []
    packet_types = []
    packet_datas = []
    index = 0

    parsed_packet_versions, parsed_packet_datas, index = read_packet(
        binary_string, index
    )
    packet_versions.extend(parsed_packet_versions)
    packet_datas.extend(parsed_packet_datas)  # Throwaway for now

    solution = sum(packet_versions)
    return solution


if __name__ == "__main__":
    if RUN_TEST:
        solution = main_part1(TEST_INPUT_FILE, *ARGS)
        print(solution)
        assert TEST_SOLUTION == solution
    else:
        solution = main_part1(INPUT_FILE, *ARGS)
        print(solution)
