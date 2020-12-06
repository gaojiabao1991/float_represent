def int_decimal_to_binary(decimal):
    if decimal == 0: return 0

    bits = []

    while decimal != 0:
        mod = decimal % 2
        bits.append(mod)
        decimal = int(decimal / 2)

    bits.reverse()
    bits = [str(bit) for bit in bits]
    binary = ''.join(bits)
    return int(binary)


def float_decimal_to_binary(decimal):
    if decimal == 0: return 0

    binary = 0
    bit = 1
    while decimal != 0:
        bit_value = 1 / pow(2, bit)
        if decimal >= bit_value:
            binary += 1 / pow(10, bit)
            decimal -= bit_value

        bit += 1

    return binary


def decimal_to_binary(x):
    int_part = int(x)
    float_part = x - int_part

    binary_int_part = int_decimal_to_binary(int_part)
    binary_float_part = float_decimal_to_binary(float_part)

    return binary_int_part + binary_float_part


def int_binary_to_decimal(binary):
    if binary == 0: return 0
    decimal = 0
    bit = 0
    while binary != 0:
        mod = binary % 10
        decimal += mod * pow(2, bit)
        binary = int(binary / 10)
        bit += 1

    return decimal


def float_binary_to_decimal(binary: str):
    if binary == '0': return 0

    decimal = 0
    for bit in range(len(binary)):
        if binary[bit] == '1':
            decimal += 1 / pow(2, bit + 1)

    return decimal


def binary_to_decimal(binary: str):
    if binary == '0': return 0

    # int_part = int(binary)
    # float_part = binary - int_part

    int_part = int(binary[:binary.find('.')])
    float_part_str = binary[binary.find('.') + 1:]

    decimal_int_part = int_binary_to_decimal(int_part)
    decimal_float_part = float_binary_to_decimal(float_part_str)

    return decimal_int_part + decimal_float_part


# 二进制的表达必须用字符串传, 因为对于0.1等数值, python的10进制系统无法精确保存, 直接值就变了.
m = {
    '0.001': 0.125,
    '0.11': 0.75,
    '1.1001': 1.5625,
    '10.1011': 2.6875,
    '1.001': 1.125,
    '101.111': 5.875,
    '11.0011': 3.1875,
}

for k, v in m.items():
    decimal = binary_to_decimal(k)
    binary = decimal_to_binary(v)

    print('%s : %s' % (binary, decimal))
