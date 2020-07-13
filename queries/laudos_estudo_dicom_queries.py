class LaudoEstudoDicomQuery():
    @staticmethod
    def insere_laudo(sessao, laudo):
        sessao.add(laudo)
