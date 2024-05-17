## Aqui vai abrir o menu para o usuario escolher a operação
while True:
    print("Selecione a operação desejada:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    operacao = input("Digite a operação desejada (1/2/3/4): ")

    ## Aqui o sistema vai ver se o número digitado é valido
    if operacao in ['1', '2', '3', '4']:
        ## Nessa parte pede pro usuário para informar dois números para efetuar a operação
        numero1 = float(input("Informe o primeiro número: "))
        numero2 = float(input("Informe o segundo número: "))

        ## Aqui o sistema vai fazer a operação escolhida pelo usuario
        if operacao == '1':
            resultado = numero1 + numero2
            print(f"Resultado: {numero1} + {numero2} = {resultado}")

        elif operacao == '2':
            resultado = numero1 - numero2
            print(f"Resultado: {numero1} - {numero2} = {resultado}")

        elif operacao == '3':
            resultado = numero1 * numero2
            print(f"Resultado: {numero1} * {numero2} = {resultado}")
        
        ## Se o usuario tentar fazer uma divisão por 0 o sistema retorna a mensagem de erro abaixo
        elif operacao == '4':
            if numero2 == 0:
                print("Erro! Divisão por zero não é permitida.")
            else:
                resultado = numero1 / numero2
                print(f"Resultado: {numero1} / {numero2} = {resultado}")

    else:
        ## Nessa parte o sistema vai informa pro usuário que a escolha foi inválida
        print("Escolha inválida, por favor tente novamente.")

    ## Aqui o sistema vai pedir se o usuário deseja fazer outra operação
    nova_operacao = input("Deseja realizar outra operação? (s/n): ")
    if nova_operacao.lower() != 's':
        break  ## Aqui o sistema vai sair do loop se o usuário não quiser fazer outra operação