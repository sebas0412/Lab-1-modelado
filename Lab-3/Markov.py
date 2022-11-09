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
                temp = combined[index : k + index]
                if len(temp) == k:
                    dictionary[temp] = temp
            except:
                print("")

        resultArray = [x for x in dictionary]
        resultArray.sort()
        print("")




    def calculate_transitions(self, words, sequences):
        print("")

    def create_model(self, words, ngrams):
        print("")

    def generate_word(self, model, seed):
        print("")

    def get_probability(self, model, word):
        print("")
