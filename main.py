import mariadb

# Conectando ao banco

conexao = mariadb.connect(
    user="root",
    password="vortex5422",
    host="localhost",
    port=3306,
    database="projetofisica2"
)

# Criar cursor

sql = conexao.cursor()

# Calculadora

print("Bem vindo a Calculadora Termológica!")
nome = input("Digite seu nome: ")
turma = input("Digite sua turma: ")
print("Olá " + nome + "!")
print("Vamos calcular, escolha o tipo de operação: ")
print(" 1. Celsius = Kelvin \n 2. Celsius = Fahrenheit \n 3. Variação de Temperatura \n 4. Dilatação Linear \n 5. Dilatação Superficial \n 6. Capacidade Térmica \n 7. Variação de Energia Interna \n 8. Trabalho ")
operacao = int(input("Qual operação você quer, " + nome + ": "))

# Kelvin

if operacao == 1:
    a = float(input("Digite a temperatura em Celsius (C°): "))
    kelvin = a + 273
    print("Resposta: ", kelvin, "K")

# Fahrenheit

if operacao == 2:
    a = float(input("Digite a temperatura em Celsius (C°): "))
    fahrenheit = (a * 1.8) + 32
    print("Resposta: ", fahrenheit, "F°")

# Variação de Temperatura ∆T

if operacao == 3:
    t0 = float(input("Digite a temperatura inicial em Celsius (C°): "))
    tf = float(input("Digite a temperatura final em Celsius (C°): "))
    variacaoTemperatura = t0 - tf
    print("Resposta: ", variacaoTemperatura, "C°")

# Dilatação Linear ∆L = L0 . α . ∆T

if operacao == 4:
    print("Fórmula: ∆L = L0 . α . ∆T")
    l0 = float(input("Digite o comprimento inicial em metros (m): "))
    coeficienteLinear = float(input("Digite o coeficiente de dilatação linear:" ))
    t0 = float(input("Digite a temperatura inicial em Celsius (C°): "))
    tf = float(input("Digite a temperatura final em Celsius (C°): "))
    variacaoTemperatura = t0 - tf
    dilatacaoLinear = l0 * coeficienteLinear * variacaoTemperatura
    print("Resposta: ", dilatacaoLinear, ". 10⁻⁶")

# Dilatação Superficial ∆A = A0 . β . ∆T

if operacao == 5:
    print("Fórmula: ∆A = A0 . β . ∆T")
    l0 = float(input("Digite a área inicial em metros (m²): "))
    coeficienteSuperficial = float(input("Digite o coeficiente de dilatação superficial: (C°⁻¹)" ))
    t0 = float(input("Digite a temperatura inicial em Celsius (C°): "))
    tf = float(input("Digite a temperatura final em Celsius (C°): "))
    variacaoTemperatura = t0 - tf
    dilatacaoSuperficial = l0 * coeficienteSuperficial * variacaoTemperatura
    print("Resposta: ", dilatacaoSuperficial, ". 10⁻⁶")

# Capacidade térmica C = m . c

if operacao == 6:
    print("Fórmula: C = m . c")
    massa = float(input("Digite a massa em gramas (g): "))
    calorEspecifico = float(input("Digite o calor específico em calorias:"))
    capacidadeTermica = massa * calorEspecifico
    print("Resposta:", capacidadeTermica, "cal")

# Variação de Energia Interna ∆U = Q - T

if operacao == 7:
    print("Fórmula: ∆U = Q - T")
    quantidadeCalor = int(input("Digite a quantidade de calor em J (Joule): "))
    trabalho = int(input("Digite o trabalho exercido em J (Joule): "))
    variacaoEnergiaInterna = quantidadeCalor - trabalho
    print("Resposta: ", variacaoEnergiaInterna, "J")

# Trabalho T = Qq - Qf

if operacao == 8: 
    print("Fórmula: T = Qq - Qf")
    quantidadeCalorAbsorvida = int(input("Digite a quantidade de calor absorvida da fonte quente (J): "))
    quantidadeCalorCedida = int(input("Digite a quantidade de calor cedida a fonte fria (J): "))
    t = quantidadeCalorAbsorvida - quantidadeCalorCedida
    print("Resposta: ", t, "J")

print("Obrigado por acessar a calculadora!" + nome)
print("Espero que tenha gostado!")

notas = int(input("Poderia nos avaliar de 0 a 10? "))

# Cadastrando Dados

try:
    sql.execute("INSERT INTO AVALIACAO (nome, turma, notas) VALUES (?,?, ?)", (nome, turma, notas))
    conexao.commit()
    print("Obrigado pela nota!")
except:
    print("Erro na inserção de Dados")

# Fechando a conexão

conexao.close()

