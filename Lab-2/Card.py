class Card:
    # Type indica el tipo de 'palo' de la carta
    # Type = 0 Corazones
    # Type = 1 Rombos
    # Type = 2 Picas
    # Type = 3 Treboles

    # Value es un valor numerico entero que debe incluir de 1 a 13

    value = 0
    type = 0

    def __init__(self, value, type):
        self.value = value
        self.type = type

    def __str__(self):
        typeStr = ""
        valueStr = ""

        if self.type == 0:
            typeStr = "Corazones"
        elif self.type == 1:
            typeStr = "Rombos"
        elif self.type == 2:
            typeStr = "Picas"
        elif self.type == 3:
            typeStr = "Treboles"
        else:
            typeStr = "NA"

        if self.value == 1:
            valueStr = "A"
        elif self.value == 11:
            valueStr = "J"
        elif self.value == 12:
            valueStr = "Q"
        elif self.value == 13:
            valueStr = "K"
        else:
            valueStr = str(self.value)
        return f"{valueStr}, {typeStr}"
