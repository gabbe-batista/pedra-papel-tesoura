import random

print("==== BEM-VINDO AO PEDRA, PAPEL E TESOURA! ====")

#Listas
opcoes = ["Pedra", "Papel", "Tesoura"]
respostasvitória = ["Mandou bem!", "Detonou!", "Isso aí", "Incrível"]
respostasderrota = ["Qué-qué-qué", "Não foi dessa vez!", "Talvez da próxima", "Quase me pegou"]
respostasempate = ["Ok, a próxima é minha!", "Se eu não ganho, você também não!", "Empate..."]
playerwinner = ["Você é um mestre da estratégia! Quer dar aulas pro computador?", "Computador desligando... erro 404: vitória não encontrada.", "Você esmagou a máquina! Quer que eu chame o técnico?"]
computerwinner = ["Haha! A Skynet agradece sua colaboração.", "O computador venceu. Hora de reconsiderar suas escolhas de vida?", "Não se preocupe, até os melhores perdem... às vezes."]
draw = ["Empate?! Vocês estão sincronizados mentalmente!", "Parece que temos um duelo de titãs... ou só azar mesmo.", "Empate! O universo decidiu que ninguém sai ganhando hoje."]
invalidchoice = ["Você tentou inventar uma nova jogada? 😂", "Hmm... isso não é uma opção, mas eu gostaria que fosse.", "Se você jogou 'Wi-Fi', a vitória é sua. Todo mundo respeita o Wi-Fi."]

#Pontos
playerpoints = 0
computerpoints = 0
consecutivewins = 0

#nome
nome = input("Digite seu nome: ")

#Configuração de rodadas
def roundcont():
    global rodadasdesejadas
    try:   
        while True:
                rodadasdesejadas = int(input("Digite o número de rodadas que deseja jogar: (3 ou 5): ")) + 1
                if rodadasdesejadas == 4 or rodadasdesejadas == 6:
                    game()
                    break
                else: 
                    print("Esse não é um número válido, dãnnn!")
    except ValueError:
        print("Digite um número!")
        roundcont()
        

rodada = 1

#Jogo
def game():
    global opcoes, playerpoints, computerpoints, rodadasdesejadas, rodada, consecutivewins, respostasvitória, respostasempate, respostasderrota, playerwinner, computerwinner, draw, invalidchoice, nome

    print(f"Vamos começar {nome}!")

    while True:
        print(f"==== RODADA {rodada}/{rodadasdesejadas - 1}====")
        
        player = input("Escolha: 🪨 Pedra, 📄 Papel ou ✂️ Tesoura?: ").capitalize()
        computer = random.choice(opcoes)
       
        # Player ganha
        if player == "Pedra" and computer == "Tesoura" or player == "Tesoura" and computer == "Papel" or player == "Papel" and computer == "Pedra":
            print(f"🫵 Você: {player} | 🤖Computador: {computer}")
            print(f"Você ganhou🏆! {player} ganha de {computer}.")
            print(random.choice(respostasvitória))
            playerpoints += 1
            rodada += 1
            consecutivewins += 1
        
        # Computador ganha  
        elif computer == "Pedra" and player == "Tesoura" or computer == "Tesoura" and player == "Papel" or computer == "Papel" and player == "Pedra":
            print(f"🫵 Você: {player} | 🤖Computador: {computer}")
            print(f"Você perdeu😭! {computer} ganha de {player}.")
            print(random.choice(respostasderrota))
            computerpoints += 1
            rodada += 1
            consecutivewins = 0
        
        #Empate    
        elif computer == player:
            print(f"🫵 Você: {player} |🤖 Computador: {computer}")
            print(f"Empate🫠! Você e a máquina escolheram {player}.")
            print(random.choice(respostasempate))
            rodada += 1
            consecutivewins = 0
        
        #Valor inválido
        else:
            print(random.choice(invalidchoice))
            continue
       
       #Melhor de 3
        if rodadasdesejadas == 4 and rodada == 3 and playerpoints == 2 and computerpoints == 0 or rodadasdesejadas == 4 and rodada == 3 and playerpoints == 0 and computerpoints == 2:
            placar()
            break
        #Melhor de 5
        elif rodadasdesejadas == 6 and rodada == 5 and playerpoints == 3 and computerpoints == 0 or rodadasdesejadas == 6 and rodada == 5 and playerpoints == 0 and computerpoints == 3:
            placar()
            break
        elif rodadasdesejadas == rodada:
            placar()
            break
        
            
#Pontuação
def placar():
    global playerpoints, computerpoints, consecutivewins, playerwinner, computerwinner, draw, invalidchoice, nome, rodada, rodadasdesejadas
    
    while True:
        print("==== 🎖️ 🎖️ 🎖️ PONTUAÇÃO TOTAL 🎖️ 🎖️ 🎖️ ====")
        print(f"🟨 {nome}: {playerpoints} pontos")
        print(f"🟥 Computador: {computerpoints} pontos,")
        print(f"Vitórias consecutivas: {consecutivewins}")
        if playerpoints > computerpoints:
            print("VOCÊ É O VENCEDOR!!!🥇")
            print(random.choice(playerwinner))
        elif computerpoints > playerpoints:
            print("VOCÊ PERDEU!❌🤬")
            print(random.choice(computerwinner))
        else:
            print("EMPATE!")
            print(random.choice(draw))
        novapartida = input("Deseja jogar uma nova partida? (S/N): ").upper()
        if novapartida == "S":
            print("==== NOVO JOGO ====")
            playerpoints = 0
            computerpoints = 0
            rodada = 1
            roundcont()
            break
        elif novapartida == "N":
            print(f"Até logo, foi divertido jogar com você {nome}!")
            break
        else:
            print("Opção inválida!")

roundcont()