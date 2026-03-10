🗡️ RPG RUBI DE SANGUE

Bem-vindo ao RPG RUBI DE SANGUE, um jogo de batalha em terminal feito em Python!
Defenda o reino de monstros, teste sua memória com sequências de teclas e salve o dia!

🖥️ Pré-requisitos

Para rodar o RPG RUBI DE SANGUE, você precisa de:

Python 3.6 ou superior

Necessário para rodar f-strings e os módulos padrão usados no jogo (os, sys, time, random).

Biblioteca keyboard

Instale com:

pip install keyboard

Usada para capturar setas em tempo real (⬆️⬇️⬅️➡️).

⚠️ No Windows, pode precisar rodar o terminal como Administrador.

Sistema operacional

Feito para Windows (uso de cls e color 04 para limpar a tela e mudar cor do terminal).

No Linux/macOS seria necessário ajustar:

cls → clear

color 04 → usar colorama ou outro método de cores.

🎮 Como Jogar

Abra o terminal ou CMD na pasta do projeto.

Execute o jogo com:

python play.py

Siga as instruções na tela:

Você verá sequências de teclas (⬆️⬇️⬅️➡️) que o monstro usará para atacar.

Repita corretamente a sequência usando as setas do teclado.

Você tem 5 segundos para defender cada ataque.

Se errar 3 vezes, o jogo recomeça.

No mapa, escolha para onde ir:

1 - Reino Rubi: Obtenha informações do rei.

2 - Floresta: Continue as batalhas.

Derrote o monstro para receber recompensas e salvar o reino!

⚔️ Mecânicas do Jogo

Ataques do jogador: Sequências de teclas simulam batalhas estratégicas.

Erros: Se falhar 3 sequências, o jogador perde a batalha.

Vida do monstro: Diminui aleatoriamente entre 3 e 6 pontos a cada ataque bem-sucedido.

Cutscene: O rei parabeniza o jogador ao salvar o reino.

🎨 Arte do Jogo

O jogo utiliza ASCII art para representar:

Herói

Monstro

Rei

Exemplo do herói:

       O  /          
     (/|\/           
      / \ 

🛠️ Personalização

Você pode alterar:

Cores do terminal alterando: os.system("color 04")

04 = fundo preto, letras vermelhas

Sequências de ataque do monstro em sequencias_monstro

📜 História

Ano 1347...
O reino de Rubi está em perigo. Monstros começaram a atacar as florestas rumo ao reino.
Você é o único aventureiro que pode impedir isso!

🎓 Licença

Este projeto é apenas para aprendizado e diversão.
Não é para uso comercial.
