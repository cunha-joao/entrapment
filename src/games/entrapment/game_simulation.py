def simulacao_jogos(num_simulacoes, nivel_dificuldade1, nivel_dificuldade2):
    vitorias_jogador1 = 0
    vitorias_jogador2 = 0
    empates = 0

    for i in range(num_simulacoes):
        # Criar jogadores com os níveis de dificuldade desejados
        jogador1 = criar_jogador(nivel_dificuldade1)
        jogador2 = criar_jogador(nivel_dificuldade2)

        # Iniciar um novo jogo
        tabuleiro = iniciar_tabuleiro()
        jogador_atual = JOGADOR1

        # Loop principal do jogo
        while not jogo_finalizado(tabuleiro):
            # Obter o movimento do jogador atual
            if jogador_atual == JOGADOR1:
                posicao_origem, posicao_destino = jogador1.escolher_movimento(tabuleiro)
            else:
                posicao_origem, posicao_destino = jogador2.escolher_movimento(tabuleiro)

            # Realizar o movimento no tabuleiro
            realizar_movimento(tabuleiro, posicao_origem, posicao_destino)

            # Alterar o jogador atual
            if jogador_atual == JOGADOR1:
                jogador_atual = JOGADOR2
            else:
                jogador_atual = JOGADOR1

        # Verificar o resultado final do jogo
        resultado = verificar_resultado(tabuleiro)

        # Atualizar o número de vitórias, derrotas e empates
        if resultado == VITORIA_JOGADOR1:
            vitorias_jogador1 += 1
        elif resultado == VITORIA_JOGADOR2:
            vitorias_jogador2 += 1
        else:
            empates += 1

    # Exibir os resultados das simulações
    print("Número de simulações: ", num_simulacoes)
    print("Nível de dificuldade do jogador 1: ", nivel_dificuldade1)
    print("Nível de dificuldade do jogador 2: ", nivel_dificuldade2)
    print("Número de vitórias do jogador 1: ", vitorias_jogador1)
    print("Número de vitórias do jogador 2: ", vitorias_jogador2)
    print("Número de empates: ", empates)
