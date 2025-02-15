#Resolução atividade Desafio 1:
def elegibilidade(idade):
    if idade >= 16:
        return "Você está apto a votar."
    else:
        return "Você não está apto a Votar."

idade = float(input("Informe a sua idade: "))

resultado = elegibilidade(idade)
print(resultado)