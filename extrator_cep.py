
endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440120"

import re #chamando a expressao regular


#encontrando o cep PADRÃO = 5 DIGITOS + HIFEN(OPCIONAL) + 3 DIGITOS 

# importando_padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]") #PARA OPCAO DE HIFEN UTILIZA-SE A '?' DEPOIS DO COLCHETE

# importando_padrao = re.compile("[0123456789]{5}[-]?[0123456789]{3}") #MELHORANDO O CODIGO

importando_padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}") #MELHORANDO O CODIGO


buscar_padrao = importando_padrao.search(endereco)  # 'search()extrair o valor que esteja de acordo com o padrão fornecido 
#SE A BUSCA: VALOR BUSCA É VERDADEIRO SE EXISTIR A STRING
if buscar_padrao:
    cep = buscar_padrao.group() 
    print(cep)