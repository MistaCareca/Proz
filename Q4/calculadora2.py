def calculadora():
    while True:
        print("\nSelecione a operação desejada:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")
        
        opcao = input("Digite o número da operação: ")
        
        if opcao == "0":
            print("Encerrando o programa. Até mais!")
            break
        elif opcao in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                
                if opcao == "1":
                    resultado = num1 + num2
                    print(f"Resultado da soma: {resultado}")
                elif opcao == "2":
                    resultado = num1 - num2
                    print(f"Resultado da subtração: {resultado}")
                elif opcao == "3":
                    resultado = num1 * num2
                    print(f"Resultado da multiplicação: {resultado}")
                elif opcao == "4":
                    if num2 != 0:
                        resultado = num1 / num2
                        print(f"Resultado da divisão: {resultado}")
                    else:
                        print("Erro: Divisão por zero não é permitida.")
            except ValueError:
                print("Erro: Por favor, insira valores numéricos válidos.")
        else:
            print("Essa opção não existe. Tente novamente.")
