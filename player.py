#código do jogador

import random # Importamos a ferramenta de sorteios do Python

class Player:
    def __init__(self, nome_digitado, classe_escolhida):
        # 1. Informações Básicas
        self.nome = nome_digitado
        self.classe = classe_escolhida
        self.nivel = 1
        self.xp = 0
        self.xp_needed = 100
        
        # 2. Atributos Base (Todo mundo começa com isso)
        self.vida_maxima = 100
        self.vida = 100
        self.forca = 5
        self.agilidade = 5
        self.inteligencia = 5
        self.vitalidade = 5
        self.sorte = 5
        self.destreza = 5
        
        # 3. Distribuição de Bônus Baseado na Classe!
        # Aqui a mágica acontece. O random.randint(A, B) sorteia um número entre A e B.
        
        if self.classe == "Guerreiro":
            # Guerreiro ganha bônus aleatório de força e vitalidade, mas perde inteligência
            self.forca += random.randint(3, 6) 
            self.vitalidade += random.randint(2, 4)
            self.vida_maxima += 20
            self.vida = self.vida_maxima
            self.inteligencia -= 2
            
        elif self.classe == "Assassino":
            # Assassino foca em agilidade e um pouco de força
            self.agilidade += random.randint(4, 7)
            self.forca += random.randint(1, 3)
            self.vitalidade -= 1

        elif self.classe == "Mago":
            # Mago foca muito em inteligência
            self.inteligencia += random.randint(5, 8)
            self.forca -= 3
            self.vitalidade -= 2
        
        elif self.classe == "Arqueiro":
            #classe arqueira focada em ataquem em distancia e precisão
            self.destreza += random.randint (4, 8)
            self.vitalidade -= 4
            self.agilidade += random.randint (4, 7)
            
        # Você pode ir adicionando as outras classes (Arqueiro, Lutador...) usando mais elif!
        
        # 4. Outros elementos da sua documentação
        self.inventario = []
        self.gold = 0
        self.karma = 0
        self.possui_nen = False