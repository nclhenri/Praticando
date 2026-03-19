frase = "Nicolas Henrique"
letra_repetida = ""
quantidade_atual = 0
indice = 0

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
print(f"A letra mais repetida foi '{letra_repetida}', {quantidade_atual} vezes.")