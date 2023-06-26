# Calcular iva
def calcular_iva(x):
    iva = x * 0.19
    return iva


# Calcular descuento
def calcular_descuento(precio, descuento):
    return precio - (precio * descuento / 100)


# Calcular IMC
def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    return imc


print("Bienvenido a nuestro programa")
print("Ingrese las siguientes opciones que desea operar")
while True:
    try:
        print("-" * 20)
        print("[1] Calcular iva")
        print("[2] Calcular descuento")
        print("[3] Calcular IMC")
        print("[4] Salir del programa")
        print("-" * 30)
        opc = int(input("Ingrese una de las opciones: "))
        if opc == 1:
            while True:
                try:
                    print("*" * 20)
                    print(
                        "Para comenzar con el calculo del iva, necesitamos que ingrese"
                    )
                    print("el precio de un producto")
                    precio_total = int(input("Ingrese el precio del producto: "))
                    iva = calcular_iva(precio_total)
                    precio_iva = iva + precio_total
                    print(f"el valor del iva es de: {iva}")
                    print(f"el valor del precio (con iva incluido) es de: {precio_iva}")
                    break
                except ValueError:
                    print("******ERROR******")
                    print("Ingrese un valor valido")
                    print("*****************")
        elif opc == 2:
            while True:
                try:
                    print(
                        "Para comenzar con el calculo de descuento, se le pedira ingresar dos valores"
                    )
                    precio_original = int(input("Ingrese el precio original: "))
                    ingresar_descuento = int(input("Ingrese un numero del 1 al 100: "))
                    if ingresar_descuento <= 100 and ingresar_descuento >= 1:
                        descuento_total = calcular_descuento(
                            precio_original, ingresar_descuento
                        )
                        print(f"Su descuento es de: {descuento_total}")
                        break
                    else:
                        print("Ingrese un descuento valido")
                except ValueError:
                    print("Ingrese un valor valido")
        elif opc == 3:
            while True:
                print("Esta funcion esta en proceso, intentelo mas tarde")
                break

        elif opc == 4:
            print("******************************************")
            print("*GRACIAS POR UTILIZAR NUESTRO PROGRAMA :)*")
            print("******************************************")
            break
        else:
            print("Ingrese una opcion valida")
    except ValueError:
        print("Ingrese una opcion  valida")
