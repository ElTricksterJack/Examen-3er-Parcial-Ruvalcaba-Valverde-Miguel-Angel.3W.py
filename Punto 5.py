print("\nRuvalcaba Valverde Miguel Angel_1212_3W")
print("---------------Examen 3-Punto 5---------------")
class agenda():
    def __init__(self):
        self.con = []#solo nesitaremos esta lista, al prinsipio pense en utilisar un dicionario pero es mas fasil añadir elementos a listas
        #Extra nota: al prinsipio la abia dejado como 0 pero me acorde que se podia dejar vacia la lista
    def ac(self):#Primero haemos esta funcion
        name = input("Ingrese el nombre: ")#capturamos y creamos datos
        te = input("Ingrese telefono: ")
        co = input("Ingrese el correo electronico: ")
        self.con.append({"nombre": name, "telefono": te, "correo": co})#imprimimos el mensaje y lo agregamos a la lista
    def lis(self):
        print("-•-Lista de contactos-•-") #estetica señores
        for c in self.con: #ahora imprimimos todos los elementos de la lista, con el sigiente patron de abajo, no es el mejor pero es efectivo.
            print(f"-♠-Contacto-♠-\nNombre: {c['nombre']}\nTelefono: {c['telefono']}\nCorreo: {c['correo']}\n")
    def busc(self):
        n = input("Buscar: ")#capturar dato
        for c in self.con:#iniciar bulce
            if c["nombre"].lower() == n.lower():#aqui buscamos el contacto
                print(f"-♠-Contacto-♠-\nNombre: {c['nombre']}\nTelefono: {c['telefono']}\nCorreo: {c['correo']}\n")#y aqui lo mostrarlo
                return#a esto es pára que no se repita
            else:
                print("no esta dicho contacto.")#mensaje de unexistecia
    def edit(self):
        n = input("Contacto que se editar: ")
        for c in self.con:#hasemos el mismo proses, pero capturando nuevos valores
            if c["nombre"].lower() == n.lower():
                newname = input("Ingrese el nuevo nombre: ")
                newtel = input("Ingrese el nuevo telefono: ")
                newco = input("Ingrese el nuevo correo: ")
                if newname:#ahora este if y elses alladimos los nuevos datos
                    c["nombre"] = newname
                elif newtel:
                    c["telefono"] = newtel
                elif newco:
                    c["corre"] = newco
                print(f"Contacto {n} editado.")
                return# lo mismo que el otro return
        else:#esto es por si no tienes contactos y esta solito, Im sorry fo you
            print("No hay se encotro dicho contacto.")
    def menu(self):
        et = 1
        while et > 0:#iniciamos otro bucle, al igual que undead unluck
            print("\n--- Menu de Agenda ---")
            print("1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")
            opc = int(input("eliga porfavor: "))#Nota: este lugar fue el mas estresante porque solo era un int, pero no pense que el error era el white, pero qui cauramos la variable
            match opc:#abrimos un match con el valor dado
                case 1:#y en cada case le damos la opcion de abrir cada funcion
                    self.ac()
                case 2:
                    self.lis()
                case 3:
                    self.busc()
                case 4:
                    self.edit()
                case 5:
                    ("Gracias por usar este programa chaito.")#y aqui sales
                    et = 0
                case _:
                    print("Opción no valida, mira vien la pantalla o eres ciego.")#Muahahahahaha ☻
ea = agenda()
ea.menu()#solo hasemos la invocasion y ya
print("-------------------------------------")
#adios siiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii
