from funciones import *

# Función principal
def main():
    while True:
        print("Bienvenido al programa de cálculo de área, perímetro y volumen.")
        print("1. Triángulo")
        print("2. Cuadrado")
        print("3. Rectángulo")
        print("4. Paralelogramo")
        print("5. Trapecio")
        print("6. Cubo")
        print("7. Círculo")
        print("8. Esfera")
        print("9. Cono")
        print("10. Cilindro")
        print("11. Elipse")
        print("12. Pentágono")
        print("13. Hexágono")
        print("0. Salir")

        opcion = input("Por favor, elige el número correspondiente a la figura geométrica que quieres calcular: ")

        if opcion == "0":
            print("Gracias por utilizar el programa, hasta la p´roxima")
            break

        if opcion == "1":
            base = float(input("Ingrese la longitud de la base del triángulo en cm: "))
            altura = float(input("Ingrese la altura del triángulo en cm: "))
            area = calcular_area_triangulo(base, altura)
            print("El área del triángulo es:", area, "centimetros cuadrados")
            
            lado1 = float(input("Ingrese la longitud del primer lado del triángulo en cm: "))
            lado2 = float(input("Ingrese la longitud del segundo lado del triánguloen cm: "))
            lado3 = float(input("Ingrese la longitud del tercer lado del triángulo en cm: "))
            perimetro = calcular_perimetro_triangulo(lado1, lado2, lado3)
            print("El perímetro del triángulo es:", perimetro, "centimetros")

        elif opcion == "2":
            lado = float(input("Ingrese la longitud de un lado del cuadrado en cm: "))
            area = calcular_area_cuadrado(lado)
            print("El área del cuadrado es:", area, "centimetros cuadrados")
            
            perimetro = calcular_perimetro_cuadrado(lado)
            print("El perímetro del cuadrado es:", perimetro, "centimetros")

        elif opcion == "3":
            base = float(input("Ingrese la longitud de la base del rectángulo en cm: "))
            altura = float(input("Ingrese la altura del rectángulo en cm: "))
            area = calcular_area_rectangulo(base, altura)
            print("El área del rectángulo es:", area, "centimetros cuadrados")
            
            perimetro = calcular_perimetro_rectangulo(base, altura)
            print("El perímetro del rectángulo es:", perimetro, "centimetros")

        elif opcion == "4":
            base = float(input("Ingrese la longitud de la base del paralelogramo en cm: "))
            altura = float(input("Ingrese la altura del paralelogramo en cm: "))
            area = calcular_area_paralelogramo(base, altura)
            print("El área del paralelogramo es:", area, "centimetros cuadrados")
            
            lado1 = float(input("Ingrese la longitud del primer lado del paralelogramo en cm: "))
            lado2 = float(input("Ingrese la longitud del segundo lado del paralelogramo en cm: "))
            perimetro = calcular_perimetro_paralelogramo(lado1, lado2)
            print("El perímetro del paralelogramo es:", perimetro, "centimetros")

        elif opcion == "5":
            base_mayor = float(input("Ingrese la longitud de la base mayor del trapecio en cm: "))
            base_menor = float(input("Ingrese la longitud de la base menor del trapecio en cm: "))
            altura = float(input("Ingrese la altura del trapecio en cm: "))
            area = calcular_area_trapecio(base_mayor, base_menor, altura)
            print("El área del trapecio es:", area, "centimetros cuadrados")
            
            lado1 = float(input("Ingrese la longitud del primer lado del trapecio en cm: "))
            lado2 = float(input("Ingrese la longitud del segundo lado del trapecio en cm: "))
            lado3 = float(input("Ingrese la longitud del tercer lado del trapecio en cm: "))
            lado4 = float(input("Ingrese la longitud del cuarto lado del trapecio en cm: "))
            perimetro = calcular_perimetro_trapecio(lado1, lado2, lado3, lado4)
            print("El perímetro del trapecio es:", perimetro, "centimetros")

        elif opcion == "6":
            lado = float(input("Ingrese la longitud de un lado del cubo en cm: "))
            area = calcular_area_cubo(lado)
            print("El área del cubo es:", area, "centimetros cuadrados")
            
            volumen = calcular_volumen_cubo(lado)
            print("El volumen del cubo es:", volumen, "centimetros cúbicos")
            
            perimetro = calcular_perimetro_cubo(lado)
            print("El perímetro del cubo es:", perimetro, "centímetros")

        elif opcion == "7":
            radio = float(input("Ingrese el radio del círculo en cm: "))
            area = calcular_area_circulo(radio)
            print("El área del círculo es:", area, "centímetros cuadrados")
            
            perimetro = calcular_perimetro_circulo(radio)
            print("El perímetro del círculo es:", perimetro, "centímetros")

        elif opcion == "8":
            radio = float(input("Ingrese el radio de la esfera en cm: "))
            area = calcular_area_esfera(radio)
            print("El área de la esfera es:", area, "centímetros cuadrados")
            
            volumen = calcular_volumen_esfera(radio)
            print("El volumen de la esfera es:", volumen, "centímetros cúbicos")

        elif opcion == "9":
            radio = float(input("Ingrese el radio del cono en cm: "))
            altura = float(input("Ingrese la altura del cono en cm: "))
            area = calcular_area_cono(radio, math.sqrt(radio ** 2 + altura ** 2))
            print("El área del cono es:", area, "centímetros cuadrados")
            
            volumen = calcular_volumen_cono(radio, altura)
            print("El volumen del cono es:", volumen, "centímetros cúbicos")

        elif opcion == "10":
            radio = float(input("Ingrese el radio del cilindro en cm: "))
            altura = float(input("Ingrese la altura del cilindro en cm: "))
            area = calcular_area_cilindro(radio, altura)
            print("El área del cilindro es:", area, "centímetros cuadrados")
            
            volumen = calcular_volumen_cilindro(radio, altura)
            print("El volumen del cilindro es:", volumen, "centímetros cúbicos")

        elif opcion == "11":
            semieje_mayor = float(input("Ingrese el semieje mayor de la elipse en cm: "))
            semieje_menor = float(input("Ingrese el semieje menor de la elipse en cm: "))
            area = calcular_area_elipse(semieje_mayor, semieje_menor)
            print("El área de la elipse es:", area,"centímetros cuadrados")
            
            perimetro = calcular_perimetro_elipse(semieje_mayor, semieje_menor)
            print("El perímetro de la elipse es:", perimetro, "centímetros")

        elif opcion == "12":
            lado = float(input("Ingrese la longitud de un lado del pentágono en cm: "))
            apotema = float(input("Ingrese la longitud del apotema del pentágono en cm: "))
            area = calcular_area_pentagono(lado, apotema)
            print("El área del pentágono es:", area, "centímetros cuadrados")
            
            perimetro = calcular_perimetro_pentagono(lado)
            print("El perímetro del pentágono es:", perimetro, "centímetros")

        elif opcion == "13":
            lado = float(input("Ingrese la longitud de un lado del hexágono en cm: "))
            area = calcular_area_hexagono(lado)
            print("El área del hexágono es:", area, "centímetros cuadrados")
            
            perimetro = calcular_perimetro_hexagono(lado)
            print("El perímetro del hexágono es:", perimetro, "centímetros")

        else:
            print("La opción que eligió no es válida, escoga una de la lista")

        continuar = input("¿Desea calcular otra figura? Responda si o no --> (S/N)? ").strip().lower()
        if continuar != "s" :
            print("¡Gracias por utilizar nuestro programa!")
            break

if __name__ == "__main__":
    main()
