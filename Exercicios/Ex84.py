# Ex84
class Temperatura:
    def __init__(self, celsius=0.0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:  
            raise ValueError("A temperatura em Celsius não pode ser inferior a -273.15°C.")
        self._celsius = value

    def to_fahrenheit(self):
        return (self._celsius * 9/5) + 32

    def to_kelvin(self):
        return self._celsius + 273.15

# Exemplo de uso da classe
temperatura_atual = Temperatura(25.0)

# Lendo a temperatura em Celsius
print(f'Temperatura em Celsius: {temperatura_atual.celsius}°C')

# Convertendo para Fahrenheit
print(f'Temperatura em Fahrenheit: {temperatura_atual.to_fahrenheit()}°F')

# Convertendo para Kelvin
print(f'Temperatura em Kelvin: {temperatura_atual.to_kelvin()}K')

# Ajustando a temperatura em Celsius usando o setter
temperatura_atual.celsius = 30.0
print(f'Temperatura em Celsius ajustada: {temperatura_atual.celsius}°C')
