def calc_pow(self, x: float, n: int) -> float:
    if n < 0:
        return 1/calc_pow(x, -n)
    elif n == 0:
        return 1
    elif n == 1:
        return x
    else:
        half_pow = calc_pow(x, n//2)
        if n%2 == 0:
            return half_pow * half_pow
        else:
            return half_pow *  half_pow * x