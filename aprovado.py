#Resolução atividade Desafio 1:
def aprovacao(nota):
    if nota >= 6:
        return "Aluno Aprovado."
    else:
        return "Aluno Reprovado."

nota = float(input("Informe a nota do aluno: "))

resultado = aprovacao(nota)
print(f"O aluno está {resultado}")