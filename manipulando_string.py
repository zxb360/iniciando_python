#url ="bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"
url = " "

#SANITIZACAO DA URL 
url = url.strip()

if url == "":
    raise ValueError("A URL está vazia")

#base para busca de parâmetro
url_base = url.find("?");
url_inicial = url[:url_base];
url_final = url[url_base + 1:];

#encontrando valores de um parametros
parametro_busca = "moedaDestino"

indice_parametro = url_final.find(parametro_busca)

indice_valor = indice_parametro + len(parametro_busca) + 1
ecomercial = url_final.find('&', indice_valor)

if ecomercial == -1:
    valor = url_final[indice_valor:]
else:
    valor = url_final[indice_valor:ecomercial]

print(valor)