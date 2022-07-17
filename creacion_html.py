from cliente import Cliente
from loadFile import Parser2


cliente = Cliente()


class CreacionHTML:
    
    def __init__(self) -> None:
        pass

    def crear_html(self, datos, motivos):
        transacciones = ""
        a = 0
        for e in datos["transacciones"]:
            motivo = ""
            if e["estado"] == "RECHAZADA":
                motivo = motivos[a]
                a += 1
            transacciones += "<tr><td>{fecha}</td><td>{tipo}</td><td>{estado}</td><td>{monto}</td><td>{motivo2}</td></tr>".format(
                fecha = e["fecha"],
                tipo = e["tipo"],
                estado = e["estado"],
                monto = e["monto"],
                motivo2 = motivo
                )  
            

        html_template = """
            <html>
                <head>       
                    <meta charset="utf-8">
                    <title>Tabla</title>
                </head>
                <body>
                    <h1>{apellido}, {nombre}</h1>
                    <h3>Nro Cliente: {numero}<h3>
                    <h3>DNI: {dni}<h3>
                    <h4>Direccion: {direccion}<h4>
                    <h4>{ciudad}<h4>
                    <table border="2px">
                        <tr>
                            <th>Fecha</th>
                            <th>Tipo</th>
                            <th>Estado</th>
                            <th>Monto</th>
                            <th>Razon</th>
                        </tr>
                        {transacciones2}
                        <tr>
                            <td></td>
                            <td></td>            
                            <td></td>
                            <td></td>
                            <td></td>            
                        </tr>
                    </table>
                </body>
            </html>
        """.format(
                numero = datos["numero"],
                nombre = datos["nombre"],
                apellido = datos["apellido"],
                dni = datos["dni"],
                direccion = datos["direccion"]["calle"] + " " + datos["direccion"]["numero"],
                ciudad = datos["direccion"]["pais"] + ", " + datos["direccion"]["provincia"] + ", " + datos["direccion"]["ciudad"],
                transacciones2 = transacciones
                )

        archivo = open("index.html", "w")
        archivo.write(html_template)
        archivo.close()