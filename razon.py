class Razon:
    def RazonesClassic(transacciones):
        motivo = []
        for i in transacciones:
            
            if i['tipo'] == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
                if i['cupoDiarioRestante'] < i['monto']:
                    motivo.append("Excede su cupo diario de retiro de efectivo")
            elif i['monto'] > i['saldoEnCuenta']:
                motivo.append("Error saldo en cuenta negativo, no cuenta con dinero suficiente para retirar")
            elif i['tipo'] == 'TRANSFERENCIA_RECIBIDA': 
                if i['monto'] > 150000:
                    motivo.append("No se ha informado que recibiria este monto")
            elif i['tipo'] == 'TRANSFERENCIA_ENVIADA': # A la transferencia se le aplica una commisión y la transferencia mas la commisión se resta al saldoEnCuenta, si el resultado es menor a 0 es rechazada, entiendo que la transferencia no hace efecto en el cupo diario de extraccion 
                if (i['saldoEnCuenta'] - (i['monto'] + (i['monto']*0.1))) < 0:
                    motivo.append("Saldo insuficiente para la transferencia")
            else:
                motivo.append("Su categoria de cliente no le permite hacer eso")
        return motivo

    def RazonesGold(transacciones):
        motivo = []
        for i in transacciones:
            if i['tipo'] == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
                if i['cupoDiarioRestante'] < i['monto']:
                    motivo.append("Excede su cupo diario de retiro de efectivo")
                elif (i['saldoEnCuenta'] - i['monto']) >= -10000:
                    motivo.append("Error saldo en cuenta negativo, no cuenta con dinero suficiente para retirar")
            elif i['tipo'] == 'ALTA_TARJETA_CREDITO':
                if i['totalTarjetasDeCreditoActualmente'] >= 1:
                    motivo.append("Los clientes Gold solo pueden tener una tarjeta de credito")
            elif i['tipo'] == 'ALTA_CHEQUERA':
                if i['totalChequerasActualmente'] >= 1:
                    motivo.append("Los clientes Gold solo pueden tener una chequera")
            elif i['tipo'] == 'COMPRA_DOLAR':
                if i['saldoEnCuenta'] < i['monto']:
                    motivo.append("Saldo insuficiente para comprar dolares")
            elif i['tipo'] == 'TRANSFERENCIA_ENVIADA': # A la transferencia se le aplica una commisión y la transferencia mas la commisión se resta al saldoEnCuenta, si el resultado llega a ser mayor a -10000 es rechazada, entiendo que la transferencia no hace efecto en el cupo diario de extraccion 
                if (i['saldoEnCuenta'] - (i['monto'] + (i['monto']*0.05))) >= -10000:
                    motivo.append("Saldo insuficiente para la transferencia")
            elif i['tipo'] == 'TRANSFERENCIA_RECIBIDA': 
                if i['monto'] > 500000:
                    motivo.append("No se ha informado que recibiria este monto")
        return motivo

    def RazonesBlack(transacciones):
        motivo = []
        for i in transacciones:
            if i['tipo'] == 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
                if i['cupoDiarioRestante'] < i['monto']:
                    motivo.append("Excede su cupo diario de retiro de efectivo")
                elif (i['saldoEnCuenta'] - i['monto']) >= -10000:
                    motivo.append("Error saldo en cuenta negativo, no cuenta con dinero suficiente para retirar")
            elif i['tipo'] == 'ALTA_TARJETA_CREDITO':
                if i['totalTarjetasDeCreditoActualmente'] >= 5:
                    motivo.append("Los clientes Black solo pueden tener 5 tarjetas de credito")
            elif i['tipo'] == 'ALTA_CHEQUERA':
                if i['totalChequerasActualmente'] >= 2:
                    motivo.append("Los clientes Black solo pueden tener 2 chequeras")
            elif i['tipo'] == 'COMPRA_DOLAR':
                if i['saldoEnCuenta'] < i['monto']:
                    motivo.append("Saldo insuficiente para comprar dolares")
            elif i['tipo'] == 'TRANSFERENCIA_ENVIADA': 
                if (i['saldoEnCuenta'] - i['monto']) >= -10000:
                    motivo.append("Saldo insuficiente para la transferencia")
        return motivo