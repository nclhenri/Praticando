frase = "Mc Guimê - Funk Raíz (Funk in House)"

indice = 0
quantidade_atual = 0
letra_repetida = ""

while indice < len(frase):
    letra_atual = frase[indice]

    if letra_atual == " ":
        indice += 1
        continue

    quantidade_repetida = frase.count(letra_atual)

    if quantidade_atual <= quantidade_repetida:
        quantidade_atual = quantidade_repetida
        letra_repetida = letra_atual
    indice += 1
print(f"A quantidade em que a letra '{letra_repetida}' foi repetida é de {quantidade_atual} vezes.")