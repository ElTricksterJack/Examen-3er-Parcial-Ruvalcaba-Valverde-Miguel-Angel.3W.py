print("\nRuvalcaba Valverde Miguel Angel_1212_3W")
print("---------------Examen 3-Punto 1---------------")
class alumno:#Primero creamos la funcion
    def __init__(self, name, cal, mat):#aqui definimos los atributos (hasi como dise usted profe =) pero prefiero llamarlos objetos poer ahora seran atributos.)
        self.name = name #definimos que los atributos son parte del self
        self.cal = cal 
        self.mat = mat
    def moscal(self):#despues definimos una funcion que captura dichos datos y a su bes los muestra en pantalla (Nota: el nombre significa MOStrar CALificasion.)
        self.name = input("Ingrese el nombre del alumno: ")#capturamos los datos
        self.mat = input("Ingrese el materia: ")
        self.cal = float(input("Ingresa la calificacion de dicha materia: "))
        print("-♠-♦-♠-♦-♠-♦-♠-♦-♠-♦-♠-♦-")#No hay que perder la estetica ☻
        print(f"Alumno: {self.name}\nMateria: {self.mat}\ncalificacion de la materia: {self.cal}")#y los mostramos.
e = alumno("","",0)#ahora como no se invocar funciones sin un valor definido creamos esta variable, que rellenamos temporal mente los espacioes en blanco.
e.moscal()#y ya la podemos invocar, ahora es fucional
print("-------------------------------------")
