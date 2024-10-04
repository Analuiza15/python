def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Erro: Divisão por zero não é permitida."
    
def resto_divisao(num1, num2):
    return num1 % num2

def exibir_menu():                                      
    print("CALCULADORA DAS OPERAÇÕES BÁSICAS \n")
    print("Menu de escolha:\n")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Resto da Divisão")
    print("6. Sair")
    return int(input("\nDigite uma opção: "))
def obter_valores():
    num1 = float(input("\nDigite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))
    return num1, num2

def main():
    while True:
        opcao = exibir_menu()

        if opcao == 1:
            print("Você escolheu Soma.")
            num1, num2 = obter_valores()
            resultado = soma(num1, num2)
            print(f"A soma dos números é: {resultado}\n")

        elif opcao == 2:
            print("Você escolheu Subtração.")
            num1, num2 = obter_valores()
            resultado = subtracao(num1, num2)
            print(f"A subtração dos números é: {resultado}\n")

        elif opcao == 3:
            print("Você escolheu Multiplicação.")
            num1, num2 = obter_valores()
            resultado = multiplicacao(num1, num2)
            print(f"A multiplicação dos números é: {resultado}\n")

        elif opcao == 4:
            print("Você escolheu Divisão.")
            num1, num2 = obter_valores()
            resultado = divisao(num1, num2)
            print(f"A divisão dos números é: {resultado}\n")

        elif opcao == 5:
            print("Você escolheu Resto da Divisão.")
            num1, num2 = obter_valores()
            resultado = resto_divisao(num1, num2)
            print(f"O resto da divisão é: {resultado}\n")

        elif opcao == 6:
            print("Saindo...\n")
            break

        else:
            print("Opção Inválida\n")
if __name__ == "__main__":
   main()