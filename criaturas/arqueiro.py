from .base import Criatura
from config import *
import random



class Arqueiro(Criatura):
    def __init__(self):
        super().__init__("Legola", ARQUEIRO["vida"], ARQUEIRO["ataque"], ARQUEIRO["defesa"], ARQUEIRO["velocidade"])

    def pode_usar_especial(self):
        return self._recarga_restante == 0

    def habilidade_especial(self, alvo: Criatura) -> int:
        if not self.pode_usar_especial():
            raise RuntimeError("Tiro Certeiro em recarga")

        self._recarga_restante =  TIRO_CERTEIRO_RECARGA + 1
        return alvo.receber_dano(self._ataque * TIRO_CERTEIRO_MULTIPLICADOR)

    def atacar(self, alvo: Criatura):
        dano  = self._ataque
        
        if random.random() < ARQUEIRO_CHANCE_CRITICO:
            dano = dano * 2

        return alvo.receber_dano(dano)


    

