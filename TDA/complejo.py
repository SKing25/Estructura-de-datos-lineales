class complejo:
    """
    TDA para representar numeros complejosde la forma a + bi-
    """
    def __init__(self, real: float, imaginaria: float):
        self.__real = real
        self.__imaginaria = imaginaria

    def sumar(self, otro: 'Complejo') -> 'Complejo':
        nueva_real = self.__real + otro.__real
        nueva_imaginaria = self.__imaginaria + otro.__imaginaria
        return complejo(nueva_real, nueva_imaginaria)

    def restar(self, otro: 'Complejo') -> 'Complejo':
        nueva_real = self.__real - otro.__real
        nueva_imaginaria = self.__imaginaria - otro.__imaginaria
        return complejo(nueva_real, nueva_imaginaria)

    def multiplicar(self, otro: 'Complejo') -> 'Complejo':
        nueva_real = (self.__real * otro.__real) - (self.__imaginaria * otro.__imaginaria)
        nueva_imaginaria = (self.__imaginaria * otro.__imaginaria) + (self.__real * otro.__real)
        return complejo(nueva_real, nueva_imaginaria)

    def get_real(self) -> float:
        return self.__real

    def get_imaginaria(self) -> float:
        return self.__imaginaria

    def __str__(self) -> str:
        return f'{self.__real} + {self.__imaginaria}i'