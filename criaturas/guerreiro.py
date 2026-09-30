from .base import Criatura
from config import *


class Guerreiro(Criatura):
    def __init__(self):
        super().__init__("Brutus", GUERREIRO["vida"], GUERREIRO["ataque"], GUERREIRO["defesa"], GUERREIRO["velocidade"])

    def pode_usar_especial(self):
        return self._recarga_restante == 0

    def habilidade_especial(self, alvo: Criatura) -> int:
        if not self.pode_usar_especial():
            raise RuntimeError("Golpe Devastador em recarga")

        self._recarga_restante =  GOLPE_RECARGA + 1
        return alvo.receber_dano(self._ataque * GOLPE_MULTIPLICADOR)


    

