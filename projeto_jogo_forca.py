import random
palavras = ["python", "progamacao", "computador", "desenvolvimento", "codigo"]
palavra_secreta = random.choice(palavras)
letras_descobertas = ['_' for letra in palavra_secreta]
letras_tentadas = []
tentativas_restantes = 6

print("Bem-vindo ao jogo da forca!")
print("Você tem", tentativas_restantes, "tentativas para adivinhar a palavra secreta.")
print("Palavra:", " ".join(letras_descobertas))

while tentativas_restantes > 0 and "_" in letras_descobertas:
    print("\nPalavra:", " ".join(letras_descobertas))
    print("Letras tentadas:", ", ".join(letras_tentadas))
    chute = input("Digite uma letra:").lower()

    while len(chute) != 1 or not chute.isalpha():
        print("Por favor, digite apenas uma letra.")
        chute = input("Digite uma letra:").lower()

    if chute in letras_tentadas:
        print("Você já tentou essa letra.Tente outras.")
        continue

    if chute in palavra_secreta:
        print("Você acertou uma letra!")
        for i, letra in enumerate(palavra_secreta):
            if letra == chute:
                letras_descobertas[i] = chute
    else:
            print("Você errou!")
            tentativas_restantes -= 1
            letras_tentadas.append(chute)
            print("Você tem", tentativas_restantes, "tentativas restantes.")

if "_" not in letras_descobertas:
    print("\nParabéns!Você adivinhou a palavra:", palavra_secreta)
else:
    print("\nVocê perdeu!Apalavra secreta era:", palavra_secreta)