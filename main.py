def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def PrimeList(N):
    primes = []
    for num in range(2, N):
        if is_prime(num):
            primes.append(str(num))
    return ' '.join(primes)

# 测试用例
# print(PrimeList(10))  # 输出：2 3 5 7
# print(PrimeList(20))  # 输出：2 3 5 7 11 13 17 19
