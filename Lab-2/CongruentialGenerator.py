import cgi
from math import sqrt
from Card import Card
import time
import random
import numpy


class CongruentialGenerator:
    a = 0
    b = 0
    m = 0
    generated = []
    ########################### Metodos Principales #############################
    def __init__(self, a, b, m):
        self.a = a
        self.b = b
        self.m = m

        return

    def generateTime(self):
        obj = time.gmtime(0)
        epoch = time.asctime(obj)
        x = round(time.time() * 1000)
        return x

    def seed(self, s):
        random.seed(s)
        return random.random()

    def random(self):
        randomNumber = random.randint(16384,2147483646)
        x = randomNumber & 16383
        x = x/16384
        print(x)
        return x

    def period(self):
        return len(self.generated)

    def good_abm(self, n):
        m = self.generateM(n)
        a = 1
        b = 0
        z = int(m / 3) * 2

        m_primes = self.generate_prime_array(z)
        m_multiples = self.findMultiples(m)
        m_primeFactors = [x for x in m_primes if m % x == 0]

        a = self.generateA(m_primeFactors)
        b = self.generateB(m_primes, n)
        b_multiples = self.findMultiples(b)

        self.a = a
        self.b = b
        self.m = m
        return a, b, m

    def compareHands(self, playerHand, opponentHand):
        playerScore = 0
        opponentScore = 0

        if self.isStraightFlush(playerHand):
            playerScore = 9
        elif self.isFourOfAKind(playerHand):
            playerScore = 8
        elif self.isFullHouse(playerHand):
            playerScore = 7
        elif self.isFlush(playerHand):
            playerScore = 6
        elif self.isStraight(playerHand):
            playerScore = 5
        elif self.isThreeOfAKind(playerHand):
            playerScore = 4
        elif self.isTwoPairs(playerHand):
            playerScore = 3
        elif self.isPair(playerHand):
            playerScore = 2
        elif self.isHighCard(playerHand):
            playerScore = 1

        if self.isStraightFlush(opponentHand):
            opponentScore = 9
        elif self.isFourOfAKind(opponentHand):
            opponentScore = 8
        elif self.isFullHouse(opponentHand):
            opponentScore = 7
        elif self.isFlush(opponentHand):
            opponentScore = 6
        elif self.isStraight(opponentHand):
            opponentScore = 5
        elif self.isThreeOfAKind(opponentHand):
            opponentScore = 4
        elif self.isTwoPairs(opponentHand):
            opponentScore = 3
        elif self.isPair(opponentHand):
            opponentScore = 2
        elif self.isHighCard(opponentHand):
            opponentScore = 1

        if playerScore > opponentScore:
            return "Gana Jugador"
        elif opponentScore > playerScore:
            return "Gana Oponente"
        else:
            player = []
            opponent = []
            playerTotal = 0
            opponentTotal = 0
            for x in playerHand:
                playerTotal = playerTotal + x.value
                player.append(x.value)
            for y in opponentHand:
                opponentTotal = opponentTotal + y.value
                opponent.append(y.value)

            player.sort()
            opponent.sort()

            # Compara la suma de todas las cartas
            if playerTotal > opponentTotal:
                return "Gana Jugador"
            elif opponentTotal > playerTotal:
                return "Gana Oponente"
            else:
                # Compara la carta mayor
                if player[4] > opponent[4]:
                    return "Gana Jugador"
                elif opponent[4] > player[4]:
                    return "Gana Oponente"
                else:
                    return "Empate"


    # Debe recibir dos arreglos de 5 'cartas' cada uno
    # 'carta' puede hacerse en una clase, para almacenar el valor y el palo de cada carta
    def compare_hands(self, player, opponent):
        print()

    ####################### Metodos Para Texas Hold'em #########################
    # Cada jugador posee 7 cartas en total: 2 privadas y 5 publicas
    # Cada jugador debe armar la mejor combinacion de 5 cartas, con las 7 que poseen
    # Significa que, cada uno de los metodos siguientes asumen SIEMPRE que solo se reciben 5 cartas
    # Pues estos metodos se encargan de evaluar cada jugada (la cual consiste de 5)

    # Se encarga de generar las 13x4 cartas distintas
    def generateAllCards(self):
        cardDeck = []

        # No se toma en cuenta la carta Joker

        for a in range(1, 14):
            cardDeck.append(Card(a, 0))
            cardDeck.append(Card(a, 1))
            cardDeck.append(Card(a, 2))
            cardDeck.append(Card(a, 3))
        for x in cardDeck:
            print(x)

        self.shuffleArray(cardDeck)
        return cardDeck

    def shuffleArray(self, array):
        for i in range(0, 10000):
            a = random.randint(0, 51)
            b = random.randint(0, 51)
            temp = array[a]
            array[a] = array[b]
            array[b] = temp

    # Puntaje 9
    def isStraightFlush(self, playerHand):
        return self.isStraight(playerHand) and self.isFlush(playerHand)

    # Puntaje 8
    def isFourOfAKind(self, playerHand):
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
    def isFullHouse(self, playerHand):
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
    def isFlush(self, playerHand):
        whatType = playerHand[0].type

        for x in playerHand:
            if x.type != whatType:
                return False

        return True

    # Puntaje 5
    def isStraight(self, playerHand):
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
    def isThreeOfAKind(self, playerHand):
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
    def isTwoPairs(self, playerHand):
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
    def isPair(self, playerHand):
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
    def isHighCard(self, playerHand):
        maxValue = 0

        for x in playerHand:
            if x.value > maxValue:
                maxValue = x.value
        return maxValue

    ########################### Metodos Auxiliares #############################

    def buildGenerator(self, a, b, m, x):
        results = {}
        currentSeed = x
        results[currentSeed] = currentSeed

        if self.isPowerOfTwo(m):
            while True:
                currentSeed = self.executeGenerator_TwoPowK(a, b, m, currentSeed)
                if currentSeed in results:
                    resultsArray = [x for x in results]
                    self.generated = resultsArray
                    return resultsArray
                results[currentSeed] = currentSeed
        else:
            while True:
                currentSeed = self.executeGenerator(a, b, m, currentSeed)
                if currentSeed in results:
                    resultsArray = [x for x in results]
                    self.generated = resultsArray
                    return resultsArray
                results[currentSeed] = currentSeed

    def executeGenerator(self, a, b, m, seed):
        return (a * seed + b) % m

    def executeGenerator_TwoPowK(self, a, b, m, seed):
        result = (a * seed + b)
        new_m = m - 1
        return result & new_m

    def generateM(self, n):
        # Si se desea que M sea potencia de 2
        # m = 16
        #
        # while (m < n * 2):
        #     m = m * 2
        # return m
        if n & 1:
            return n
        else:
            return n + 1

    def generateA(self, primeFactors):
        a = 1
        for x in primeFactors:
            a = a * x
        return a + 1

    def generateB(self, primes, m):
        b = 0
        for x in primes:
            if x > (m / 2):
                b = x
                break
        return b

    def findMultiples(self, n):
        multipleList = []

        for i in range(int(n / 2 + 1)):
            try:
                if n % i == 0:
                    multipleList.append(i)
            except:
                continue
        return multipleList

    def isPrime(self, n):
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

    def generate_prime_array(self, n):
        array = [2]

        for i in range(3, n + 1, 2):
            if self.isPrime(i):
                array.append(i)

        return array

    def isPowerOfTwo(self, n):
        cnt = 0

        while n > 0:
            if n & 1 == 1:
                cnt = cnt + 1
            n = n >> 1

        if cnt == 1:
            return 1
        return 0
