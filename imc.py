def calcular_imc(peso, altura):
    """
    Calcula o IMC com base no peso e altura informados.
    """
    return peso / (altura ** 2)

def classificar_imc(imc):
    """
    Classifica o IMC com base nos critérios da OMS.
    """
    if imc < 18.5:
        return "Baixo peso. É recomendado procurar um médico para avaliação criteriosa."
    elif 18.5 <= imc < 25:
        return "Peso adequado. Tudo indica que está tudo bem, mas avalie outros parâmetros corporais."
    elif 25 <= imc < 30:
        return "Sobrepeso. Consulte um médico e reveja hábitos para reverter o quadro."
    elif 30 <= imc < 35:
        return "Obesidade grau I. Busque orientação médica e nutricional."
    elif 35 <= imc < 40:
        return "Obesidade grau II. Não atrase a busca por orientação médica."
    else:
        return "Obesidade grau III. É fundamental buscar orientação médica."

def main():
    """
    Função principal para entrada e saída de dados.
    """
    print("Cálculo de IMC (Índice de Massa Corporal)")
    try:
        peso = float(input("Digite seu peso em kg: "))
        altura = input("Digite sua altura (em metros ou centímetros, ex: 1.75 ou 175): ")
        
        # Converte altura para metros, se necessário
        if "." in altura:
            altura = float(altura)  
        else:
            altura = float(altura) / 100  # Converte de centímetros para metros

        # Verifica se a altura é válida
        if not (1.50 <= altura <= 2.50):
            print("Erro: A altura deve estar entre 1,50 m e 2,50 m.")
            return
        
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        
        print(f"\nSeu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos para peso e altura.")
    except ZeroDivisionError:
        print("Erro: A altura não pode ser zero.")

if __name__ == "__main__":
    main()

