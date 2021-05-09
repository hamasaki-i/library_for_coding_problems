def isPrime(num):
    import math
    i = 2
    while i <= math.sqrt(num):
        if num % i == 0: return False
        i += 1
    return True
        