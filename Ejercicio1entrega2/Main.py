from Class.Persona import Persona

def Registrar(p):
    if(p.comprobarSobrePeso() == -1):
        print(f'{p.getNombre()} tiene peso ideal')
    elif(p.comprobarSobrePeso() == 0):
        print(f'{p.getNombre()} esta por debajo de su peso ideal')
    elif(p.comprobarSobrePeso() == 1):
        print(f'{p.getNombre()} esta en sobrepeso')
    
    if(p.esMayorDeEdad()):
        print(f'{p.getNombre()} es mayor de edad {p.getEdad()}')
    else:
        print(f'{p.getNombre()} es menor de edad {p.getEdad()}')
    
    print(p)

if __name__ == "__main__":
    nombre = input("Ingrese el nombre de la primera persona ")
    edad = int(input("Ingrese la edad de la primera persona "))
    sexo = input("Ingrese el sexo de la primera persona ")
    peso = int(input("Ingrese el peso de la persona "))
    altura = float(input("Ingrese la altura de la persona "))

    p1 = Persona(nombre,edad,sexo,peso,altura)

    Registrar(p1)

    p2 = Persona(nombre,edad,sexo)
    print(p2)
    p2.setPeso(88)
    p2.setAltura(1.80)

    Registrar(p2)

    p3 = Persona()
    p3.setNombre("Ana")
    p3.setEdad(32)
    p3.setSexo('M')
    p3.setPeso(52)
    p3.setAltura(1.60)
    Registrar(p3)
    
     
  

    