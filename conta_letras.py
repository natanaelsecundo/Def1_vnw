def contar_letras(nome):
    return f"O nome {nome} tem {len(nome)} letras"

nome = input("Informe um  nome: ")

resultado = contar_letras(nome)
print(resultado)
