import math

def radio_circulo(radio):
    Resultado = radio ** 2 * math.pi
    print(Resultado)

radio = int(input('Escriba el radio de su circunferencia para sacar area: '))
radio_circulo(radio)
