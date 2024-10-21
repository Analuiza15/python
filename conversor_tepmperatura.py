def exibirMenu():
    print("****Conversor de Temperatura****")
    print("1. Converter de Celsius para Fahrenheit")
    print("2. Converter de Celsius para Kelvin")
    print("3. Converter de Fahrenheit para Celsius")
    print("4. Converter de Fahrenheit para Kelvin")
    print("5. Converter de Kelvin para Celsius")
    print("6. Converter de Kelvin para Fahrenheit")
    print("7. Sair")

    select = int(input("O que você quer converter? "))
    return select

def celsius_farenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def celsius_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def fahrenhiet_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def fahhrenhiet_kelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5/9 + 273.
    return kelvin

def kelvin_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def kelvin_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return fahrenheit


while True:
    select = exibirMenu()

    if select == 1:
        print ("- Selecionando opção 1 - \n")
        celsius = float(input("Digite a temperatura em Celsius: "))
        print(f"A temperatura é: {celsius_farenheit(celsius)}° F\n")

    elif select == 2:
        print ("- Selecionando opção 2 - \n")
        celsius = float(input("Digite a temperatura em Celsius: "))
        print(f"A temperatura é: {celsius_kelvin(celsius)} K\n")

    elif select == 3:
        print ("- Selecionando opção 3 - \n")
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        print(f"A temperatura é: {fahrenhiet_celsius(fahrenheit)}° C\n")

    elif select == 4:
        print ("- Selecionando opção 4 - \n")
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        print(f"A temperatura é: {fahhrenhiet_kelvin(fahrenheit)} K\n")

    elif select == 5:
        print ("- Selecionando opção 5 - \n")
        kelvin = float(input("Digite a temperatura em Kelvin: "))
        print(f"A temperatura é: {kelvin_celsius(kelvin)}° C\n")
        
    elif select == 6:
        print ("- Selecionando opção 6 - \n")
        kelvin = float(input("Digite a temperatura em Kelvin: "))
        print(f"A temperatura é: {kelvin_fahrenheit(kelvin)}° F\n")

    elif select == 7:
        print("Obrigado por usar o programa!")
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")