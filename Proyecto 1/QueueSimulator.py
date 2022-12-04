import math
import numpy as np
from numpy import random

def degenerate(lambd):
    return lambd

#def markovian(lambd):
#    exponential = np.random.exponential(lambd, 15)
#    return exponential

def markovian(lambd):
    x = random.rand()
    exponential = (-(np.log(1-x)))/lambd
    return exponential

def calcularLambda(n: int):
    return 64 - n ** 1.5
def calcularMu(n: int):
    return 5 + 3 * n

class Client:

    horaLlegada : int
    horaAtencion : int
    horaSalida : int

    def __init__(self):
        self.horaAtencion = 0
        self.horaLlegada = 0
        self.horaSalida =0
    def __str__(self):
        return f"Hora de llegada: {self.horaLlegada} Hora de Atencion: {self.horaAtencion} Hora de salida: {self.horaSalida}"

class Server:
    clienteSiendoAtendido : Client
    servidorOcupado : bool
    offtime: float
    serverQueue = []
    def __init__(self, queue):
        self.servidorOcupado = False
        self.offtime = 0
        self.serverQueue = queue
        self.clienteSiendoAtendido = Client()
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
    contadorServidor: int
    clientesGeneradosMaximos: int
    clientesServidos: int
    clientesPerdidos: int
    esperaPromedioCola : float
    esperaPromedioClientes : float
    promedioTiempoOcioso : float
    clientesActualmenteEnSistema : float
    tasaLlegada : float
    tasaSalida : float

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
        self.contadorServidor = 0
        self.clientesGeneradosMaximos = 0
        self.clientesPerdidos = 0
        self.clientesServidos = 0
        self.esperaPromedioClientes = 0.0
        self.esperaPromedioCola = 0.0
        self.promedioTiempoOcioso = 0.0
        self.clientesActualmenteEnSistema = 0.0
        self.tasaLlegada = 0.0
        self.tasaSalida = 0.0
        for i in range(s):
            self.servidores.append(Server(self.queue))

    def simulation(self, time_limit, initial_clients, maximum_arrivals):

        if maximum_arrivals != 0:
            self.clientesGeneradosMaximos = maximum_arrivals
            
        for i in range(initial_clients):
            self.queue.append(Client())
            self.clientesActualmenteEnSistema += 1

        while self.contador < time_limit:

            if self.arrival == "Exponencial":
                tasaLlegada = markovian(calcularLambda(self.clientesActualmenteEnSistema))
            elif self.arrival == "Degenerate":
                tasaLlegada = degenerate(self.lambd)

            if self.arrival == "Exponencial":
                tasaSalida = markovian(calcularMu(self.clientesActualmenteEnSistema))
            elif self.arrival == "Degenerate":
                tasaSalida = degenerate(self.mu)    

            if len(self.queue) < self.lmax:
                self.contador = self.contador + tasaLlegada
                cliente = Client()
                cliente.horaLlegada = self.contador
                self.queue.append(cliente)
                self.clientesActualmenteEnSistema += 1

            else:
                self.clientesPerdidos += 1
                self.contador = self.contador + tasaLlegada

            for servidor in self.servidores:
                if servidor.servidorOcupado == False:
                    if len(self.queue) == 0:
                        servidor.offtime = servidor.offtime + tasaLlegada 
                    else:
                        servidor.cliente = self.queue.pop()
                        servidor.servidorOcupado = True
                        self.clientesServidos += 1
                        servidor.cliente.horaAtencion = self.contador

                        self.esperaPromedioCola = self.esperaPromedioCola + (servidor.cliente.horaAtencion - servidor.cliente.horaLlegada)

                    ##print("No ocupado")
                else: 
                    if tasaSalida > tasaLlegada: 
                            servidor.cliente.horaSalida = self.contador
                            self.esperaPromedioClientes = self.esperaPromedioClientes + (servidor.cliente.horaSalida - servidor.cliente.horaLlegada)
                            servidor.servidorOcupado = False
                            self.clientesActualmenteEnSistema -= 1
                    ##print("Ocupado")

        for servidor in self.servidores:
            self.promedioTiempoOcioso = (self.promedioTiempoOcioso + servidor.offtime)/len(self.servidores)
        
        self.esperaPromedioCola = self.esperaPromedioCola/self.clientesServidos

        return f"Tiempo Transcurrido: {self.contador}, Espera promedio de cola: {self.esperaPromedioCola}, Espera promedio atencion clientes: {self.esperaPromedioClientes}, Clientes perdidos: {self.clientesPerdidos}, Clientes servidos: {self.clientesServidos}, Promedio tiempo ocioso: {self.promedioTiempoOcioso}"

    def agregarClienteALaCola(self):
        print()


simulacion = Queue(15,2,"Exponencial",calcularLambda(0),"Exponencial",calcularMu(0))
print(simulacion.simulation(1000,0,0))