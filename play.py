import sys
import time
import random
import os
import keyboard  # pip install keyboard

# =========================================================
# CONFIGURAÇÕES INICIAIS
# =========================================================
os.system("color 04")  # Fundo preto e letras vermelhas

# =========================================================
# FUNÇÕES DE ESCRITA E LIMPEZA
# =========================================================
def escrever(texto, velocidade=0.08):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()

def escrever_erro(texto, velocidade=0.12):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()

def limpar():
    os.system("cls")

# =========================================================
# ASCII ART
# =========================================================
heroi = """
       O  /          
     (/|\/           
      / \ 
"""

monstro = """
        (\_._/)          
        ( o o )         
       ( = - = )       
      / | | | | \       
     /  | | | |  \      
    /   | | | |   \    
   /    | | | |    \    
  /     | | | |     \  
 (      | | | |      )  
(_______|_ | |_ |_____)
"""

rei = """
       🜲         
      /|\\       
      / \\
"""

# =========================================================
# FUNÇÕES DE JOGO
# =========================================================
def escolher_acao():
    while True:
        escolha = input("> ")
        if escolha in ["1", "2"]:
            return escolha

# Sequências manuais do monstro
sequencias_monstro = [
    ["right", "left", "down", "down", "up"],
    ["up", "up", "left", "right", "down"],
    ["left", "right", "up", "down", "left"],
    ["down", "up", "down", "right", "right"]
]
indice_atual = 0  # Controla qual sequência o jogador deve atacar

# =========================================================
# FUNÇÃO DE ATAQUE DO MONSTRO (nova mecânica)
# =========================================================
def ataque_monstro():
    global indice_atual
    ataque = sequencias_monstro[indice_atual]
    entrada = []

    escrever("\nO monstro está atacando! Observe a sequência!")

    # Padroniza o tamanho das teclas para 5 caracteres
    def formatar_tecla(tecla):
        return tecla.upper().ljust(5)

    # Piscar 3 vezes a sequência
    for _ in range(3):
        linha = " ".join([formatar_tecla(x) for x in ataque])
        print("\r" + linha, end="", flush=True)
        time.sleep(0.7)
        print("\r" + " " * len(linha), end="", flush=True)
        time.sleep(0.7)
    print()  # linha final limpa

    escrever("Agora, defenda a tempo! Você tem 5 segundos!")

    start_time = time.time()

    # ============================
    # Contagem de tempo visual (5 pontos)
    # ============================
    def mostrar_tempo(elapsed):
        pontos = ["●" if i < int(elapsed) else "." for i in range(5)]
        print("\rTempo: " + " ".join(pontos), end="", flush=True)

    # Captura teclas em tempo real
    def capturar_tecla(e):
        nonlocal entrada
        if e.name in ["up","down","left","right"]:
            if len(entrada) < len(ataque):
                entrada.append(e.name)

    keyboard.on_press(capturar_tecla)

    while len(entrada) < len(ataque):
        elapsed = time.time() - start_time
        if elapsed > 5:
            keyboard.unhook_all()
            escrever_erro("\n⏱️ Tempo esgotado! Você não conseguiu defender a tempo.")
            return False
        mostrar_tempo(elapsed)
        time.sleep(0.05)

    keyboard.unhook_all()
    print()  # quebra de linha final

    if entrada == ataque:
        escrever("🛡️ Você bloqueou o ataque do monstro!")
        indice_atual = (indice_atual + 1) % len(sequencias_monstro)
        return True
    else:
        escrever_erro("💥 Você errou a sequência!")
        return False

# =========================================================
# FUNÇÃO DO MAPA
# =========================================================
def mapa():
    while True:
        limpar()
        escrever("Você chegou a um mapa. Para onde deseja ir?")
        print("\n1 - Reino Rubi")
        print("2 - Floresta")

        escolha = input("> ")
        if escolha == "1":
            limpar()
            print(rei)
            escrever("👑 Rei: Vá à floresta! O reino está em perigo!")
            escrever("⚔️ Os monstros já derrotaram quase todos os aventureiros...")
            input("\nPressione ENTER para continuar...")
        elif escolha == "2":
            escrever("Você vai para a floresta e retorna à batalha!")
            input("\nPressione ENTER para continuar...")
            batalha()
            return

