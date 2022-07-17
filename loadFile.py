from cliente import Cliente
import json


cliente = Cliente()

class Parser2:

    def leerDatos(self, filename:str):
        with open(filename) as jsonFile:
            clientes = json.load(jsonFile)

        return (clientes)