
from cliente import Cliente
from creacion_html import CreacionHTML
from loadFile import Parser2

cliente = Cliente()



if __name__ == "__main__":

    razones = ""

    parse = Parser2()
    datos = parse.leerDatos('eventos.json')
    transacciones = datos['transacciones']
    

    if datos['tipo'] == "CLASSIC":
        motivos = cliente.ClienteClassic(transacciones, razones)
    elif datos['tipo'] == "GOLD":
        motivos = cliente.ClienteGold(transacciones, razones)
    elif datos['tipo'] == "BLACK":
        motivos = cliente.ClienteBlack(transacciones, razones)
    
    salida = CreacionHTML()
    salida.crear_html(datos, motivos)