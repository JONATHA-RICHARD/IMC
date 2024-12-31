def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        return f"IMC: {imc:.2f} - Baixo peso"
    elif 18.5 <= imc < 25:
        return f"IMC: {imc:.2f} - Peso adequado"
    elif 25 <= imc < 30:
        return f"IMC: {imc:.2f} - Sobrepeso"
    elif 30 <= imc < 35:
        return f"IMC: {imc:.2f} - Obesidade grau I"
    elif 35 <= imc < 40:
        return f"IMC: {imc:.2f} - Obesidade grau II"
    else:
        return f"IMC: {imc:.2f} - Obesidade grau III"

if __name__ == "__main__":
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    print(calcular_imc(peso, altura))
