class ExtratorURL: #CRIANDO UMA CLASSE
    def __init__(self, url) -> None: #CONSTRUTOR DA CLASSE RECEBE A URL
        self.url = self.sanitizacao(url)
        self.validando_url()
#VALIDANDO A SANITIZACAO
    def sanitizacao(self, url):
        return url.strip() #RETORNANDO A URL

#VALIDANDO ERRRO NA URL
    def validando_url(self):
        if self.url == "":
            raise ValueError("URL vazia")

#ORGANIZANDO O CODIGO PARA CLASSES-EXERCICIO DA URL

#ORGANIZANDO SEPARANDO PARAMETRO BASE
    def get_url_base(self):#INICIO DA URL
        url_base = self.url.find("?")
        url_inicio = self.url[:url_base]
        return url_inicio

    def url_parametro(self):#FIM DA URL
        url_base = self.url.find("?")
        url_final = self.url[url_base+1:]
        return url_final

#pasando para classes
#extrator_url = ExtratorURL("bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real")
extrator_url = ExtratorURL(" ")
#valor_quantidade = extrator_url("quantidade") 