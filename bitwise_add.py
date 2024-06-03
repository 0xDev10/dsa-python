def bitwise_add(a, b):
    while b:
        print('a = ', a, bin(a))
        print('b = ', b, bin(b))
        ans = a ^ b
        carry = (a & b) << 1
        print(int(ans), int(carry))
        print('ans = ',bin(ans))
        print('and = ', bin(a&b))
        print('carry = ',bin(carry))
        print('-'*20)
        a = ans
        b = carry
    return a

a = 11
b = 23
print(bitwise_add(a, b))