from math import gcd

class Fraccion:
    """
    TDA para representar fracciones a/b
    """
    def __init__(self, numerador: int, denominador: int):
        if denominador == 0:
            raise ValueError('El denominador no puede ser cero')
        self.__numerador = numerador
        self.__denominador = denominador
        self.simplificar()

    def simplificar(self):
        # Calculamos el gcd y dividimos numerador y denominador
        divisor = gcd(self.__numerador, self.__denominador)
        self.__numerador //= divisor
        self.__denominador //= divisor
        # Aseguramos que el denominador sea positivo
        if self.__denominador < 0:
            self.__denominador = -self.__denominador
            self.__numerador = -self.__numerador

    def sumar(self, otra: 'Fraccion') -> 'Fraccion':
        nuevo_num = (self.__numerador * otra.__denominador) + (otra.__denominador * self.__numerador)
        nuevo_den = self.__denominador * otra.__denominador
        return Fraccion(nuevo_num, nuevo_den)

    def restar(self, otra: 'Fraccion') -> 'Fraccion':
        nuevo_num = (self.__numerador * otra.__denominador) - (otra.__numerador * self.__denominador)
        nuevo_den = self.__denominador * otra.__denominador
        return Fraccion(nuevo_num, nuevo_den)

    def multiplicar(self, otra: 'Fraccion') -> 'Fraccion':
        nuevo_num = self.__numerador * otra.__numerador
        nuevo_den = self.__denominador * otra.__denominador
        return Fraccion(nuevo_num, nuevo_den)

    def dividir(self, otra: 'Fraccion') -> 'Fraccion':
        nuevo_num = self.__numerador * otra.__denominador
        nuevo_den = self.__denominador * otra.__numerador
        return Fraccion(nuevo_num, nuevo_den)

    def comparar(self, otra: 'Fraccion') -> int:
        """
        Retorna:
        0 si son iguales
        positivo si self > otra
        negativo si self < otra
        """
        return (self.__numerador * otra.__denominador) - (otra.__numerador * self.__denominador)

    def get_numerador(self) -> int:
        return self.__numerador

    def get_denominador(self) -> int:
        return self.__denominador

    def __str__(self) -> str:
        return f'{self.__numerador} / {self.__denominador}'

f1 = Fraccion(2,3)
f2 = Fraccion(12,6)

suma = f1.sumar(f2)
resta = f1.restar(f2)
mult = f1.multiplicar(f2)
div = f1.dividir(f2)

print(suma)
print(resta)
print(mult)
print(div)