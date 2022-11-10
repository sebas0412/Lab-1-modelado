from Markov import Markov

markov = Markov()
markov.load_words("words.txt")
model = markov.create_model(markov.wordsArray,1)
markov.generate_word(model, 17)
##print(transition, sequences)