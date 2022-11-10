from Markov import Markov

markov = Markov()
markov.load_words("words.txt")
print(markov.get_sequences("$$hello$$$$world$$", 2))
markov.calculate_transitions(markov.wordsArray,markov.get_sequences("$$hello$$$$world$$", 1))
