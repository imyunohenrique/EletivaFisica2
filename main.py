import math

print("Bem vindo a Calculadora Termológica!")
nome = input("Digite seu nome: ")
print("Olá " + nome + "!")
print("Vamos calcular, escolha o tipo de operação: ")
print(" 1. Celsius = Kelvin \n 2. Celsius = Fahrenheit \n 3. Variação de Temperatura \n 4. Dilatação Linear \n 5. Dilatação Volumétrica \n 6. Capacidade Térmica \n 7. Variação de Energia Interna \n 8. Trabalho ")
operacao = int(input("Qual operação você quer, " + nome + ": "))

if operacao == 1:
    a = float(input("Digite a temperatura em Celsius (C°): "))
    kelvin = a + 273
    print("Resposta: ", kelvin, "K")

if operacao == 2:
    a = float(input("Digite a temperatura em Celsius (C°): "))
    fahrenheit = (a * 1.8) + 32
    print("Resposta: ", fahrenheit, "F°")

if operacao == 3:
    t0 = float(input("Digite a temperatura inicial em Celsius (C°): "))
    tf = float(input("Digite a temperatura final em Celsius (C°): "))
    variacaoTemperatura = t0 - tf
    print("Resposta: ", variacaoTemperatura, "C°")

if operacao == 4:
    l0 = float(input("Digite o comprimento inicial em metros (m): "))
    coeficienteLinear