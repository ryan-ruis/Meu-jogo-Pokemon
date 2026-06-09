# 🎮 Pokémon Terminal RPG

<p align="center">
  <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/25.gif" alt="Pikachu Animado" width="80"/>
  <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/4.gif" alt="Charmander Animado" width="80"/>
  <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/7.gif" alt="Squirtle Animado" width="80"/>
  <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/1.gif" alt="Bulbasaur Animado" width="80"/>
</p>



<h4 align="center"> 
  🚀 Pokémon Terminal RPG concluído com sucesso! 🏁
</h4>

<p align="center">
 <a href="#-sobre-o-projeto">Sobre</a> •
 <a href="#-funcionalidades">Funcionalidades</a> •
 <a href="#-foco-em-poo">Foco em POO</a> •
 <a href="#-como-jogar">Como Jogar</a> •
 <a href="#-autor">Autor</a>
</p>

---

## 📋 Sobre o Projeto

Este projeto é um jogo de RPG baseado no universo Pokémon desenvolvido inteiramente em **Python** para rodar direto no terminal. O jogo simula mecânicas clássicas como exploração de mapas, encontros aleatórios na grama alta, gerenciamento de equipe e batalhas em turnos.

---

## ✨ Funcionalidades do Game

* 🎒 **Criação de Treinador:** Defina seu nome de usuário e comece sua jornada com um Pikachu inicial (Level 5).
* 🌿 **Exploração Avançada:** Explore a grama alta com chances calculadas de encontrar Pokémons selvagens ou Treinadores de Estrada desafiadores.
* 🔴 **Sistema de Captura:** Utilize suas Pokébolas consumíveis para tentar capturar novos companheiros para sua equipe.
* 🏪 **Loja Pokémon:** Gerencie seu dinheiro ganho em batalhas para comprar suprimentos e reabastecer suas Pokébolas.
* 🏥 **Centro Pokémon:** Recupere completamente os pontos de vida (HP) de toda a sua equipe conversando com a Enfermeira Joy.
* 💾 **Sistema de Salvamento Automático:** O progresso do treinador e de seus Pokémons é salvo ao sair e carregado automaticamente ao iniciar o jogo, evitando ter que recomeçar do zero.

---

## 🧠 Foco em Orientação a Objetos (POO)

Este projeto foi desenvolvido como meu ambiente de consolidação e treino em **Programação Orientada a Objetos** em Python. Durante a construção da arquitetura do jogo, apliquei e exercitei conceitos pilares do paradigma:

* **Classes e Objetos:** Toda a lógica estrutural é baseada em entidades reais do jogo (`Player`, `Inimigo`, `Pokemon`).
* **Herança:** Utilizada extensivamente para estender os tipos de Pokémons e Treinadores a partir de classes base genéricas, reaproveitando atributos e comportamentos comuns.
* **Polimorfismo:** Implementado na execução das batalhas e cálculo de ações dinâmicas baseadas na classe específica que está em campo.
* **Persistência de Objetos (Pickle):** Desafio prático superado ao utilizar serialização binária com o módulo `pickle` para salvar e recuperar estados de instâncias completas de objetos direto em disco.

---

## 🚀 Como Jogar

### Pré-requisitos
Você precisará apenas do [Python 3](https://www.python.org/downloads/) instalado na sua máquina.

### 💻 Executando Localmente

```bash
# 1. Clone este repositório
$ git clone [https://github.com/ryan-ruis/Meu-jogo-Pokemon.git](https://github.com/ryan-ruis/Meu-jogo-Pokemon.git)

# 2. Entre na pasta do projeto
$ cd pokemon-Ryan

# 3. Execute o jogo
$ python main.py
