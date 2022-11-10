import numpy as np


class Seq:
    occurrence = ""
    amount = 0

    def __init__(self, occurrence):
        self.occurrence = occurrence
        self.amount = 0


class Markov:
    wordsArray = []

    def __init__(self):
        self.wordsArray = []

    def load_words(self, filename):
        file = open(filename, 'r')

        for line in file:
            for word in line.split():
                if word != ' ' or '\n' or '\t':
                    self.wordsArray.append(word)

    def add_decorators(self, words: str, decorator: str, n: int):
        decor: str = ""
        decoratedWords = []

        for index in range(n):
            decor += decorator

        for item in words:
            decoratedWords.append(decor + item + decor)

        return decoratedWords

    def get_sequences(self, words: str, k):
        combined = ""
        dictionary = {}
        for item in words:
            combined += item

        for index in range(len(combined)):

            try:
                temp = combined[index: k + index]
                if len(temp) == k:
                    dictionary[temp] = temp
            except:
                print("")

        resultArray = [x for x in dictionary]
        resultArray.sort()
        return resultArray

    def calculate_transitions(self, words, sequences):
        matrixSize = len(sequences)
        matrix = np.zeros(shape=(matrixSize, matrixSize))
        sequenceSize = len(sequences[0])
        dictionary = []

        for item in sequences:
            dictionary.append(Seq(item))

        for seq in range(len(dictionary)):
            currentOccurrence = dictionary[seq].occurrence

            for entry in dictionary:
                entry.amount = 0

            for word in words:
                for char in range(len(word)):
                    if (word[char] == currentOccurrence):
                        try:
                            currentChar = word[char + 1: char + 1 + sequenceSize]
                            dictionary[self.findDictionaryIndex(currentChar, dictionary)].amount += 1
                        except:
                            continue

            total = 0

            for entry in dictionary:
                total += entry.amount
            for x in range(len(dictionary)):
                matrix[seq][x] = (1 / total) * dictionary[x].amount

        print("")
        return matrix

    def findDictionaryIndex(self, entry, dictionary):
        counter = 0

        for item in dictionary:
            if item.occurrence == entry:
                break
            counter += 1

        return counter

    def create_model(self, words, ngrams):
        print("")

    def generate_word(self, model, seed):
        print("")

    def get_probability(self, model, word):
        print("")
