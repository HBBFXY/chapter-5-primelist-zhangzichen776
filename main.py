def PrimeList(N):
    if N <= 2:
        return ""
    # 初始化筛法列表，is_prime[i]表示i是否为质数
    is_prime = [True] * N
    is_prime[0] = is_prime[1] = False  # 0和1不是质数
    # 埃氏筛核心逻辑：标记非质数
    for current in range(2, int(N ** 0.5) + 1):
        if is_prime[current]:
            # 标记当前数的倍数为非质数（从current*current开始，之前已被更小的数标记）
            for multiple in range(current * current, N, current):
                is_prime[multiple] = False
    # 收集所有质数并转为字符串
    primes = [str(i) for i, prime in enumerate(is_prime) if prime]
    return ' '.join(primes)
