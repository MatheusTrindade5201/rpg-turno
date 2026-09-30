from abc import ABC, abstractmethod
import random
from config import *

class Criatura(ABC):
    def __init__(self, nome: str, vida_max: int, ataque: int, defesa: int, velocidade: int, mana_max: int = 0, mana_regen: int = 0):
        self._nome = nome
        self.__vida = vida_max
        self._vida_max = vida_max
        self._ataque = ataque
        self._defesa = defesa
        self._velocidade = velocidade
        self._defendendo = False
        self.__mana = mana_max
        self._mana_regen = mana_regen
        self._mana_max = mana_max
        self._recarga_restante  = 0

    def atacar(self, alvo):
        return alvo.receber_dano(self._ataque)

    @abstractmethod
    def pode_usar_especial(self):
        pass

    @abstractmethod
    def habilidade_especial(self, alvo):
        pass


    def receber_dano(self, dano: int, ignorar_defesa:bool = False):
        multiplicador_dano  = random.uniform(*VARIACAO_DANO)
        dano = dano * multiplicador_dano

        if not ignorar_defesa:
            dano = dano * (1 - self._defesa/100)

        if self._defendendo:
            dano = dano * REDUCAO_DEFENDER 

        dano = max(DANO_MINIMO, round(dano))

        self.__vida = max((self.__vida - dano), 0)

        return dano

    def esta_viva(self):
        return self.__vida > 0

    def defender(self):
        self._defendendo = True

    def iniciar_turno(self):
        self._defendendo = False

    def finalizar_turno(self) -> None:    
        self.__mana = min(self.__mana + self._mana_regen, self._mana_max)
        self._recarga_restante = max(0, self._recarga_restante - 1)

    def _gastar_mana(self, custo: int) -> bool:
        if self.__mana < custo:
            return False
        self.__mana -= custo
        return True

    def curar(self, quantidade):
            antes = self.__vida
            self.__vida = min(self.__vida + quantidade, self._vida_max)
            return self.__vida - antes

    @property
    def vida(self) -> int:
        return self.__vida
    

    @property
    def recarga_restante(self) -> int:
        return self._recarga_restante

    @property
    def mana(self) -> int:
        return self.__mana

    @property
    def vida_max(self) -> int:
        return self._vida_max

    def __str__(self) -> str:
        return f"{self._nome} ({self.__vida}/{self._vida_max} HP)"

    def mostrar_atributos(self) -> str:
        return (
            f"{self._nome}\n"
            f"    Vida: {self._vida_max} HP\n"
            f"    Ataque: {self._ataque}\n"
            f"    Velocidade: {self._velocidade}\n"
            f"    Defesa: {self._defesa}%"
        )

    @property
    def velocidade(self):
        return self._velocidade

    @property
    def nome(self):
        return self._nome

                


    
