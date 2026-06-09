import random
from pokemons import *

NOMES = ["Lucas", "Mariana", "Rafael", "Juliana", "Felipe", "Camila", "Gustavo", "Amanda", "Thiago", "Beatriz", "Eduardo", "Larissa", "Bruno", "Fernanda", "Diego", "Vanessa", "André", "Patricia", "Matheus", "Renata", "Leonardo", "Gabriela", "Ricardo", "Isabela", "Vinicius", "Daniela", "Caio", "Natalia", "Marcelo", "Tatiane", "João", "Bianca", "Rodrigo", "Elaine", "Pedro", "Karina", "Wesley", "Priscila", "Fabio", "Aline", "Henrique", "Simone", "Victor", "Leticia", "Cristian", "Jessica", "Samuel", "Débora", "Alan", "Michelle", "Gary"]

class Pessoas:
    def __init__(self, nome, dinheiro = 100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.dinheiro = dinheiro 
        self.pokemons = []
        self.pokebolas = 0

    def capturar_pokemon(self, pokemon_selvagem):
        self.pokemons.append(pokemon_selvagem)
        print(f"✨ {self.nome} capturou um {pokemon_selvagem.especie} (Level {pokemon_selvagem.level})!")

    def mostrar_pokemons(self):
        if not self.pokemons:
            print(f"🎒 {self.nome} não tem nenhum Pokémon na mochila.")
            return
            
        print(f"\n🎒 TIME DE POKÉMONS DE {self.nome.upper()}:")
        for indice, pokemon_atual in enumerate(self.pokemons, start=1):
            print(f"  {indice}. {pokemon_atual.especie} | Level {pokemon_atual.level} | ❤️ HP: {pokemon_atual.hp}/{pokemon_atual.hp_maximo} | ⚔️ Ataque: {pokemon_atual.ataque}")


class Player(Pessoas):
    def __init__(self, nome, dinheiro=500):
        super().__init__(nome, dinheiro)
        self.pokebolas = 3
        
    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print(f"🪙 Você ganhou ${quantidade}! Dinheiro total: ${self.dinheiro}")

    def gastar_dinheiro(self, quantidade):
        if self.dinheiro >= quantidade:
            self.dinheiro -= quantidade
            print(f"🪙 Você pagou ${quantidade}. Dinheiro restante: ${self.dinheiro}")
            return True
        else:
            print("❌ Você não tem dinheiro suficiente!")
            return False


class Inimigo(Pessoas):
    def __init__(self, tipo_treinador, nome=None, dinheiro=100):
        super().__init__(nome, dinheiro)
        self.tipo_treinador = tipo_treinador
        
        lista_classes = [Charmander, Pikachu, Squirtle, Bulbasaur, Lombre, RotomHeat]
        classe_sorteada = random.choice(lista_classes)
        self.pokemons.append(classe_sorteada(level=random.randint(4, 10)))


def escolher_pokemon_batalha(jogador):
    print("\n🎒 Escolha o Pokémon para lutar:")
    for index, pokemon_disponivel in enumerate(jogador.pokemons, start=1):
        print(f"  {index} - {pokemon_disponivel.especie} (Lv {pokemon_disponivel.level}) | ❤️ HP: {pokemon_disponivel.hp}/{pokemon_disponivel.hp_maximo}")
        
    while True:
        try:
            escolha = int(input("Sua escolha: ")) - 1
            if 0 <= escolha < len(jogador.pokemons):
                pokemon_escolhido = jogador.pokemons[escolha]
                
                if pokemon_escolhido.hp <= 0:
                    print("❌ Este Pokémon está desmaiado! Escolha outro.")
                else:
                    return pokemon_escolhido
            else:
                print("❌ Opção inválida!")
        except ValueError:
            print("❌ Digite um número válido!")


def iniciar_batalha(jogador, oponente):
    meu_pokemon = escolher_pokemon_batalha(jogador)
    pokemon_oponente = oponente.pokemons[0]      
    
    print(f"\n💥 A LUTA COMEÇOU: {meu_pokemon.especie} VS {pokemon_oponente.especie}!")
    
    while meu_pokemon.hp > 0 and pokemon_oponente.hp > 0:
        print(f"\n--- SEU TURNO ({meu_pokemon.especie} HP: {meu_pokemon.hp}/{meu_pokemon.hp_maximo}) ---")
        print("1 - Atacar")
        print("2 - Trocar de Pokémon")
        acao = input("O que deseja fazer? ")
        
        if acao == "2":
            novo_pokemon = escolher_pokemon_batalha(jogador)
            if novo_pokemon != meu_pokemon:
                meu_pokemon = novo_pokemon
                print(f"🔄 Você mandou {meu_pokemon.especie} para o combate!")
            else:
                print("🔹 Você manteve o mesmo Pokémon.")
        else:
            lista_ataques = list(meu_pokemon.meus_ataques.keys())
            for idx, nome_atk in enumerate(lista_ataques, start=1):
                print(f"  {idx} - {nome_atk}")
                
            try:
                escolha = int(input("Escolha o ataque: ")) - 1
                nome_ataque_escolhido = lista_ataques[escolha]
            except (ValueError, IndexError):
                print("❌ Opção inválida, você errou o golpe!")
                nome_ataque_escolhido = None
                
            if nome_ataque_escolhido:
                if meu_pokemon.atacar(nome_ataque_escolhido, pokemon_oponente):
                    break
                    
        # --- TURNO DO INIMIGO ---
        print(f"\n--- TURNO DO INIMIGO ({pokemon_oponente.especie} HP: {pokemon_oponente.hp}/{pokemon_oponente.hp_maximo}) ---")
        atk_inimigo = random.choice(list(pokemon_oponente.meus_ataques.keys()))
        
        if pokemon_oponente.atacar(atk_inimigo, meu_pokemon):
            pokemons_vivos = [p for p in jogador.pokemons if p.hp > 0]
            if pokemons_vivos:
                print(f"😢 Seu {meu_pokemon.especie} desmaiou! Você precisa colocar outro Pokémon!")
                meu_pokemon = escolher_pokemon_batalha(jogador)
                print(f"🔄 Vai {meu_pokemon.especie}!")
            else:
                break
            
    # --- FIM DA BATALHA ---
    if meu_pokemon.hp <= 0:
        print(f"\n💀 Todos os seus Pokémons desmaiaram... Você perdeu para {oponente.nome}!")
        jogador.pokemons[0].hp = int(jogador.pokemons[0].hp_maximo * 0.3)
        print(f"🏥 Seu {jogador.pokemons[0].especie} foi reanimado com 30% de vida no Centro Pokémon.")
    else:
        print(f"\n🏆 PARABÉNS! Você derrotou {oponente.nome}!")
        jogador.ganhar_dinheiro(pokemon_oponente.level * 20)
        meu_pokemon.ganhar_experiencia(pokemon_oponente.level * 50)