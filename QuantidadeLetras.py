frase = "SAN X COR 15/03/26"

indice = 0
letra_repetida = ""
quantidade_atual = 0

while indice < len(frase):
    letra_atual = frase[indice]

    if letra_atual == " ":
        indice += 1
        continue

    quantidade_total = frase.count(letra_atual)

    if quantidade_atual < quantidade_total:
        quantidade_atual = quantidade_total
        letra_repetida = letra_atual
    indice += 1
print(f"A letra mais repetida é a '{letra_repetida}' com a quantidade de {quantidade_atual} vezes.")