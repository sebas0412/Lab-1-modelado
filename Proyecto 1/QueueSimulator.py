import math
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

class Queue:
    lmax: int           #Longitud maxima de la queue
    s: int              #Cantidad de servidores
    arrival: str        #Distribucion tiempo de entrada
    lambd: float        #Tasa de llegada de clientes dado N
    service: str        #Distribucion tiempo de salida
    mu: float           #Tasa de servicio de clientes dado N
    contador: int

    def __init__(self, lmax, s, arrival, lambd, service, mu):
        self.lmax = lmax
        self.s = s
        self.arrival = arrival
        self.lambd = lambd
        self.service = service
        self.mu = mu
        self.contador = 0

    def simulation(self, time_limit, initial_clients, maximum_arrivals):

        print()

        #Imprimir total de clientes servidos
        #Imprimir total de clientes perdidos (llegaron y la cola estaba llena)
        #Tiempo de espera promedio de la cola (Qw)
        #Tiempo de servicio Promedio (Lw)
        #Tiempo primedio ocioso   p = lambda/mu, 1-p
    def calcularLambda(self, n: int):
        return 64 - n ** 1.5

    def calcularMu(self, n: int):
        return 5 + 3 * n

    def incrementarContador(self):
        self.contador += 1
        self.agregarClienteALaCola()
    def agregarClienteALaCola(self):
        print()

def degenerate(lambd):
    return lambd

def markovian(lambd):
    exponential = np.random.exponential(lambd, 1)
    return exponential

print(markovian(0.864))
cliente1 = Client(2,7,7)
print(Server(cliente1, 822))