import random

TABELA_DE_TIPOS = {
    "Fogo": {"Vantagem": "Planta", "multiplicador": 2.0},
    "Agua": {"Vantagem": "Fogo", "multiplicador": 2.0},
    "Planta": {"Vantagem": "Agua", "multiplicador": 2.0},
    "Eletrico": {"Vantagem": "Agua", "multiplicador": 2.0}
}

class Pokemon:
    def __init__(self, especie, ataque, tipo, level = None, hp = 10 ):
        self.especie = especie

        if level:
            self.level = level
        else:
            self.level = random.randint (1,100)

        if tipo not in TABELA_DE_TIPOS and not isinstance(tipo, list):
            raise ValueError(f"⚠️ Erro: O tipo '{tipo}' não existe na TABELA_DE_TIPOS!")
        
        self.tipo = tipo

        self.hp_base = hp
        self.ataque_base = ataque

        self.hp_maximo = 50 + (hp * self.level)
        self.hp = self.hp_maximo  
        self.ataque = ataque + (int(ataque * 0.1) * (self.level - 1))
        
        self.meus_ataques = {}
        self.experiencia = 0
        self.proximo_level_xp = self.level * 100  

    def atacar(self, nome_ataque, pokemon):
        dados_ataque = self.meus_ataques[nome_ataque]
        dano_base = dados_ataque["dano_base"]
        tipo_ataque = dados_ataque["tipo"]
        
        multiplicador = 1.0
        
        if tipo_ataque in TABELA_DE_TIPOS:
            if TABELA_DE_TIPOS[tipo_ataque]["Vantagem"] == pokemon.tipo:
                multiplicador = TABELA_DE_TIPOS[tipo_ataque]["multiplicador"]
                print("💥 É SUPER EFETIVO!")

        variacao = random.random() * 0.3 + 0.85
        ataque_efetivo = int((self.ataque * dano_base * 0.05) * variacao * multiplicador)
        
        pokemon.hp -= ataque_efetivo
        print(f"⚔️ {self.especie} usou {nome_ataque}!")
        print(f"💥 {pokemon.especie} perdeu {ataque_efetivo} pontos de vida.")
        
        if pokemon.hp <= 0:
            pokemon.hp = 0
            print(f"💀 {pokemon.especie} foi derrotado!")
            return True
        else:
            print(f"❤️ {pokemon.especie} ficou com {pokemon.hp}/{pokemon.hp_maximo} pontos de vida.")
            return False

    def ganhar_experiencia(self, xp_ganho):
        print(f"✨ {self.especie} ganhou {xp_ganho} pontos de experiência!")
        self.experiencia += xp_ganho
        
        while self.experiencia >= self.proximo_level_xp:
            self.experiencia -= self.proximo_level_xp
            self.subir_de_nivel()

    def subir_de_nivel(self):
        self.level += 1
        self.proximo_level_xp = self.level * 100
        
        self.hp_maximo += self.hp_base
        self.hp = self.hp_maximo 
        
        bonus_ataque = int(self.ataque_base * 0.1)
        self.ataque += bonus_ataque if bonus_ataque > 0 else 1
        
        print(f"🎉 PARABÉNS! {self.especie} subiu para o Level {self.level}!")
        print(f"📊 Status Atualizados -> ❤️ HP Máximo: {self.hp_maximo} | ⚔️ Ataque: {self.ataque}\n")


class Fogo(Pokemon):
    def __init__(self, especie, ataque, tipo="Fogo", level=None, hp=10):
        super().__init__(especie, ataque, tipo, level, hp)
        self.tipo = "Fogo"
        self.ataques_possiveis = {
            "Brasas": {"dano_base": 40, "tipo": "Fogo"},
            "Lança-Chamas": {"dano_base": 90, "tipo": "Fogo"},
            "Giro de Fogo": {"dano_base": 35, "tipo": "Fogo"},
            "Explosão de Fogo": {"dano_base": 110, "tipo": "Fogo"}
        }
        if not hasattr(self, 'pulaselecao'):
            for n in random.sample(list(self.ataques_possiveis.keys()), 4):
                self.meus_ataques[n] = self.ataques_possiveis[n]


class Eletrico(Pokemon):
    def __init__(self, especie, ataque, tipo="Eletrico", level=None, hp=10):
        super().__init__(especie, ataque, tipo, level, hp)
        self.tipo = "Eletrico"
        self.ataques_possiveis = {
            "Choque do Trovão": {"dano_base": 40, "tipo": "Eletrico"},
            "Raio Trovão": {"dano_base": 90, "tipo": "Eletrico"},
            "Onda de Choque": {"dano_base": 60, "tipo": "Eletrico"},
            "Trovão": {"dano_base": 110, "tipo": "Eletrico"}
        }
        if not hasattr(self, 'pulaselecao'):
            for n in random.sample(list(self.ataques_possiveis.keys()), 4):
                self.meus_ataques[n] = self.ataques_possiveis[n]


class Agua(Pokemon):
    def __init__(self, especie, ataque, tipo="Agua", level=None, hp=10):
        super().__init__(especie, ataque, tipo, level, hp)
        self.tipo = "Agua"
        self.ataques_possiveis = {
            "Pistola de Água": {"dano_base": 40, "tipo": "Agua"},
            "Jato de Água": {"dano_base": 65, "tipo": "Agua"},
            "Surfar": {"dano_base": 90, "tipo": "Agua"},
            "Hidro Bomba": {"dano_base": 110, "tipo": "Agua"}
        }
        if not hasattr(self, 'pulaselecao'):
            for n in random.sample(list(self.ataques_possiveis.keys()), 4):
                self.meus_ataques[n] = self.ataques_possiveis[n]


