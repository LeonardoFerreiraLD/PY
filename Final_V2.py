# esse código tem como função ser uma calculdora
print("****Calculadora**** \n")

opcao = False  # declaramos uma váriavel para criar um laço de repetição infinita com o while
while opcao == False:  # aqui usamos o while para criar o laço de repetição

    primeiro_numero = int(input("Digite o primeiro número: "))
    operacao = input(
        "Digite qual a operação que deseja realizar ( +(adição), -(subtração) , *(multiplicação) ou /(divisão)): ")
    # como em uma calculadora, digitamos o primeiro número que queremos trabalhar e escolhemos a operação númerica que será realizada

    # depois de escolher a operação, escolhemos o segundo número para continuação da conta
    segundo_numero = int(input("Digite o segundo número: "))

    resultado = 0  # criação da variavel resultado

    if operacao == '+':  # depois de declarar os números que iremos trabalhar e a operação que será realizada, o programa cria variaveis para cada operação e executa a conta
        resultado = primeiro_numero + segundo_numero
        label = "soma"
    elif operacao == '-':
        resultado = primeiro_numero - segundo_numero
        label = "subtracao"
    elif operacao == '*':
        resultado = primeiro_numero * segundo_numero
        label = "multiplicação"
    elif operacao == '/':
        resultado = primeiro_numero / segundo_numero
        label = "divisão"
        # A operação de adição, subtração, multiplicação ou divisão, serão executadas para depois imprimir o resultado com a devida concatenação
    else:
        # caso a operação der erro como em uma calculadora normal, o programa apresentará na tela "Operação Inválida" e o código se encerrará
        print("Operação Inválida!")
        exit()

    # Aqui acontecera a concatenção e exibira para o usuario, qual operação foi realizada com a ajuda da váriavel label, os números selecionados para execução da conta, o operador escolido: +, -, *  ou / e o resultado da conta
    print("A ", label, "de " + str(primeiro_numero) + ' ' + operacao +
          ' ' + str(segundo_numero) + ' é = ' + str(resultado))
    # Depois de realizar a conta, o usuario poderá escolher se, deseja continuar com mais operações ou deseja encerrar os calculas aqui, caso digite não(N), isso acabara com a execução do código e do laço infinito do while
    continuar = input(" Deseja continuar? sim(S) / não (N)? ")

    # Caso o usuario digite não(N), o programa vai se encerrar  com a mensagem "Obrigado e volte sempre!!!"
    if continuar == "N":
        opcao = True
        # Se caso deseja continuar e digitar sim(S), o programa continuara normalmente voltando para escolha dos numeros, escolha de operação e o programa todo irá repetir novamente até o usuario digitar não(N) no comando de deseja continuar.
        print("Obrigada e volte sempre!!!")
