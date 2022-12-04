import math
import numpy as np
from numpy import random


def degenerate(lambd):
    return lambd


# def markovian(lambd):
#    exponential = np.random.exponential(lambd, 15)
#    return exponential

def markovian(lambd):
    x = random.rand()
    exponential = (-(np.log(1 - x))) / lambd
    return exponential


def calcularLambda(n: int):
    return 64 - n ** 1.5 + 1


def calcularMu(n: int):
    return 5 + 3 * n


class Client:
    horaLlegada: int
    horaAtencion: int
    horaSalida: int

    def __init__(self):
        self.horaAtencion = 0
        self.horaLlegada = 0
        self.horaSalida = 0

    def __str__(self):
        return f"Hora de llegada: {self.horaLlegada} Hora de Atencion: {self.horaAtencion} Hora de salida: {self.horaSalida}"


class Server:
    clienteSiendoAtendido: Client
    servidorOcupado: bool
    offtime: float

    acumuladorServidor: float
    acumuladorClientes: float

    serverQueue = []

    def __init__(self, queue):
        self.servidorOcupado = False
        self.offtime = 0
        self.serverQueue = queue
        self.acumuladorServidor = 0.0
        self.acumuladorClientes = 0.0
        self.clienteSiendoAtendido = Client()

    def __str__(self):
        return f"{self.offtime}"


class Queue:
    lmax: int  # Longitud maxima de la queue
    s: int  # Cantidad de servidores
    arrival: str  # Distribucion tiempo de entrada
    lambd: float  # Tasa de llegada de clientes dado N
    service: str  # Distribucion tiempo de salida
    mu: float  # Tasa de servicio de clientes dado N
    contador: int
    clientesServidos: int
    clientesPerdidos: int
    esperaPromedioCola: float
    esperaPromedioClientes: float
    promedioTiempoOcioso: float
    clientesActualmenteEnSistema: int
    tasaLlegada: float
    tasaSalida: float

    queue = []
    servidores = []

    def __init__(self, lmax, s, arrival, lambd, service, mu):
        self.lmax = lmax
        self.s = s
        self.arrival = arrival
        self.lambd = lambd
        self.mu = mu
        self.service = service
        self.contador = 0
        self.totalClientesGenerados = 0
        self.clientesPerdidos = 0
        self.clientesServidos = 0
        self.esperaPromedioClientes = 0.0
        self.esperaPromedioCola = 0.0
        self.promedioTiempoOcioso = 0.0
        self.clientesActualmenteEnSistema = 0
        self.tasaLlegada = 0.0
        self.tasaSalida = 0.0
        for i in range(s):
            self.servidores.append(Server(self.queue))

    def simulation(self, time_limit, initial_clients, maximum_arrivals):
        unlimited: bool
        contadorLlegada = 0
        contadorSalida = 0
        acumuladorClientes = 0

        if maximum_arrivals == 0:
            unlimited = True
        else:
            unlimited = False

        for i in range(initial_clients):
            cliente = Client()
            cliente.horaLlegada = 0
            self.queue.append(cliente)
            self.clientesActualmenteEnSistema += 1

        while self.contador < time_limit:
            if self.totalClientesGenerados > maximum_arrivals and unlimited == False:
                break

            if self.arrival == "Exponential":
                contadorLlegada += markovian(calcularLambda(self.clientesActualmenteEnSistema))
            else:
                contadorLlegada += degenerate(calcularLambda(self.clientesActualmenteEnSistema))

            for server in self.servidores:
                server.acumuladorClientes += contadorLlegada


            self.totalClientesGenerados += 1
            self.contador += contadorLlegada

            if len(self.queue) > maximum_arrivals:
                self.clientesPerdidos += 1
            else:
                cliente = Client()
                cliente.horaLlegada = self.contador
                self.queue.append(Client())
                self.clientesActualmenteEnSistema += 1

            for servidor in self.servidores:
                # 0.14 Mu
                # 0.18 Lmbda

                if self.service == "Exponential":
                    servidor.acumuladorServidor = markovian(calcularMu(self.clientesActualmenteEnSistema))
                else:
                    servidor.acumuladorServidor = degenerate(calcularMu(self.clientesActualmenteEnSistema))

                if servidor.servidorOcupado == True:
                    if servidor.acumuladorServidor <= servidor.acumuladorClientes:
                        servidor.cliente.horaSalida = self.contador
                        servidor.acumuladorClientes = 0.0
                        acumuladorClientes = 0.0
                        self.esperaPromedioClientes += (servidor.cliente.horaSalida - servidor.cliente.horaAtencion)
                        self.clientesActualmenteEnSistema -= 1
                        servidor.servidorOcupado = False
                else:
                    if len(self.queue) == 0:
                        servidor.offtime += contadorLlegada
                    else:
                        servidor.cliente = self.queue.pop()
                        servidor.servidorOcupado = True
                        self.clientesServidos += 1
                        servidor.cliente.horaAtencion = self.contador
                        self.esperaPromedioCola += (servidor.cliente.horaAtencion - servidor.cliente.horaLlegada)

        for servidor in self.servidores:
            self.promedioTiempoOcioso += servidor.offtime
        self.promedioTiempoOcioso /= 2
        self.esperaPromedioCola /= self.clientesServidos
        self.esperaPromedioClientes /= self.clientesServidos

        return f"\nTiempo Transcurrido: {self.contador}\n" \
               f"Espera promedio de cola: {self.esperaPromedioCola}\n" \
               f"Espera promedio atencion clientes: {self.esperaPromedioClientes}\n" \
               f"Clientes perdidos: {self.clientesPerdidos}\n" \
               f"Clientes servidos: {self.clientesServidos}\n" \
               f"Clientes totales: {self.totalClientesGenerados}\n" \
               f"Promedio tiempo ocioso: {self.promedioTiempoOcioso}\n"

    def agregarClienteALaCola(self):
        print()


simulacion = Queue(15, 1, "Exponential", calcularLambda(0), "Exponential", calcularMu(0))
print(simulacion.simulation(1000, 0, 0))
simulacion = Queue(15, 1, "Degenerate", calcularLambda(0), "Degenerate", calcularMu(0))
print(simulacion.simulation(1000, 0, 0))
