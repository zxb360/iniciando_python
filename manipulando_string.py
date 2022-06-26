url ="bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
#base para busca de parâmetro
url_base = url.find("?");
url_inicial = url[:url_base];
url_final = url[url_base + 1:];

#encontrando valores com parametros

print(url_inicial)
print(url_final)


