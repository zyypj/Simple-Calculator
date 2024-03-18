import math

def calcular():
    exibir_menu()
    operacao = input("Digite o número da operação desejada: ")
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro número: "))

    if operacao == '1':
        resultado = soma(num1, num2)
    elif operacao == '2':
        resultado = subtracao(num1, num2)
    elif operacao == '3':
        resultado = multiplicacao(num1, num2)
    elif operacao == '4':
        resultado = divisao(num1, num2)
    else:
        print("Operação não encontrada!")
        return

    print("O resultado é:", resultado)

def exibir_menu():
    print("Operações disponíveis:")
    print("")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    return a / b

# Chamada da função calcular fora dela, para que seja executada após sua definição
calcular()
