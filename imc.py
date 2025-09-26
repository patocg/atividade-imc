# Programa para calcular o IMC (Índice de Massa Corporal)

# Fórmula de cálculo: IMC = Peso / (Altura * Altura)

# Solicita peso e altura do usuário
peso = float(input("Digite seu peso: ")) # ex: 87.5
altura = float(input("Digite sua altura: ")) # ex: 1.82

# Calculo do IMC
imc = peso / (altura ** 2)

# Mostra o resultado com duas casas decimais
print(f"Seu IMC é: {imc:.2f}")

# Classifica o resultado do IMC
if imc < 18.5:
    print ("Abaixo do Peso")
elif imc < 25:
    print("Peso Normal")
elif imc > 30:
    print("Obesidade")
else:
    print("Sobrepeso")

# Mensagem Final
print("Obrigado por usar este programa de cálculo do IMC!")
