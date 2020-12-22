def Converter_(num, case):
    """
    num: the number or string to be converted as string type.
    case: 1 for decimal to binary and 0 otherwise
    return: the converted number
    """
    def decimalToBinary(n):
        return bin(n).replace("0b","")

    def binaryToDecimal(n):
        return int(n,2)

    if case == 1:
        conv = decimalToBinary(int(num))
    if case == 0:
        conv = binaryToDecimal(num)
    print(conv)
