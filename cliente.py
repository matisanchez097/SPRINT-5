from razon import Razon


class Cliente:

    def ClienteClassic(self, transacciones, razones):
        for e in transacciones:
            if e['estado'] == 'RECHAZADA':
                razones = Razon.RazonesClassic(transacciones)
        return(razones)
    
    def ClienteGold(self, transacciones, razones):
        for e in transacciones:
            if e['estado'] == 'RECHAZADA':
                razones = Razon.RazonesGold(transacciones)
        return(razones)

    def ClienteBlack(self, transacciones, razones):
        for e in transacciones:
            if e['estado'] == 'RECHAZADA':
                razones = Razon.RazonesBlack(transacciones)
        return(razones)