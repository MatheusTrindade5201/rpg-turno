from menu import Menu


def main():
    menu = Menu()

    quer_jogar = True

    while quer_jogar:
        menu.combate()

        quer_jogar = menu.perguntar_novo_jogo()
    


if __name__ == "__main__":
    main()
