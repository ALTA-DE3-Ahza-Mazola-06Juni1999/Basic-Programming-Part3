def full_prima(N):
    if N < 2:
        return False
    
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return False
    
    if 10 <= N <= 99:
        digit1 = N // 10
        digit2 = N % 10
        if digit1 not in [2, 3, 5, 7] or digit2 not in [2, 3, 5, 7]:
            return False
        if digit1 == 1 or digit2 == 1:
            return False
        if not full_prima(digit1) or not full_prima(digit2):
            return False
    
    return True

if __name__ == '__main__':
    print(full_prima(2))   # True
    print(full_prima(3))   # True
    print(full_prima(11))  # False
    print(full_prima(13))  # False
    print(full_prima(23))  # False
    print(full_prima(29))  # False
    print(full_prima(37))  # True
    print(full_prima(41))  # False
    print(full_prima(43))  # False
    print(full_prima(53))  # False
    print(full_prima(97))  # True