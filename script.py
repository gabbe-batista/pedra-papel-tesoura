import random

print("==== BEM-VINDO AO PEDRA, PAPEL E TESOURA! ====")
opcoes = ["Pedra", "Papel", "Tesoura"]
playerpoints = 0
computerpoints = 0
rodadasdesejadas = int(input("Digite o número de rodadas que deseja jogar: ")) + 1
rodada = 1

def game():
    global opcoes, playerpoints, computerpoints, rodadasdesejadas, rodada
    
    while True:
        print(f"==== RODADA {rodada}/{rodadasdesejadas - 1}====")
        
        player = input("Escolha: Pedra, Papel ou Tesoura?: ").capitalize()
        computer = random.choice(opcoes)
       
        # Player ganha
        if player == "Pedra" and computer == "Tesoura" or player == "Tesoura" and computer == "Papel" or player == "Papel" and computer == "Pedra":
            print(f"Você: {player} | Computador: {computer}")
            print(f"Você ganhou! {player} ganha de {computer}.")
            playerpoints += 1
            rodada += 1
        
        # Computador ganha  
        elif computer == "Pedra" and player == "Tesoura" or computer == "Tesoura" and player == "Papel" or computer == "Papel" and player == "Pedra":
            print(f"Você: {player} | Computador: {computer}")
            print(f"Você perdeu! {computer} ganha de {player}.")
            computerpoints += 1
            rodada += 1
        
        #Empate    
        elif computer == player:
            print(f"Você: {player} | Computador: {computer}")
            print(f"Empate! Você e a máquina escolheram {player}.")
            rodada += 1
        
        #Valor inválido
        else:
            print("Jogada inválida") 
       
        if rodada == rodadasdesejadas:
            
            #Pontuação
            print("==== PONTUAÇÃO TOTAL ====")
            print(f"Você: {playerpoints} pontos")
            print(f"Computador: {computerpoints} pontos,")
            if playerpoints > computerpoints:
                print("VOCÊ É O VENCEDOR!!!")
            elif computerpoints > playerpoints:
                print("VOCÊ PERDEU!")
            else:
                print("EMPATE!")
            novapartida = input("Deseja jogar uma nova partida? (S/N): ").upper()
            if novapartida == "S":
                print("==== NOVO JOGO ====")
                playerpoints = 0
                computerpoints = 0
                rodadasdesejadas = int(input("Digite o número de rodadas que deseja jogar: ")) + 1
                rodada = 1
                continue
            elif novapartida == "N":
                print("Até logo, foi divertido jogar com você!")
                break
            else:
                print("Opção inválida!")

game()