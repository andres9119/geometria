import math

def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

def calcular_perimetro_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3

def calcular_area_cuadrado(lado):
    return lado * lado

def calcular_perimetro_cuadrado(lado):
    return 4 * lado

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_perimetro_rectangulo(base, altura):
    return 2 * (base + altura)

def calcular_area_paralelogramo(base, altura):
    return base * altura

def calcular_perimetro_paralelogramo(lado1, lado2):
    return 2 * (lado1 + lado2)

def calcular_area_trapecio(base_mayor, base_menor, altura):
    return 0.5 * (base_mayor + base_menor) * altura

def calcular_perimetro_trapecio(lado1, lado2, lado3, lado4):
    return lado1 + lado2 + lado3 + lado4

def calcular_volumen_cubo(lado):
    return lado ** 3

def calcular_area_cubo(lado):
    return 6 * lado ** 2

def calcular_perimetro_cubo(lado):
    return 12 * lado

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

def calcular_volumen_esfera(radio):
    return (4/3) * math.pi * radio ** 3

def calcular_area_esfera(radio):
    return 4 * math.pi * radio ** 2

def calcular_volumen_cono(radio, altura):
    return (1/3) * math.pi * radio ** 2 * altura

def calcular_area_cono(radio, generatriz):
    return math.pi * radio * (radio + generatriz)

def calcular_volumen_cilindro(radio, altura):
    return math.pi * radio ** 2 * altura

def calcular_area_cilindro(radio, altura):
    return 2 * math.pi * radio * (radio + altura)

def calcular_area_elipse(semieje_mayor, semieje_menor):
    return math.pi * semieje_mayor * semieje_menor

def calcular_perimetro_elipse(semieje_mayor, semieje_menor):
    a = semieje_mayor
    b = semieje_menor
    return math.pi * (3 * (a + b) - math.sqrt((3 * a + b) * (a + 3 * b)))

def calcular_perimetro_pentagono(lado):
    return 5 * lado

def calcular_area_pentagono(lado, apotema):
    return (5 * lado * apotema) / 2

def calcular_perimetro_hexagono(lado):
    return 6 * lado

def calcular_area_hexagono(lado):
    return (3 * math.sqrt(3) * lado ** 2) / 2