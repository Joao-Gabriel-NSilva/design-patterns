

class Impressora(object):

    def visitar_soma(self, soma):
        output = "({} + {})".format(soma.expressao_esquerda.aceitar(self), soma.expressao_direita.aceitar(self))
        return output

    def visitar_subtracao(self, sub):
        output = "({} - {})".format(sub.expressao_esquerda.aceitar(self), sub.expressao_direita.aceitar(self))
        return output

    def visitar_numero(self, numero):
        output = numero.avaliar()
        return output