# =========================================================
# CUTSCENE DO REI APÓS VITÓRIA
# =========================================================
def recompensa_rei():
    limpar()
    print(rei)
    escrever("👑 Rei: Graças a você o Reino de Rubi está salvo!")
    limpar()
    escrever("💰 Tome 100 moedas de ouro.")
    escrever("🏅 Você salvou o reino!")
    escrever("""
▗▄▄▄▖▗▄▄▄▖▗▖  ▗▖
▐▌     █  ▐▛▚▞▜▌
▐▛▀▀▘  █  ▐▌  ▐▌
▐▌   ▗▄█▄▖▐▌  ▐▌""")
    input("\nPressione ENTER para encerrar o jogo...")  

# =========================================================
# FUNÇÃO DE BATALHA
# =========================================================
def batalha():
    vida_monstro = 15
    erros = 0

    while vida_monstro > 0:
        limpar()
        print("=== BATALHA ===\n")
        print("HERÓI")
        print(heroi)
        print("MONSTRO")
        print(monstro)
        print("Vida do monstro:", vida_monstro)
        print(f"Erros da sequência: {erros}/3")
        print("\n1 - Atacar")
        print("2 - Fugir")

        escolha = escolher_acao()

        if escolha == "1":
            sucesso = ataque_monstro()
            if not sucesso:
                erros += 1
                if erros >= 3:
                    limpar()
                    escrever("☠️ Você errou 3 vezes e foi derrotado pelo monstro!")
                    time.sleep(2)
                    batalha()
                    return
                continue

            dano_jogador = random.randint(3,6)
            vida_monstro -= dano_jogador
            escrever(f"\n⚔️ Você atacou e causou {dano_jogador} de dano!")
            time.sleep(1)

        elif escolha == "2":
            mapa()
            return

        if vida_monstro <= 0:
            limpar()
            escrever("🏆 Você derrotou o monstro!")
            time.sleep(1)
            recompensa_rei()
            return

# =========================================================
# INÍCIO DO JOGO
# =========================================================
limpar()
print("""
                              
        


                    ██████╗ ██████╗  ██████╗ 
                    ██╔══██╗██╔══██╗██╔════╝
                    ██████╔╝██████╔╝██║  ███╗
                    ██╔══██╗██╔═══╝ ██║   ██║
                    ██║  ██║██║     ╚██████╔╝
                    ╚═╝  ╚═╝╚═╝      ╚═════╝
▗▄▄▖ ▗▖ ▗▖▗▄▄▖ ▗▄▄▄▖    ▗▄▄▄ ▗▄▄▄▖     ▗▄▄▖ ▗▄▖ ▗▖  ▗▖ ▗▄▄▖▗▖ ▗▖▗▄▄▄▖
▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌  █      ▐▌  █▐▌       ▐▌   ▐▌ ▐▌▐▛▚▖▐▌▐▌   ▐▌ ▐▌▐▌   
▐▛▀▚▖▐▌ ▐▌▐▛▀▚▖  █      ▐▌  █▐▛▀▀▘     ▝▀▚▖▐▛▀▜▌▐▌ ▝▜▌▐▌▝▜▌▐▌ ▐▌▐▛▀▀▘
▐▌ ▐▌▝▚▄▞▘▐▙▄▞▘▗▄█▄▖    ▐▙▄▄▀▐▙▄▄▖    ▗▄▄▞▘▐▌ ▐▌▐▌  ▐▌▝▚▄▞▘▝▚▄▞▘▐▙▄▄▖
                                                                     
                                                                     
""")
input("\nPressione ENTER para começar...")

# HISTÓRIA
limpar()
escrever("Ano 1347...")
input()
limpar()
escrever("O reino de rubi está em perigo.")
input()
limpar()
escrever("Monstros começaram a aparecer nas florestas em rumo ao reino.")
input()
limpar()
escrever("Você é o único aventureiro que pode impedir isso.")
input()

# Inicia primeira batalha
batalha()