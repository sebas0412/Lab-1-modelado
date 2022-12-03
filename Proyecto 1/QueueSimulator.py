
import numpy as np

print("Hello world")


class Client:
    def __init__(self,horaLlegada,horaAtencion,horaSalida):
        self.horaLlegada = horaLlegada
        self.horaAtencion = horaAtencion
        self.horaSalida = horaSalida
    def __str__(self):
        return f"Hora de llegada: {self.horaLlegada} Hora de Atencion: {self.horaAtencion} Hora de salida: {self.horaSalida}"


class Server:
    def __init__(self,clienteActual, offtime):
        self.clienteActual = clienteActual
        self.offtime = offtime
    def __str__(self):
        return f"{self.offtime}"


def degenerate(lambd):
    return lambd

def markovian(lambd):
    exponential = np.random.exponential(lambd, 1)
    return exponential

print(markovian(0.864))
cliente1 = Client(2,7,7)
print(Server(cliente1, 822))