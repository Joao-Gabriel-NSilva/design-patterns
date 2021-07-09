# DSL, design pattern Interpreter e Visitor


class Sub(object):
    def __init__(self, left_expr, right_expr):
        self.__expressao_esquerda = left_expr
        self.__expressao_direita = right_expr

    def avaliar(self):
        return self.__expressao_esquerda.avaliar() - self.__expressao_direita.avaliar()

    @property
    def expressao_esquerda(self):
        return self.__expressao_esquerda

    @property
    def expressao_direita(self):
        return self.__expressao_direita

    def aceitar(self, visitor):
        return visitor.visitar_subtracao(self)


class Soma(object):
    def __init__(self, left_expr, right_expr):
        self.__expressao_esquerda = left_expr
        self.__expressao_direita = right_expr

    def avaliar(self):
        return self.__expressao_esquerda.avaliar() + self.__expressao_direita.avaliar()

    def aceitar(self, visitor):
        return visitor.visitar_soma(self)

    @property
    def expressao_esquerda(self):
        return self.__expressao_esquerda

    @property
    def expressao_direita(self):
        return self.__expressao_direita


class Numero(object):
    def __init__(self, numero):
        self.__numero = numero

    def avaliar(self):
        return self.__numero

    def aceitar(self, visitor):
        return visitor.visitar_numero(self)


if __name__ == '__main__':
    from impressao import Impressora

    expressao_esquerda = Sub(Numero(10), Numero(5))
    expressao_direita = Soma(Numero(2), Numero(10))
    expressao_conta = Soma(expressao_esquerda, expressao_direita)

    visitor = Impressora()
    print(expressao_conta.aceitar(visitor))
