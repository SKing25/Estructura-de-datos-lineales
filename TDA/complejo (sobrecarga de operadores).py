class Complejo:
    def __init__(self, real: float, imaginaria: float):
        self._real = real
        self._imag = imaginaria

    @property
    def real(self) -> float:
        return self._real

    @real.setter
    def real(self, nuevo_valor: float):
        # Aqui podriamos validar o realizar alguna logica
        self._real = nuevo_valor

    @property
    def imag(self) -> float:
        return self._imag

    @imag.setter
    def imag(self, nuevo_valor: float):
        self._imag = nuevo_valor

    #Metodos especiales para sobrecarga de operadores:
    def __add__(self, other: 'Complejo') -> 'Complejo':
        """
        Sobrecarga del operador +
        """
        nueva_real = self._real + other._real
        nuevo_imag = self._imag + other._imag
        return Complejo(nueva_real, nuevo_imag)

    def __sub__(self, other: 'Complejo') -> 'Complejo':
        """
        Sobrecarga del operador -
        """
        nueva_real = self._real - other._real
        nuevo_imag = self._imag - other._imag
        return Complejo(nueva_real, nuevo_imag)

    def __mul__(self, other: 'Complejo') -> 'Complejo':
        """
        Sobrecarga del operador *
        """
        nueva_real = (self._real * other._real) - (self._imag * other._imag)
        nueva_imag = (self._imag * other._real) + (self._real * other._imag)
        return Complejo(nueva_real, nueva_imag)

    def __repr__(self) -> str:
        """
        Representacion interna (por ejemplo, en el interprete)
        """
        return f'Complejo({self.__real}, {self.__imag})'

    def __str__(self) -> str:
        """
        Representacion en string (por ejemplo, al hacer print())
        """
        return f'{self._real} + {self._imag}i'

c1 = Complejo(2, 3) # 2 + 3i
c2 = Complejo(1, 4) # 1 + 4i

suma = c1 + c2  # Internamente llama c1.__add__(c2)
resta = c1 - c2 # ci.__sub__(c2)
mult = c1 * c2  # c1.__mul__(c2)

print(suma)     # 3 + 7i
print(resta)    # 1 - 1i
print(mult)     # (2*1 - 3*4) + (2*4, 3*1)i = -10 + 11i
