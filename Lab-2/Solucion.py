from math import sqrt

def execute(a, b, m, x):
    return get_period(a, b, m, x)


def good_abm(n):
    m = n * 2
    a = 1
    b = 0

    m_primes = generate_prime_array(m)
    m_multiples = find_multiples(m)
    m_primeFactors = [x for x in m_primes if m % x == 0]

    a = generate_a(m_primeFactors)
    b = generate_b(m_primes, m)
    b_multiples = find_multiples(b)

    return a, b, m


def get_period(a, b, m, x):
    results = []
    currentSeed = x
    results.append(currentSeed)

    if(isPowerOfTwo(m)):
        while (True):
            currentSeed = executeGenerator_TwoPowK(a, b, m, currentSeed)
            for x in results:
                if x == currentSeed:
                    loop = False
                    return results
            results.append(currentSeed)
    else:
        while (True):
            currentSeed = executeGenerator(a, b, m, currentSeed)
            for x in results:
                if x == currentSeed:
                    loop = False
                    return results
            results.append(currentSeed)

def executeGenerator(a, b, m, seed):
    return (a * seed + b) % m

def executeGenerator_TwoPowK(a, b, m, seed):
    result = (a * seed + b)
    new_m = m-1
    return result & new_m

def generate_m(n):
    # Si se desea que M sea potencia de 2
    # m = 16
    #
    # while (m < n * 2):
    #     m = m * 2
    # return m

    return n * 2


def generate_a(primeFactors):
    a = 1
    for x in primeFactors:
        a = a * x
    return a + 1


def generate_b(primes, m):
    b = 0
    for x in primes:
        if (x > m / 2):
            b = x
            break
    return b


def find_multiples(n):
    multipleList = []

    for i in range(int(n / 2 + 1)):
        try:
            if n % i == 0:
                multipleList.append(i)
        except:
            continue
    return multipleList


def isPrime(n):
    isPrime = True

    if (n < 2):
        isPrime = False
    elif (n == 2):
        isPrime = True
    elif (n % 2 == 0):
        isPrime = False
    else:
        root = sqrt(n)

        for i in range(3, int(root) + 1, 2):
            if (n % i == 0):
                isPrime = False
                break

    return isPrime


def generate_prime_array(n):
    array = [2]

    for i in range(3, n + 1, 2):
        if (isPrime(i)):
            array.append(i)

    return array


def isPowerOfTwo(n):
    cnt = 0

    while n > 0:
        if n & 1 == 1:
            cnt = cnt + 1
        n = n >> 1

    if cnt == 1:
        return 1
    return 0

print("start")
a, b, m = good_abm(20)
result = execute(a, b, m, 7)
print(result)
print(len(result))
result.sort()
print(result)
print(len(result))
