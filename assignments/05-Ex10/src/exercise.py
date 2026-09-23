import random

def generar_numero_aleatorio():
    return random.randint(1, 100)

def generar_operador_aritmetico():
    operador = random.randint(1,4)
    if operador == 1:
        return "+"
    elif operador == 2:
        return "-"
    elif operador == 3:
        return "*"
    else:
        return "/"

def generar_ejercicio():
    num1 = generar_numero_aleatorio()
    num2 = generar_numero_aleatorio()

    operador = generar_operador_aritmetico()

    match operador:
        case "+":
            respuesta = int(input(f"{num1} + {num2} = "))
            resultado = num1 + num2
        case "-":
            respuesta = int(input(f"{num1} - {num2} = "))
            resultado = num1 - num2
        case "*":
            respuesta = int(input(f"{num1} * {num2} = "))
            resultado = num1 * num2
        case "/":
            respuesta = float(input(f"{num1} / {num2} = "))
            resultado = num1 / num2

    if respuesta == resultado:
        print("Correcto")
    else:
        print("Incorrecto")

def main():
    generar_ejercicio()
   
if __name__=='__main__':
    main()
