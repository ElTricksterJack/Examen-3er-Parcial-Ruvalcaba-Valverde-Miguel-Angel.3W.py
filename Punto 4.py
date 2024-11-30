print("\nRuvalcaba Valverde Miguel Angel_1212_3W")
print("---------------Examen 3-Punto 4---------------")
class Calculadora():#creamos la clase
    def __init__(self, num1, num2):#definimos los atributos
        self._num1=num1
        self._num2=num2
    def cal(self):#hasemos una funcion que muestre todos los resultados de cada operacion
        r=self._num1 + self._num2
        print(f"El resultado de la suma: {self._num1} + {self._num2}= {r}")
        r=self._num1 - self._num2
        print(f"El resultado de la resta: {self._num1} – {self._num2}= {r}")
        r=self._num1 / self._num2
        print(f"El resultado de la divison: {self._num1} / {self._num2}= {r}")
        r=self._num1 * self._num2
        print(f"El resultado de la multiplicación: {self._num1} * {self._num2} = {r}")

print("Ingresaras 2 numeros para + - / y *.")#desir indicasiones y capturar los datos.
n1 = float(input("Ingrese el primer numero: "))
n2 = float(input("Ingrese el segundo numero: "))
op=Calculadora(n1, n2)#invocamos la clase con sus operasiones.
op.cal()
print("-------------------------------------")
