import csv
import config

class Cliente:
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"({self.dni}) {self.nombre} {self.apellido}"

class Clientes:
    
    lista = []
    with open(config.DATABASE_PATH, newline="\n") as fichero:
        reader = csv.reader(fichero, delimiter=";")
        for dni, nombre, apellido in reader:
            cliente = Cliente(dni, nombre, apellido)
            lista.append(cliente)

    @staticmethod
    def buscar(dni):
        for cliente in Clientes.lista:
            if cliente.dni == dni:
                return cliente

    @staticmethod
    def crear(dni, nombre, apellido):
        nuevo_cliente = Cliente(dni, nombre, apellido)
        Clientes.lista.append(nuevo_cliente)
        Clientes.guardar()
        return nuevo_cliente
    
    @staticmethod
    def modificar(dni, nombre, apellido):
        for i, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                Clientes.lista[i].nombre = nombre
                Clientes.lista[i].apellido = apellido
                Clientes.guardar()
                return Clientes.lista[i]
            
    @staticmethod
    def borrar(dni):
        for i, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                cliente_borrado = Clientes.lista.pop(i)
                Clientes.guardar()
                return cliente_borrado

    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, mode="w", newline="\n") as fichero:
            writer = csv.writer(fichero, delimiter=";")
            for cliente in Clientes.lista:
                writer.writerow((cliente.dni,cliente.nombre,cliente.apellido))