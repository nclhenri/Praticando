frase = "Nintendo Music"
indice = 0
quantidade_atual = 0
letra_repetida = ""

while indice < len(frase):
    letra_atual = frase[indice]

    if letra_atual == " ":
        indice += 1
        continue

    quantidade_total = frase.count(letra_atual)

    if quantidade_atual <= quantidade_total:
        quantidade_atual = quantidade_total
        letra_repetida = letra_atual
    indice += 1
print(f"A letra em que mais se repete é '{letra_repetida}', {quantidade_atual} vezes")