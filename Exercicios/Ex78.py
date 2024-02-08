# Ex78

class Circulo:

    def __init__(self, raio):
        self.__raio = raio
        self.__pi = 3.14159


    def get_raio(self):
        return f'O raio do circulo é {self.__raio}'


    def set_raio(self, raio):
        print('O valor do raio foi modificado {raio}')
        self.__raio = raio

    def calcular_area(self):
        return f'A area do circulo é : {self.__pi * self.__raio ** 2}'

