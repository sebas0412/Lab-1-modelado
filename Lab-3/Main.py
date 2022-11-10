# Pregunta 8a
# ¿Por qué la probabilidad de formar un nombre parece aumentar conforme n incrementa?
# Porque las secuencias más grandes ya son bloques más grandes y pueden tener incluso palabras
# ya formadas que se usan para construir nuevas palabras, no hay que ir solo por todas las
# combinaciones posibles como podría ser cuando se va letra por letra.




from Markov import Markov

markov = Markov()

# Pregunta 8b
# Semilla 142, con secuencia tamano 1
markov.load_words("pokemon.csv")
model = markov.create_model(markov.wordsArray, 1)
# print(markov.generate_word(model, 142))
print(markov.get_probability(model, "mew"))
##print(transition, sequences)

# Nombre que no tiene sentido
# Semilla 1335, con secuencia tamano 1
markov.load_words("pokemon.csv")
model = markov.create_model(markov.wordsArray, 1)
print(markov.generate_word(model, 1335))
