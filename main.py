import random
import os
import pickle
from pokemons import * 
from pessoas import *


ARQUIVO_SAVE = "savegame.pkl"

print("====== BEM-VINDO AO MUNDO POKÉMON ======")


if os.path.exists(ARQUIVO_SAVE):
    print("💾 Encontramos um jogo salvo! Carregando seu progresso...")
    try:
        with open(ARQUIVO_SAVE, "rb") as arquivo:
            jogador = pickle.load(arquivo)
        print(f"✨ Bem-vindo de volta, Treinador {jogador.nome}!")
    except Exception as e:
        print("❌ Erro ao carregar o save. Iniciando um novo jogo...")
        jogador = None
else:
    jogador = None


if jogador is None:
    nome_usuario = input("Digite seu nome de Treinador: ")
    jogador = Player(nome_usuario)


    jogador.capturar_pokemon(Pikachu(level=5))

    print("\n🔥 O seu rival Gary aparece correndo para te desafiar!")
    gary = Inimigo(tipo_treinador="Rival", nome="Gary")
    iniciar_batalha(jogador, gary)


classes_possiveis = [
    Charmander, Cyndaquil, Growlithe, Torchic, RotomHeat,
    Pikachu, Mareep, Electrike, Shinx, Chinchou,
    Squirtle, Totodile, Mudkip, Piplup, Lombre,
    Bulbasaur, Chikorita, Treecko, Turtwig, Ludicolo
]

while True:
    print("\n======================================")
    print(f"🎒 Treinador: {jogador.nome} | 🪙 Dinheiro: ${jogador.dinheiro} | 🔴 Pokébolas: {jogador.pokebolas}")
    print("--------------------------------------")
    print("O que deseja fazer?")
    print("1 - Em busca de Pokémons (Explorar)")
    print("2 - Lutar com um inimigo direto")
    print("3 - Ver Pokeagenda (Seu Time)")
    print("4 - Ir à Loja Pokémon")
    print("5 - Ir ao Centro Pokémon 🏥")
    print("0 - Salvar e Sair do jogo 💾")
    print("======================================")
    
    escolha = input("Sua escolha: ")

    if escolha == "1":
        print("\n🌿 Você está explorando a grama alta...")
        sorteio = random.random()
        
        if sorteio <= 0.40:
            pokemon_selvagem = random.choice(classes_possiveis)(level=random.randint(2, 8))
            print(f"✨ Um {pokemon_selvagem.especie} selvagem (Level {pokemon_selvagem.level}) pulou da grama!")
            
            print("1 - Tentar Capturar")
            print("2 - Fugir")
            op_selvagem = input("Sua escolha: ")
            
            if op_selvagem == "1":
                if jogador.pokebolas > 0:
                    jogador.pokebolas -= 1
                    if random.random() <= 0.60:
                        jogador.capturar_pokemon(pokemon_selvagem)
                    else:
                        print(f"❌ Droga! O {pokemon_selvagem.especie} escapou da pokébola e fugiu!")
                else:
                    print("❌ Você não tem Pokébolas disponíveis!")
            else:
                print("💨 Você correu em segurança!")

        elif sorteio <= 0.70:
            oponente = Inimigo(tipo_treinador="Treinador de Estrada")
            print(f"🤠 O oponente {oponente.nome} ({oponente.tipo_treinador}) apareceu e quer batalhar!")
            iniciar_batalha(jogador, oponente)
            
        else:
            print("🥾 Você caminhou bastante, mas o horizonte está calmo. Nenhum sinal de Pokémons por perto.")

    elif escolha == "2":
        oponente_direto = Inimigo(tipo_treinador="Líder de Ginásio")
        print(f"🏟️ Você entrou na arena para lutar contra {oponente_direto.nome}!")
        iniciar_batalha(jogador, oponente_direto)

    elif escolha == "3":
        jogador.mostrar_pokemons()

    elif escolha == "4":
        print("\n🏪 Bem-vindo à Loja Pokémon!")
        print(f"Seu saldo atual: ${jogador.dinheiro}")
        print("1 - Comprar 1 Pokébola ($50)")
        print("2 - Voltar para a aventura")
        
        opcaoloja = input("O que deseja comprar? ")
        if opcaoloja == "1":
            if jogador.gastar_dinheiro(50):
                jogador.pokebolas += 1
                print("🔴 Você guardou a Pokébola na mochila!")
        else:
            print("🏪 Volte sempre!")

    elif escolha == "5":
        print("\n🏥 Bem-vindo ao Centro Pokémon!")
        print("Enfermeira Joy: 'Olá! Deixe-me cuidar dos seus Pokémon para você...'")
        print("🎵 *Bi-bi-bi-bi-bi...* 🎵")
        
        if hasattr(jogador, 'pokemons') and jogador.pokemons:
            for pkmn in jogador.pokemons:
                if hasattr(pkmn, 'hp_maximo'):
                    pkmn.hp = pkmn.hp_maximo
                elif hasattr(pkmn, 'hp_max'):
                    pkmn.hp = pkmn.hp_max
            print("Enfermeira Joy: 'Prontinho! Seus Pokémon estão totalmente recuperados! Boa sorte!'")
        else:
            print("Enfermeira Joy: 'Ué, parece que você não está carregando nenhum Pokémon...'")

    elif escolha == "0":
        print("\n💾 Salvando seu progresso... Não feche o jogo.")
        try:
            # Salva o objeto do jogador inteirinho no arquivo binário
            with open(ARQUIVO_SAVE, "wb") as arquivo:
                pickle.dump(jogador, arquivo)
            print("✅ Progresso salvo com sucesso!")
        except Exception as e:
            print(f"❌ Erro ao salvar o progresso: {e}")
            
        print("\n👋 Obrigado por jogar! Boa sorte no deploy para o GitHub!")
        break
    else:
        print("❌ Escolha inválida! Digite um número do menu.")