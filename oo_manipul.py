import re

class ExtratorURL: #CRIANDO UMA CLASSE
    def __init__(self, url) -> None: #CONSTRUTOR DA CLASSE RECEBE A URL
        self.url = self.sanitizacao(url)
        self.validando_url()
#VALIDANDO A SANITIZACAO
#MELHORANDO O CODIGO--- CASO O VALOR URL NÃO SEJA STRING ELA VAI RETORNAR VAZIO
    def sanitizacao(self, url):
        #return url.strip()   #RETORNANDO A URL COM A EXTENÇÃO STRIP() ANULA OS ESPACAMENTOS
        #MELHORANDO O CODIGO------- VERIFICANDO SE O VALOR É STRING OU VAZIO
        if type(url) == str:
            return url.strip()
        else:
            return ""    
#VALIDANDO ERRRO NA URL
    def validando_url(self):
        if not self.url:
            raise ValueError("URL vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)


        if not match:
            raise ValueError("URL not validi")

    

#ORGANIZANDO O CODIGO PARA CLASSES-EXERCICIO DA URL

#ORGANIZANDO SEPARANDO PARAMETRO BASE
    def get_url_base(self):#INICIO DA URL
        url_base = self.url.find("?")
        url_inicio = self.url[:url_base]
        return url_inicio

    def get_url_parametro(self):#FIM DA URL
        url_base = self.url.find("?")
        url_final = self.url[url_base+1:]
        return url_final

    def get_valor_parametro(self, parametro_busca):
        
    #indice_parametro = self.url_final.find(parametro_busca)
    #url_final ESTÁ EM FUNCAO---VALOR PASSADO AGORA É get_url_parametro
        indice_parametro = self.get_url_parametro().find(parametro_busca)#<- PASSAR O PARAMETRO DE BUSCA
        indice_valor = indice_parametro + len(parametro_busca) + 1
        ecomercial = self.get_url_parametro().find('&', indice_valor)

        if ecomercial == -1:
            valor = self.get_url_parametro()[indice_valor:]
        else:
            valor = self.get_url_parametro()[indice_valor:ecomercial]

        return valor 

    def __len__(self):
        return len(self.url)

    def __str__(self) -> str:
        return self.url + "\n" + "Parametro: " + self.get_url_parametro() + '\n' + "URL Base: " + self.get_url_base()

    def __eq__(self, other) -> bool:
        return self.url == other.url    

#passando para classes

extrator_url = ExtratorURL("bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real")
print("O tamanho: " , len(extrator_url))
#extrator_url = ExtratorURL(" ")
# valor_quantidade = extrator_url.get_valor_parametro("moedaOrigem") 
# print(valor_quantidade)