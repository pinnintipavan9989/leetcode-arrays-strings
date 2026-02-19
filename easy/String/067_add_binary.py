
def addBinary(a, b):
    p1, p2 = len(a) - 1, len(b) - 1
    carry = 0
    result = []

    while p1 >= 0 or p2 >= 0 or carry:
        digit1 = int(a[p1]) if p1 >= 0 else 0
        digit2 = int(b[p2]) if p2 >= 0 else 0

        total = digit1 + digit2 + carry
        result.append(str(total % 2))
        carry = total // 2

        p1 -= 1
        p2 -= 1

    return "".join(reversed(result))