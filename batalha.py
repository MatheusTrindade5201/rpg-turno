from criaturas import Criatura
import random
from enum import Enum


class Acao(str, Enum):
    atacar = "atacar"
    defender = "defender"
    especial = "especial"


class Batalha:
    def __init__(self, jogador: Criatura, oponente: Criatura):
        self._jogador = jogador
        self._oponente = oponente
        self._rodada = 1
        self.definir_quem_comeca()

    def definir_quem_comeca(self):
        ordenado_velocidade = sorted([self._jogador, self._oponente], key=lambda c: c.velocidade, reverse=True)

        if self._jogador.velocidade == self._oponente.velocidade:
            primeiro_index = random.randint(0, 1)
            self._vez_de = ordenado_velocidade.pop(primeiro_index)
            self._alvo = ordenado_velocidade.pop(0)

        else:
            self._vez_de, self._alvo = ordenado_velocidade

        self._vez_de.iniciar_turno()

    def passar_turno(self):
        if self.tem_ganhador():
            return

        self._vez_de.finalizar_turno()

        self._rodada += 1
        self._vez_de, self._alvo = self._alvo, self._vez_de

        self._vez_de.iniciar_turno()


    def fazer_acao(self, acao: Acao):

        acao_dict = {
            Acao.atacar: lambda: self._vez_de.atacar(self._alvo),
            Acao.defender: lambda: self._vez_de.defender(),
            Acao.especial: lambda: self._vez_de.habilidade_especial(self._alvo)
        }

        metodo_acao = acao_dict[acao]
        return metodo_acao()


    def ganhador_batalha(self):
        if not self.tem_ganhador():
            return

        return self._jogador if self._jogador.vida > self._oponente.vida else self._oponente 

    def tem_ganhador(self):
        return not self._oponente.esta_viva() or not self._jogador.esta_viva()

    @property
    def vez_de(self):
        return self._vez_de
    