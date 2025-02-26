class Fraccion:
    def __init__(self, numerador: int, denominador: int):
        # Evitamos acceso directo, usamos __ para sugerir provacidad
        self.__numerador = numerador
        # Validacion temprana
        if denominador == 0:
            raise ValueError('El denominador no puede ser 0')
        self.__denominador = denominador
        self.__simplificar()

    def __simplificar(self):
        # Usa la funcion gcd (maximo comun divisor)
        from math import gcd
        divisor = gcd(self.__numerador, self.__denominador)
        self.__numerador //= divisor
        self.__denominador //= divisor
        # Asegurarnos que el denominador sea positivo
        if self.__denominador < 0:
            self.__denominador = -self.__denominador
            self.__numerador = -self.__numerador

    # Metodos de acceso (getters)
    def get_numerador(self) -> int:
        return self.__numerador

    def get_denominador(self) -> int:
        return self.__denominador

    def __str__(self):
        return f'{self.__numerador} / {self.__denominador}'

