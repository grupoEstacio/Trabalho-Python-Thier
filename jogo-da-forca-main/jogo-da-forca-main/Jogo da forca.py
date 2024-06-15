def jogo_da_forca():
    # Palavra secreta fixa
    palavra_secreta = "estacio".lower().strip()
    letras_acertadas = ['_'] * len(palavra_secreta)
    tentativas_restantes = 6
    letras_erradas = []

    print("\n" * 50)  # Limpa a tela (para esconder a palavra secreta)

    print("Bem-vindo ao Jogo da Forca!")

    while tentativas_restantes > 0 and '_' in letras_acertadas:
        print("Palavra: ", " ".join(letras_acertadas))
        print(f"Tentativas restantes: {tentativas_restantes}")
        print("Letras erradas: ", " ".join(letras_erradas))

        palpite = input("Adivinhe uma letra: ").lower().strip()

        if palpite in letras_erradas or palpite in letras_acertadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if palpite in palavra_secreta:
            for i, letra in enumerate(palavra_secreta):
                if letra == palpite:
                    letras_acertadas[i] = palpite
        else:
            letras_erradas.append(palpite)
            tentativas_restantes -= 1

    if '_' not in letras_acertadas:
        print("Parabéns! Você adivinhou a palavra:", palavra_secreta)
    else:
        print("Você perdeu! A palavra era:", palavra_secreta)

if __name__ == "__main__":
    jogo_da_forca)
