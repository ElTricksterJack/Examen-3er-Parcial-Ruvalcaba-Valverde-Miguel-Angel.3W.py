print("\nRuvalcaba Valverde Miguel Angel_1212_3W")
print("---------------Examen 3-Punto 3---------------")
class tri:#Primero creamos la funcion
    def __init__(self, l1, l2, l3):#aqui definimos los atributos
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
    def mostri(self):#despues definimos una funcion que captura dichos datos y a su bes los muestra en pantalla
        print("-Ingresaras la longitud de cada lado de un triangulo-")
        self.l1 = float(input("Ingresa la longitud del lado 1: "))#capturamos datos
        self.l2 = float(input("Ingresa la longitud del lado 2: "))
        self.l3 = float(input("Ingresa la longitud del lado 3: "))
        if self.l1 == self.l2 and self.l2 == self.l3:#ahora con un if definimos la primera condicion, que sus lados sean iguales para que sea equilatero
            print(f"Lado 1: {self.l1}\nLado 2: {self.l2}\nLado 3: {self.l3}\nEl triangulo es equilatero")
        elif self.l1 == self.l2 or self.l2 == self.l3 or self.l1 == self.l3:#con el elif que solo 2 de sus lados sean iguales
            print(f"Lado 1: {self.l1}\nLado 2: {self.l2}\nLado 3: {self.l3}\nEl triangulo es isosceles")
        else:#y con este por descarte que ninguno sea igaul es escaleno
            print(f"Lado 1: {self.l1}\nLado 2: {self.l2}\nLado 3: {self.l3}\nEl triangulo es escaleno")
e = tri(0,0,0)#ahora como no se invocar funciones sin un valor definido creamos esta variable.
e.mostri()#y ya la podemos invocar, ahora es fucional
print("-------------------------------------")
