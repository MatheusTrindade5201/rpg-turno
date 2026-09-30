from criaturas import *
from batalha import *
import random

CRIATURAS = {
    "1": Arqueiro,
    "2": Guerreiro,
    "3": Curandeiro,
    "4": Mago
}

ACOES = {
    "1": Acao.atacar,
    "2": Acao.defender,
    "3": Acao.especial
}


class Menu:
    def __init__(self):
        self._escolha_jogador = None

    def escolher_personagem(self):
        print("Escolha o seu personagem:")
        for numero, classe in CRIATURAS.items():
            print(f"{numero} - {classe().mostrar_atributos()}")

        while True:
            personagem = input("Digite o número do personagem desejado: ").strip()

            if personagem in CRIATURAS:
                self._escolha_jogador = personagem
                return CRIATURAS[personagem]()

            print("Opção inválida, tente novamente.")

    def personagem_da_maquina(self):
        chaves = list(CRIATURAS.keys())
        chaves.remove(self._escolha_jogador)
        sorteada = random.choice(chaves)

        return CRIATURAS[sorteada]()

    def escolher_acao(self):
        print("Escolha a sua ação:")
        for numero, opcao in ACOES.items():
            print(f"{numero} - {opcao.value.capitalize()}")

        while True:
            acao = input("Digite o número da ação desejada: ").strip()

            if acao in ACOES:
                return ACOES[acao]

            print("Opção inválida, tente novamente.")

    def acao_ia(self, pode_usar_especial):
        opcoes = [Acao.atacar, Acao.defender]
        pesos = [10, 10]

        if pode_usar_especial:
            opcoes.append(Acao.especial)
            pesos.append(80)

        return random.choices(opcoes, weights=pesos)[0]

    def mostrar_resultado(self, autor, acao, resultado):
        if acao == Acao.atacar:
            print(f"{autor.nome} atacou e causou {resultado} de dano.")
        elif acao == Acao.defender:
            print(f"{autor.nome} está se defendendo.")
        else:
            print(f"{autor.nome} usou a habilidade especial! ({resultado})")

    def mostrar_vida(self, jogador, oponente):
        print(f"Você: {jogador}  |  Oponente: {oponente}")

    def perguntar_novo_jogo(self):
        while True:
            decisao = input("Deseja jogar novamente? (s/n)").lower().strip()
        
            if decisao in ["s", "sim", "y", "yes"]:
                return True

            elif decisao in ["n", "não", "nao", "no"]:
                return False

            print("Opção inválida, tente novamente.")


    def combate(self):
        jogador = self.escolher_personagem()
        oponente = self.personagem_da_maquina()

        print(f"\n{jogador.nome} (você) contra {oponente.nome}!")

        batalha = Batalha(jogador, oponente)

        while not batalha.tem_ganhador():
            autor = batalha.vez_de
            print(f"\n--- Vez de {autor.nome} ---")

            if autor is jogador:
                acao = self.escolher_acao()
            else:
                acao = self.acao_ia(autor.pode_usar_especial())

            try:
                resultado = batalha.fazer_acao(acao)
            except RuntimeError as e:
                print(f"Não foi possível: {e}. Escolha outra ação.")
                continue

            self.mostrar_resultado(autor, acao, resultado)
            self.mostrar_vida(jogador, oponente)

            batalha.passar_turno()

        ganhador = batalha.ganhador_batalha()
        mensagem = "Você venceu!" if ganhador is jogador else "Você perdeu!"
        print(f"\n{ganhador.nome} venceu a batalha. {mensagem}")