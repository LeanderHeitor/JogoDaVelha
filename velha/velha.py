class JogoDaVelha:
    def __init__(self):
        self.jogoAtivo = False

    def comecarTabuleiro(self):
        tabuleiro = []
        for i in range(3):
            linha = [' ' for i in range(3)]
            tabuleiro.append(linha)
        return tabuleiro

    def mostrarTabuleiro(self):
        print("\nTabuleiro:")
        print("  0   1   2")
        for i in range(len(self.tabuleiro)):
            linha = self.tabuleiro[i]
            print(i, ' | '.join(linha))
            if i < 2:
                print("  " + "---+---+---")
        print()

    def verificarVitoria(self, jogador):
        for linha in self.tabuleiro:
            if self.verificarLinha(linha, jogador):
                return True

        for coluna in range(3):
            if self.verificarColuna(coluna, jogador):
                return True

        if self.verificarDiagonalPrincipal(jogador) or self.verificarDiagonalSecundaria(jogador):
            return True

        return False

    def verificarLinha(self, linha, jogador):
        for espaco in linha:
            if espaco != jogador:
                return False
        return True

    def verificarColuna(self, coluna, jogador):
        for linha in range(3):
            if self.tabuleiro[linha][coluna] != jogador:
                return False
        return True

    def verificarDiagonalPrincipal(self, jogador):
        for i in range(3):
            if self.tabuleiro[i][i] != jogador:
                return False
        return True

    def verificarDiagonalSecundaria(self, jogador):
        for i in range(3):
            if self.tabuleiro[i][2 - i] != jogador:
                return False
        return True

    def verificarEmpate(self):
        for linha in self.tabuleiro:
            for espaco in linha:
                if espaco == ' ':
                    return False
        return True

    def movimentoValido(self, linha, coluna):
        if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
            return False
        if self.tabuleiro[linha][coluna] != ' ':
            return False
        return True

    def mover(self, linha, coluna, jogador):
        if self.movimentoValido(linha, coluna):
            self.tabuleiro[linha][coluna] = jogador
            return True
        return False

    def alternarJogador(self):
        self.jogadorAtual = 'O' if self.jogadorAtual == 'X' else 'X'

    def jogar(self):
        self.tabuleiro = self.comecarTabuleiro()
        self.jogadorAtual = 'X'
        self.jogoAtivo = True

        while self.jogoAtivo:
            self.mostrarTabuleiro()
            print(f"Vez do jogador {self.jogadorAtual}")

            linha, coluna = self.escolherMovimento()

            if self.mover(linha, coluna, self.jogadorAtual):
                if self.verificarVitoria(self.jogadorAtual):
                    self.mostrarTabuleiro()
                    print(f"Jogador {self.jogadorAtual} venceu!")
                    self.jogoAtivo = False
                elif self.verificarEmpate():
                    self.mostrarTabuleiro()
                    print("Empate!")
                    self.jogoAtivo = False
                else:
                    self.alternarJogador()
            else:
                print("Movimento inválido. Tente de novo.")

        if self.jogarNovamente():
            self.jogar()
        else:
            print("Obrigado por jogar!")

    def escolherMovimento(self):
        while True:
            try:
                linha = int(input("Escolha a linha (0, 1, 2): "))
                coluna = int(input("Escolha a coluna (0, 1, 2): "))
                if linha in [0, 1, 2] and coluna in [0, 1, 2]:
                    return linha, coluna
                else:
                    print("Entrada inválida. Digite números entre 0 e 2.")
            except ValueError:
                print("Entrada inválida. Digite números inteiros.")

    def jogarNovamente(self):
        while True:
            resposta = input("Quer jogar de novo? (s/n): ").lower()
            if resposta == 's':
                return True
            elif resposta == 'n':
                return False
            else:
                print("Resposta inválida. Digite 's' para sim ou 'n' para não.")
