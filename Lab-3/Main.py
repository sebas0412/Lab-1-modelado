from Markov import Markov

markov = Markov()
markov.load_words("words.txt")
transition, sequences = markov.create_model(markov.wordsArray,1)
print(transition, sequences)