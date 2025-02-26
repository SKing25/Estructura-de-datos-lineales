class CuentaBancaria:
    def __init__(self, saldo_inicial: float):
        self._saldo = saldo_inicial # atributo interno

    @property
    def saldo(self) -> float:
        """
        Getter (lectura) para _saldo
        """
        return self._saldo

    @saldo.setter
    def saldo(self, nuevo_saldo: float):
        """
        Setter (escritura) para _saldo
        """
        if nuevo_saldo <= 0:
            raise ValueError('El saldo no puede ser negativo')
        self._saldo = nuevo_saldo

cuenta = CuentaBancaria(1000)
print(cuenta.saldo) # invoca @property -> getter
cuenta.saldo = 500 # invoca @saldo.setter
print(cuenta.saldo) 