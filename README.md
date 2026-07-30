# jogodaforca
print("******************************")
print("bem vindo ao jogo da forca")
print("******************************")

palavrasecreta = "forte"
palavrasacertadas = ["_","_","_","_","_","_"]

enforcou = false
acertou = false

While(not enforcou and not acertou):
    chute = input("digite uma letra?")
    chute = chute.strip()

    index = 0
    for letra in palavrasecreta:
        if(chute.upper() == letra.upper()):
           print("encontrei a letra {} na oposição {}". format(letra, index))
        index = index + 1

  print("jogando"

  print("fim do jogo")
