import time

x = [0,0,0,0,0,0,0]
bool = [False, False, False, False, False, False]
tentativas = 3

assets = ["-"*130,"->"]
print(assets[0])
print("Jogo Detetive")
print(assets[0])
nome = input("Informe seu nome jogador: ")
print(assets[0])
print(f"Olá, {nome} pronto(a) para investigar esse mistério? Temos um novo caso para você!\n\n"
      f"Nessa madrugada, um importante historiador, Armando Ventura, foi assassinado em sua casa, provavelmente porque \n"
      f"dias antes de morrer encontrou um artefato de grande valor, um geodo de Hope Diamont,uma das pedras \n"
      f"mais raras do mundo, e seu objetivo é desvendar o mistério de como foi o crime e vasculhar o ambiente e \n"
      f"descobrir se esta pedra foi roubada ou não, e caso não tenha sido, poderemos atrair o assassino para uma emboscada.\n\n"
      f"Boa sorte!")
time.sleep(0)
print(assets[0])
print("Você dirige por cerca de 15 minutos e chega em uma mansão grande no meio da cidade, mansão essa que era a cena do crime!\n")

while x[0] == 0:
    comodo = int(input("Qual cômodo você quer investigar?\n1 - Cozinha, 2 - Escritório, 3 - Sala de Estar, 4 - Quarto\n-> "))
    print(assets[0])
    while comodo == 1:
        print("Você está na cozinha, observa alguns itens interessantes que podem ajudar na investigação.\n ")
        cozinha = int(input("1 - Um armário aberto, 2 - Uma gaveta quebrada, 3 - O forno, 4 - Voltar\n-> "))
        time.sleep(2)
        print(assets[0])
        if cozinha == 1:
            print("Você abriu o armário, encontrou pratos, copos, e nada fora do comum.")
            print(assets[0])
        elif cozinha == 2:
            print("Você abriu a gaveta de talheres quebrada, encontrou um fundo falso levemente levantado, \nonde uma arma estava escondida!"
            "E logo abaixo você observa uma trilha de pequenas gotas de sangue indo em direção ao quarto.")
            time.sleep(2)
            print(assets[0])
        elif cozinha == 3:
            print("Você abriu o forno, e se assustou com as baratas subindo em sua mão.")
            print(assets[0])
            time.sleep(2)
        elif cozinha == 4:
            comodo = 0
    while comodo == 2 and bool[0] == False:
        print("Você tentou entrar no escritório, mas a porta estava trancada, encontre a chave.")
        print(assets[0])
        comodo = 0
    while comodo == 2 and bool[0] == True:
        print("Você usa a chave simples e está no escritório, observa alguns itens interessantes que podem ajudar na investigação.")
        escritorio= int(input(f"1 - Um quadro torto, 2 - Uma estatueta, 3 - Uma escrivaninha, 4 - Uma estante de livros, 5 - Voltar\n-> "))
        time.sleep(2)
        print(assets[0])
        if escritorio == 4:
            bool[1] = True
            print("Você começa a mexer cautelosamente na estante de livro e encontra um livro preso,\n"
                  "e decide puxar, sentindo um tremor de fundo.")
            time.sleep(2)
        elif escritorio == 2:
            print("Você pegou uma estatueta antiga, e não observou nada de interessante e a colocou no lugar.")
        elif escritorio == 1 and bool[1] == False:
            print("Você nota um quadro torto e o tira, e dá de cara com a parede.")
            time.sleep(2)
        elif escritorio == 3:
            print("Você mexe na escrivaninha, abre suas gavetas mas não acha nada de interessante.")
        elif escritorio == 5:
            comodo = 0
        elif escritorio == 1 and bool[1] == True:
            print("Você retira o quadro e se depara com um cofre com uma tranca de dígitos.")
            time.sleep(2)
            if bool[2] == True:
                print("Felizmente você encontrou a senha na sala, e pode abrir o cofre.")
                time.sleep(2)
                print(f"PARABÉNS {nome}! VOCÊ ENCONTROU O ARTEFATO!\n"
                      f"Agora só falta deduzir a sequência dos acontecimentos em cada local.")
                bool[3] = True
                time.sleep(3)
                sequencia = int(input("Digite a sequência dos acontecimentos (1 - Cozinha, 2 - Escritório, 3 - Sala de Estar, 4 - Quarto):"))
                if sequencia == 3142:
                    print(assets[0])
                    print(f"PARABÉNS {nome}! VOCÊ DEDUZIU CORRETAMENTE O CASO!\n"
                    f"Você envia o caso e a pedra pra polícia, mas sem dar informações para a mídia sobre a conclusão, \n"
                    f"então sua emboscada para o assassino esta armada e resta apensa esperar o tempo certo.")
                    time.sleep(1)
                    print("•")
                    time.sleep(1)
                    print("•")
                    time.sleep(1)
                    print("•")
                    time.sleep(2)
                    print(assets[0])
                    print("Três dias depois da polícia sair da casa, a sua emboscada se mostra efetiva, pois no meio da noite\n"
                        "o assassino voltou até a cena do crime para tentar procurar a pedra, e foi surpreendido pelo nosso plano.\n"
                        "O assassino foi identificado como")
                    time.sleep(2)
                    print("•")
                    time.sleep(2)
                    print("•")
                    time.sleep(2)
                    print("•")
                    time.sleep(2)
                    print(assets[0])
                    print("APHONSO PETROVISKI, um antigo colega de trabalho do Dr. Ventura. Em sua confissão,\n"
                    "confirmou que Armando não quis dar crédito a ele a descoberta da pedra, ainda que ele participou ativamente.\n" 
                    "Seu plano era apenas roubar a pedra, mas como não conseguiu acha-la, acabou entrando numa briga com Armando, que custou sua vida.")
                    print(assets[0])
                    time.sleep(3)
                    print(assets[0])
                    print("E assim você concluiu seu caso\n"
                    "E terminou o jogo de detetive, parabéns."
                    "Jogo feito por Carlos Mello, Henrique Tetilha e Luana Tiemann.")
                    print(assets[0])
                    time.sleep(5)
                    x[0] = 1
                    comodo = 0
                else:
                    print(assets[0])
                    time.sleep(3)
                    tentativas -= 1
                    print("Sequência incorreta\n"
                    "Restam",tentativas)
                    print(assets[0])
                    time.sleep(2)
                    if tentativas == 0:
                        print("Você fracassou na sua missão, nunca saberemos quem é o suspeito...")
                        x[0] = 1
                        comodo = 0
    while comodo == 3:
        print("Você está na sala de estar, observa alguns itens interessantes que podem ajudar na investigação.")
        time.sleep(2)
        sEstar = int(input("1 - Uma cômoda de madeira, 2 - Um vaso quebrado no chão, 3 - Uma lareira apagada, 4 - Voltar\n-> "))
        print(assets[0])
        if sEstar == 1:
            print("Você abre as gavetas da cômoda e começa a vasculhalas, porém não acha nada muito interessante.")
        elif sEstar == 2:
            print("Você chega mais perto do vaso e percebe que caiu de uma estante, parece que o objeto caiu em direção a cozinha.")
            time.sleep(2)
        elif sEstar == 3 and bool[4] == False:
            print("Você observa a lareira, mas não encontra nada, parece que não foi acesa a algumas semanas.")
            bool[4] = True
            time.sleep(1)
        elif sEstar == 3 and bool[4] == True:
            print("Você observa a lareira e percebe um espaço aberto na parte de dentro. Você coloca a mão e pega papéis que estavam escondidos.\n"
            f"Você passa as páginas e acha um código de quatro digitos, isso pode ser importante então você guarda o papel.")
            bool[2] = True
            time.sleep(2)
        elif sEstar == 4:
            comodo = 0
            time.sleep(3)
    while comodo == 4:
        print("Você está no quarto, observa alguns itens interessantes que podem ajudar na investigação.")
        time.sleep(2)
        quarto = int(input("1 - Uma cama bagunçada, 2 - Um armário aberto, 3 - Um espelho quebrado, 4 - Voltar\n-> "))
        print(assets[0])
        if quarto == 1:
            print("Você observa a cama e resolve olhar embaixo. Você acha uma pequena caixa de sapato.\n"
            "Você abre a caixa e acha uma chave simples, agora resta descobrir para que ela serve.")
            bool[0] = True
            time.sleep(2)
        elif quarto == 2:
            print("Você observa o armário mais cautelosamente e acha no bolso de um casaco uma chave dourada e com a ponta peculiar\n"
            "esta chave parece muito importante, é melhor guardá-la.")
            bool[5] = True
            time.sleep(2)
        elif quarto == 3:
            print("Você encontra um espelho quebrado com pedaços de vidro no chão, indo em direção para o escritório.")
            time.sleep(2)
        elif quarto == 4:
            comodo = 0
            time.sleep(2)



"""
Para a resolução desse mistério, primeiro você precisa ir até a sala de estar, onde a briga entre Armando e Aphonso começou, achar o código do cofre analisando duas vezes a
lareira e analisar o vaso quebrado em direção a cozinha, e depois prosseguir para o próximo cômodo, a cozinha, analisar a gaveta de talheres, onde havia uma arma escondida, 
primeiro local onde Armando foi para se defender, mas não conseguiu pegar a arma a tempo, apensas conseguiu se defender com um talher, então encontrar a trilha de sangue em 
direção ao quarto, então seguiu a procura da chave que abria o escritório escondida embaixo da cama, local onde guardava a pedra e onde foi o final desse confronto. 
Você com a chave e com um código que ainda não sabia para que serve, entra no escritório e analisa a estante de livros puxando um livro que estava num local estranho, 
escutando um barulho atrás de você, então analisa o quadro torto e descobre um cofre imbutido na parede onde insere o código e finalmente acha a tão procurada pedra preciosa,
e resolve a sequência de cômodos sequindo a lógica das dicas, sala de estar, cozinha, quarto e escritório.
"""