print("\nRuvalcaba Valverde Miguel Angel_1212_3W")
print("---------------Examen 3-Punto 2---------------")
class persona:#Primero creamos la clase
    def __init__(self, name, ed):#aqui definimos los atributos
        self.name = name #definimos que los atributos son parte del self
        self.ed = ed
    def moscal(self):#despues definimos una funcion que captura dichos datos y a su bes los muestra en pantalla
        self.name = input("Ingrese el nombre del la persona: ")#capturamos los datos
        self.ed = int(input("Ingrese la edad de la persona: "))
        print("-♥-♣-♥-♣-♥-♣-♥-♣-♥-♣-")
        if self.ed >= 18:#abrimos un if para ver si es mayor de 18
            print(f"veras {self.name} eres mayor de edad, Im sorry for you")#si es el caso se muestra el mensaje
        elif self.ed >= 90:#un detalle mio
            print(f"veras {self.name} hay 2 opcines o me estas mintiendo o tienes un pie entre la muerte y la vida")
        else:#despues si eres mayor de edad se puestra el respectivo mensaje, grasias al else
            print(f"{self.name} eres menor de edad")
e = persona("",0)#definido creamos esta variable, que rellenamos temporal mente los espacioes en blanco.
e.moscal()#y ya la podemos invocar, ahora es fucional
print("-------------------------------------")