class Planta(Pokemon):
    def __init__(self, especie, ataque, tipo="Planta", level=None, hp=10):
        super().__init__(especie, ataque, tipo, level, hp)
        self.tipo = "Planta"
        self.ataques_possiveis = {
            "Chicote de Vinha": {"dano_base": 45, "tipo": "Planta"},
            "Folha Navalha": {"dano_base": 55, "tipo": "Planta"},
            "Mega Dreno": {"dano_base": 40, "tipo": "Planta"},
            "Tempestade de Folhas": {"dano_base": 130, "tipo": "Planta"}
        }
        if not hasattr(self, 'pulaselecao'):
            for n in random.sample(list(self.ataques_possiveis.keys()), 4):
                self.meus_ataques[n] = self.ataques_possiveis[n]


class Charmander(Fogo):
    def __init__(self, level=None): super().__init__("Charmander", 14, level=level, hp=9)
class Cyndaquil(Fogo):
    def __init__(self, level=None): super().__init__("Cyndaquil", 12, level=level, hp=11)
class Growlithe(Fogo):
    def __init__(self, level=None): super().__init__("Growlithe", 10, level=level, hp=13)
class Torchic(Fogo):
    def __init__(self, level=None): super().__init__("Torchic", 16, level=level, hp=7)
class RotomHeat(Fogo, Eletrico):
    def __init__(self, level=None):
        self.pulaselecao = True
        Fogo.__init__(self, "Rotom-Heat", 13, level=level, hp=10)
        self.tipo = "Fogo"
        at_fogo = Fogo(self.especie, self.ataque, level=self.level).ataques_possiveis
        at_elec = Eletrico(self.especie, self.ataque, level=self.level).ataques_possiveis
        for n in random.sample(list(at_fogo.keys()), 2): self.meus_ataques[n] = at_fogo[n]
        for n in random.sample(list(at_elec.keys()), 2): self.meus_ataques[n] = at_elec[n]

class Pikachu(Eletrico):
    def __init__(self, level=None): super().__init__("Pikachu", 13, level=level, hp=9)
class Mareep(Eletrico):
    def __init__(self, level=None): super().__init__("Mareep", 10, level=level, hp=13)
class Electrike(Eletrico):
    def __init__(self, level=None): super().__init__("Electrike", 12, level=level, hp=11)
class Shinx(Eletrico):
    def __init__(self, level=None): super().__init__("Shinx", 15, level=level, hp=8)
class Chinchou(Eletrico, Agua):
    def __init__(self, level=None):
        self.pulaselecao = True
        Eletrico.__init__(self, "Chinchou", 11, level=level, hp=12)
        self.tipo = "Eletrico"
        at_elec = Eletrico(self.especie, self.ataque, level=self.level).ataques_possiveis
        at_agua = Agua(self.especie, self.ataque, level=self.level).ataques_possiveis
        for n in random.sample(list(at_elec.keys()), 2): self.meus_ataques[n] = at_elec[n]
        for n in random.sample(list(at_agua.keys()), 2): self.meus_ataques[n] = at_agua[n]

class Squirtle(Agua):
    def __init__(self, level=None): super().__init__("Squirtle", 11, level=level, hp=12)
class Totodile(Agua):
    def __init__(self, level=None): super().__init__("Totodile", 14, level=level, hp=9)
class Mudkip(Agua):
    def __init__(self, level=None): super().__init__("Mudkip", 12, level=level, hp=11)
class Piplup(Agua):
    def __init__(self, level=None): super().__init__("Piplup", 10, level=level, hp=13)
class Lombre(Agua, Planta):
    def __init__(self, level=None):
        self.pulaselecao = True
        Agua.__init__(self, "Lombre", 12, level=level, hp=11)
        self.tipo = "Agua"
        at_agua = Agua(self.especie, self.ataque, level=self.level).ataques_possiveis
        at_planta = Planta(self.especie, self.ataque, level=self.level).ataques_possiveis
        for n in random.sample(list(at_agua.keys()), 2): self.meus_ataques[n] = at_agua[n]
        for n in random.sample(list(at_planta.keys()), 2): self.meus_ataques[n] = at_planta[n]

class Bulbasaur(Planta):
    def __init__(self, level=None): super().__init__("Bulbasaur", 12, level=level, hp=11)
class Chikorita(Planta):
    def __init__(self, level=None): super().__init__("Chikorita", 9, level=level, hp=14)
class Treecko(Planta):
    def __init__(self, level=None): super().__init__("Treecko", 15, level=level, hp=8)
class Turtwig(Planta):
    def __init__(self, level=None): super().__init__("Turtwig", 11, level=level, hp=12)
class Ludicolo(Planta, Agua):
    def __init__(self, level=None):
        self.pulaselecao = True
        Planta.__init__(self, "Ludicolo", 13, level=level, hp=10)
        self.tipo = "Planta"
        at_planta = Planta(self.especie, self.ataque, level=self.level).ataques_possiveis
        at_agua = Agua(self.especie, self.ataque, level=self.level).ataques_possiveis
        for n in random.sample(list(at_planta.keys()), 2): self.meus_ataques[n] = at_planta[n]
        for n in random.sample(list(at_agua.keys()), 2): self.meus_ataques[n] = at_agua[n]