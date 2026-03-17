palavra_secreta = "badbunny"
tentativas = 0
letras_acertadas = ""
print("Teste a sua sorte!")
tentativa = input("Digite uma letra:")

while tentativa != palavra_secreta:

    if len(tentativa) > 1:
        print("Você digitou mais de uma letra. Tente novamente:")
        tentativa = input("")
        tentativas += 1
        continue

    if tentativa in palavra_secreta:
        print(f"A letra {tentativa} TEM na palavra secreta!")
        letras_acertadas += tentativa
    else:
        print(f"A letra {tentativa} NÃO TEM na palavra secreta!")

    palavra_formada = ""

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
    
    tentativas += 1
    print(f"Palavra gerada: {palavra_formada}")
    tentativa = input("Digite outra letra:")
print(f"PARABÉNS! Você acertou a palavra secreta. Em {tentativas} tentativas!")
print(f"A palavra secreta era: {palavra_secreta}")