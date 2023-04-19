
print("Calculadora-1.0!!")
# Criando as variaveis
sair = False

while sair == False:
    num1 = int(input("Digite o primeiro número: "))
    operador = input("Digite o operador desejado: (+,-,/ ou *) ")
    num2 = int(input("Digite o segundo número: "))
    # Testando as condicionais

    # Soma
    if operador == "+":
        print("O resultado da soma é: ", num1 + num2)

    # Subtração
    if operador == "-":
        print("O resultado da subtração é: ", num1 - num2)

    # Divisão
    if operador == "/":
        print("O resultado da divisão é: ", num1 / num2)

    # Multiplicação
    if operador == "*":
        print("O resultado da multiplicação é: ", num1 * num2)

    teste = input("Deseja sair ? (s/n)")
    if teste == "s":
        sair = True
        print("Tchau!!!")
