"""Valores de balanceamento do jogo de combate por turnos.

Validados em simulação (5.000 batalhas por confronto). Altere um número
por vez e jogue algumas partidas antes de mexer no próximo.
"""

# ---------------------------------------------------------------------------
# Regras gerais
# ---------------------------------------------------------------------------
VARIACAO_DANO = (0.9, 1.1)   # todo dano é multiplicado por um valor sorteado nesse intervalo
DANO_MINIMO = 1              # nenhum golpe causa menos que isso
REDUCAO_DEFENDER = 0.5       # "Defender" reduz o dano recebido pela metade até o seu próximo turno

# ---------------------------------------------------------------------------
# Atributos base  (defesa = % de redução do dano recebido)
# ---------------------------------------------------------------------------
GUERREIRO = {"vida": 165, "ataque": 18, "defesa": 5, "velocidade": 8, "mana": 0}
MAGO = {"vida": 130, "ataque": 14, "defesa": 5, "velocidade": 12, "mana": 100}
ARQUEIRO = {"vida": 145, "ataque": 20, "defesa": 5, "velocidade": 14, "mana": 0}
CURANDEIRO = {"vida": 215, "ataque": 16, "defesa": 15, "velocidade": 10, "mana": 100}

# ---------------------------------------------------------------------------
# Habilidades especiais
# ---------------------------------------------------------------------------
# Guerreiro - Golpe Devastador: ataque x 2.6, reduzido pela defesa do alvo
GOLPE_MULTIPLICADOR = 2.6
GOLPE_RECARGA = 2            # turnos do Guerreiro até poder usar de novo

# Mago - Bola de Fogo: dano fixo que IGNORA a defesa do alvo
BOLA_DE_FOGO_DANO = 38
BOLA_DE_FOGO_CUSTO = 30
MAGO_REGEN_MANA = 10         # recupera ao fim de cada turno do Mago

# Arqueiro - passiva + Tiro Certeiro
ARQUEIRO_CHANCE_CRITICO = 0.30   # só no ataque normal; crítico = dano x 2
TIRO_CERTEIRO_MULTIPLICADOR = 1.5  # ataque x 1.5, IGNORA a defesa do alvo
TIRO_CERTEIRO_RECARGA = 2

# Curandeiro - Cura
CURA_QUANTIDADE = 35         # nunca ultrapassa a vida máxima
CURA_CUSTO = 40
CURANDEIRO_REGEN_MANA = 5

# ---------------------------------------------------------------------------
# IA do oponente (a que foi usada no balanceamento)
# ---------------------------------------------------------------------------
IA_CHANCE_DEFENDER = 0.10
IA_CHANCE_ATAQUE_NORMAL = 0.10   # no restante, usa a especial se puder
IA_LIMIAR_CURA = 0.30            # Curandeiro só cura abaixo de 30% da vida
