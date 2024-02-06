def potencia():
    comprobar=True
    while(comprobar):
        try:
            a=float(input("Inserte la base: "))
            b=float(input("Inserte el exponente: "))
            comprobar=False
        except:
            print("Inserte un valor válido")

    pot=a**b
    print("El resultado es: ", pot)


def raz():
    comprobar=True
    while(comprobar):
        try:
            a=float(input("Inserte el valor a sacar raíz cuadrada: "))
            comprobar=False
        except:
            print("Inserte un valor válido")

    raiz=a**0.5
    print("El resultado es: ", raiz)


def resta():
    comprobar=True
    while(comprobar):
        try:
            a=float(input("Inserte el primer valor a restar: "))
            b=float(input("Inserte el segundo valor a restar: "))
            comprobar=False
        except:
            print("Inserte un valor válido")

    diferencia=a-b
    print("La respuesta es: ", diferencia)


def dividir():
    comprobar=True
    while(comprobar):
        try:
            a=float(input("Inserte el numerador: "))
            b=float(input("Inserte el denominador "))
            comprobar=False
        except:
            print("Inserte un valor válido")

    if(b==0):
        print("No es posible dividir entre cero, su valor es indetederminado")
    else:
        div=a/b
        print("La respuesta es: ", div)


def suma():
    comprobar=True
    while(comprobar):
        try:
            print("¿Cuántos valores desea sumar?")
            x=int(input("Respuesta: "))
            comprobar=False
        except:
            print("Inserte un valor válido")

    lista_valores=[]

    for x in range (0,x,1):
        comprobar2=True
        while(comprobar2):
            try:
                b=float(input("Digite un valor: "))
                comprobar2=False
            except:
                print("Ingrese un valor válido")
        lista_valores.append(b)
    total=sum(lista_valores)
    print("El resultado es: ",total)


def multiplicar():
    comprobar=True
    while(comprobar):
        try:
            print("¿Cuántos valores desea multiplicar?")
            x=int(input("Respuesta: "))
            comprobar=False
        except:
            print("Inserte un valor válido")

    lista_valores=[]

    for x in range (0,x,1):
        comprobar2=True
        while(comprobar2):
            try:
                b=float(input("Digite un valor: "))
                lista_valores.append(b)
                comprobar2=False
            except:
                print("Ingrese un valor válido")

    total=1

    for numero in lista_valores:
        total = total * numero
    print("El resultado es: ", total)

def bucle_operaciones():
    ciclo_operaciones=True
    pregunta_repetir=True
    while(ciclo_operaciones):
        menu_operaciones2()
        comprobar1=True
        while(comprobar1):
            try:
                respuesta1=int(input("Seleccione una operación del menú: "))
                comprobar1=False
            except:
                print("Inserte un valor válido")
        if(respuesta1==1):
            suma()
            ciclo_operaciones=False
        elif(respuesta1==2):
            resta()
            ciclo_operaciones=False
        elif(respuesta1==3):
            multiplicar()
            ciclo_operaciones=False
        elif(respuesta1==4):
            dividir()
            ciclo_operaciones=False
        elif(respuesta1==5):
            potencia()
            ciclo_operaciones=False
        elif(respuesta1==6):
            raz()
            ciclo_operaciones=False
        else:
            print("Inserte un valor válido")


def menu_operaciones2():
    print("MENÚ OPERACIONES")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicación")
    print("4) División")
    print("5) Potenciación")
    print("6) Raíz cuadrada")

def repetir_operaciones():
    print("¿Desea realizar otra operación?")
    print("1) Sí, por favor")
    print("2) No, chao")


# M A I N 👋

print("Bienvenido a nuestra calculadora")
print("Esperamos que te ayude en tus cálculos")

ciclo_operaciones=True
pregunta_repetir=True

while(ciclo_operaciones):
    print("MENÚ OPERACIONES")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicación")
    print("4) División")
    print("5) Potenciación")
    print("6) Raíz cuadrada")
    print("7) Salir")
    comprobar1=True
    while(comprobar1):
        try:
            respuesta1=int(input("Seleccione una operación del menú: "))
            comprobar1=False
        except:
            print("Inserte un valor válido")
    if(respuesta1==1):
        suma()
        ciclo_operaciones=False
    elif(respuesta1==2):
        resta()
        ciclo_operaciones=False
    elif(respuesta1==3):
        multiplicar()
        ciclo_operaciones=False
    elif(respuesta1==4):
        dividir()
        ciclo_operaciones=False
    elif(respuesta1==5):
        potencia()
        ciclo_operaciones=False
    elif(respuesta1==6):
        raz()
        ciclo_operaciones=False
    elif(respuesta1==7):
        print("Cuídate")
        ciclo_operaciones=False
        pregunta_repetir=False
    else:
        print("Inserte un valor válido")

while(pregunta_repetir):
    
    comprobar3=True
    while(comprobar3):
        repetir_operaciones()
        try:
            respuesta2=int(input("Respuesta: "))
            comprobar3=False
        except:
            print("Inserte un valor válido")

    if(respuesta2==1):
        bucle_operaciones()
    elif(respuesta2==2):
        print("Vale, cuídate")
        pregunta_repetir=False
    else:
        print("Inserte un valor válido")
        
        


        
