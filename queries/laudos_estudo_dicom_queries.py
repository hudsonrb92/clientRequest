class LaudoEstudoDicomQuery():
    def insere_laudo(self, sessao, laudo):
        sessao.add(laudo)