from .base import Criatura
from config import *


class Mago(Criatura):
    def __init__(self):
        super().__init__("Merlin", MAGO["vida"], MAGO["ataque"], MAGO["defesa"], MAGO["velocidade"], MAGO["mana"], MAGO_REGEN_MANA)

    def pode_usar_especial(self):
        return self.mana >=  BOLA_DE_FOGO_CUSTO
    
    def habilidade_especial(self, alvo: Criatura) -> int:
        if not self.pode_usar_especial():
            raise RuntimeError("Mana insuficiente")

        self._gastar_mana(BOLA_DE_FOGO_CUSTO)

        return alvo.receber_dano(BOLA_DE_FOGO_DANO, True)



    

