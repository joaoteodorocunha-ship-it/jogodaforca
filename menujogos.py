def escolherjogo():


print("──────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▀▌")
print("───▄▄██▌█░░░░texto░░░░▌.")
print("▄▄▄▌▐██▌█░░░░ nome░░░░▌.")
print("███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▄▌")
print("▀❍▀▀▀▀▀▀▀❍❍▀▀▀▀▀▀❍❍▀")
print("Escolha o jogo que deseja jogar")
print("[1] - Jogo da Forca")
print("[2] - Jogo de Adivinhação")



jogo = int(input ("Qual jogo você deseja jogar"))
match jogo:
    case 1:
        print("Jogando Jogo de Forca")
        jogodeadivinhacao.jogar()