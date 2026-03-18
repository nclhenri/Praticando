palavra_secreta = "SãoPauloTriMundial"
letras_acertadas = ""
tentativas = 0
print("Teste a sua sorte!")
tentativa = input("Digite uma letra:")

while tentativa != palavra_secreta:

    if tentativa in palavra_secreta:
        print("Essa letra TEM na palavra secreta!")
        tentativas += 1
        letras_acertadas += tentativa
    else:
        print("Essa letra NÃO TEM na palavra secreta!")

    palavra_formada = ""

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"

    print(f"Palavra gerada: {palavra_formada}")
    tentativa = input("Digite outra letra:")
    tentativas += 1
print("PARABÉNS!!! Você acertou!")
print(f"A palavra secreta é: {palavra_secreta}")
print(f"Tentativas necessárias: {tentativas}")
    