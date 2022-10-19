from math import sqrt
from Card import Card


########################### Metodos Principales #############################

def good_abm(n):
    m = generate_m(n)
    a = 1
    b = 0

    m_primes = generate_prime_array(m)
    m_multiples = find_multiples(m)
    m_primeFactors = [x for x in m_primes if m % x == 0]

    a = generate_a(m_primeFactors)
    b = generate_b(m_primes, n)
    b_multiples = find_multiples(b)

    return a, b, m

# Debe recibir dos arreglos de 5 'cartas' cada uno
# 'carta' puede hacerse en una clase, para almacenar el valor y el palo de cada carta
def compare_hands(player, opponent):
    print()

####################### Metodos Para Texas Hold'em #########################
# Cada jugador posee 7 cartas en total: 2 privadas y 5 publicas
# Cada jugador debe armar la mejor combinacion de 5 cartas, con las 7 que poseen
# Significa que, cada uno de los metodos siguientes asumen SIEMPRE que solo se reciben 5 cartas
# Pues estos metodos se encargan de evaluar cada jugada (la cual consiste de 5)

# Se encarga de generar las 13x4 cartas distintas
def generateAllCards():
    cardDeck = []

    # No se toma en cuenta la carta Joker

    for a in range(1, 14):
        cardDeck.append(Card(a, 0))
        cardDeck.append(Card(a, 1))
        cardDeck.append(Card(a, 2))
        cardDeck.append(Card(a, 3))
    for x in cardDeck:
        print(x)

# Puntaje 9
def isStraightFlush(playerHand):
    return isStraight(playerHand) and isFlush(playerHand)


# Puntaje 8
def isFourOfAKind(playerHand):
    seen = {}

    for x in playerHand:
        if x.value not in seen:
            seen[x.value] = 1
        else:
            seen[x.value] = seen[x.value] + 1

    if len([x for x in seen if seen[x] == 4]) == 1:
        return True
    else:
        return False

# Puntaje 7
def isFullHouse(playerHand):
    seen = {}

    for x in playerHand:
        if x.value not in seen:
            seen[x.value] = 1
        else:
            seen[x.value] = seen[x.value] + 1

    if len([x for x in seen if seen[x] == 3]) == 1 and len([x for x in seen if seen[x] == 2]) == 1:
        return True
    else:
        return False

# Puntaje 6
def isFlush(playerHand):
    whatType = playerHand[0].type

    for x in playerHand:
        if x.type != whatType:
            return False

    return True

# Puntaje 5
def isStraight(playerHand):
    handCopy = []
    result = True

    for x in playerHand:
        handCopy.append(x.value)
    handCopy.sort()

    innerIndex = 0
    if handCopy[3] == 13 and handCopy[4] == 1:
        for i in range(handCopy[0], handCopy[3] + 1):
            if handCopy[innerIndex] != i:
                result = False
                break
            innerIndex = innerIndex + 1
    else:
        for i in range(handCopy[0], handCopy[4] + 1):
            if handCopy[innerIndex] != i:
                result = False
                break
            innerIndex = innerIndex + 1

    return result


# Puntaje 4
def isThreeOfAKind(playerHand):
    seen = {}

    for x in playerHand:
        if x.value not in seen:
            seen[x.value] = 1
        else:
            seen[x.value] = seen[x.value] + 1

    if len([x for x in seen if seen[x] == 3]) == 1 and len([x for x in seen if seen[x] == 1]) == 2:
        return True
    else:
        return False

# Puntaje 3
def isTwoPairs(playerHand):
    seen = {}

    for x in playerHand:
        if x.value not in seen:
            seen[x.value] = 1
        else:
            seen[x.value] = seen[x.value] + 1

    if len([x for x in seen if seen[x] == 2]) == 2:
        return True
    else:
        return False

# Puntaje 2
def isPair(playerHand):
    seen = {}

    for x in playerHand:
        if x.value not in seen:
            seen[x.value] = 1
        else:
            seen[x.value] = seen[x.value] + 1

    if len([x for x in seen if seen[x] == 2]) == 1 and len([x for x in seen if seen[x] == 1]) == 3:
        return True
    else:
        return False

# Puntaje 1
# Devuelve la carta con el valor mas alto
def isHighCard(playerHand):
    maxValue = 0

    for x in playerHand:
        if x.value > maxValue:
            maxValue = x.value
    return maxValue

########################### Metodos Auxiliares #############################

def get_period(a, b, m, x):
    results = {}
    currentSeed = x
    results[currentSeed] = currentSeed

    if isPowerOfTwo(m):
        while True:
            currentSeed = executeGenerator_TwoPowK(a, b, m, currentSeed)
            if currentSeed in results:
                resultsArray = [x for x in results]
                return resultsArray
            results[currentSeed] = currentSeed
    else:
        while True:
            currentSeed = executeGenerator(a, b, m, currentSeed)
            if currentSeed in results:
                resultsArray = [x for x in results]
                return resultsArray
            results[currentSeed] = currentSeed


def executeGenerator(a, b, m, seed):
    return (a * seed + b) % m


def executeGenerator_TwoPowK(a, b, m, seed):
    result = (a * seed + b)
    new_m = m - 1
    return result & new_m


def generate_m(n):
    # Si se desea que M sea potencia de 2
    # m = 16
    #
    # while (m < n * 2):
    #     m = m * 2
    # return m
    return n * 2 + 1


def generate_a(primeFactors):
    a = 1
    for x in primeFactors:
        a = a * x
    return a + 1


def generate_b(primes, m):
    b = 0
    for x in primes:
        if x > (m / 2):
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

    if n < 2:
        isPrime = False
    elif n == 2:
        isPrime = True
    elif not (n & 1):
        isPrime = False
    else:
        root = sqrt(n)

        for i in range(3, int(root) + 1, 2):
            if n % i == 0:
                isPrime = False
                break

    return isPrime


def generate_prime_array(n):
    array = [2]

    for i in range(3, n + 1, 2):
        if isPrime(i):
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

array = [Card(3, 1), Card(3, 1), Card(5, 1), Card(2, 1), Card(1, 1)]
print(isPair(array))
