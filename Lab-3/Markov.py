import numpy as np
import random


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

    def add_decorators(self, words, decorator, n):
        decor: str = ""
        decoratedWords = []

        for index in range(n):
            decor += decorator

        for item in words:
            decoratedWords.append(decor + item + decor)

        return decoratedWords

    def get_sequences(self, words, k):
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
                try:
                    for char in range(len(word)):
                        if (word[char:char + sequenceSize] == currentOccurrence):
                            try:
                                currentChar = word[char + 1: char + 1 + sequenceSize]
                                dictionary[self.findDictionaryIndex(currentChar, dictionary)].amount += 1
                            except:
                                continue
                except:
                    continue

            total = 0

            for entry in dictionary:
                total += entry.amount
            if total > 0:
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
        decorators = self.add_decorators(words, "$", 1)
        sequences = self.get_sequences(decorators, ngrams)
        transitions = self.calculate_transitions(decorators, sequences)
        return transitions, sequences

    def generate_word(self, model, seed):
        transitions,sequences = model
        r = random.Random()
        r.seed(seed)
        currentState = 0
        currentIteration = 0
        result = ""
        while True:
            if currentState == 0 and currentIteration > 0:
                break
            currentIteration += 1
            randomNumber = r.random()
            for i in range(len(transitions[currentState])):
                if randomNumber < transitions[currentState][i]:
                    result += sequences[i]
                    currentState = i
                else:
                    randomNumber -= transitions[currentState][i]

        return result

    def get_probability(self, model, word):
        print("")
