from .base import Criatura
from config import *


class Curandeiro(Criatura):
    def __init__(self):
        super().__init__("Xamã", CURANDEIRO["vida"], CURANDEIRO["ataque"], CURANDEIRO["defesa"], CURANDEIRO["velocidade"], CURANDEIRO["mana"], CURANDEIRO_REGEN_MANA)

    def pode_usar_especial(self):
        is_below_minimum = self.vida <= (self.vida_max * IA_LIMIAR_CURA)

        return is_below_minimum and self.mana >=  CURA_CUSTO


    def habilidade_especial(self, alvo) -> int:
        if not self.pode_usar_especial():
            raise RuntimeError("Condições do especial não atendidas")

        self._gastar_mana(CURA_CUSTO)

        return self.curar(CURA_QUANTIDADE)



    

