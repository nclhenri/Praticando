palavra_secreta = "Nicolas"
tentativas = 0
letras_acertadas = ""
print("Teste a sua sorte.")
tentativa = input("Digite uma letra:")

while tentativa != palavra_secreta:

    if len(tentativa) > 1:
        print("Você digitou mais de uma letra!")
        print("Tente novamente.")
        tentativas += 1
        tentativa = input("Digite uma letra:")
        continue
    
    if tentativa in palavra_secreta:
        print("Essa letra TEM na palavra secreta!")
        letras_acertadas += tentativa
        tentativas += 1
    else:
        print("Essa letra NÃO TEM na palavra secreta!")
        tentativas += 1

    palavra_formada = " "

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
    print(f"Palavra gerada: {palavra_formada}")
    tentativa = input("Tente outra letra:")
print(f"PARABÉNS! Você acertou em {tentativas} tentativas.")
print(f"A palavra secreta era: {palavra_secreta}")

    