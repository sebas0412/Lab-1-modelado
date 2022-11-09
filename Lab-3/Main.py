from Markov import Markov

m = Markov()
m.load_words("words.txt")
print(m.get_sequences("$$hello$$$$world$$", 2))
