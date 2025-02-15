#CLassificassão de notas por ranking
def classificacao(nota):
    if 90 <= nota <= 100:
        return "Parabéns, você tirou A! "
    elif 80 <= nota <= 89:
        return "Muito bem, você tirou B."
    elif 70 <= nota <= 79:
        return "Bom trabalho, você tirou C."
    elif 60 <= nota <= 69:
        return "Fique atento, você tirou D."
    else:
        return "Estude um pouco mais, você tirou F."

nota = float(input("Informe a nota do aluno: "))

resultado = classificacao(nota)
print(resultado)