# UF	=	Unidade da Federação	
# V8005	=	Idade do morador na data de referência
# V06111	=	Nos últimos três meses, utilizou a Internet em algum local
# V4750	=	Rendimento mensal familiar per capita 
# V4745	=	Nível de instrução mais elevado alcançado (todas as pessoas)




# V061112	=	O acesso à Internet foi feito através de microcomputador
# V061113	=	O acesso à Internet foi feito através de telefone celular
# V061114	=	O acesso à Internet foi feito através de tablet
# V061115	=	O acesso à Internet foi feito através de tv
# V061116	=	O acesso à Internet foi feito através de outro equipamento eletrônico
# V061111	=	Nos últimos doze meses, utilizou a Internet em algum local
# V06112	=	Tem telefone móvel celular para uso pessoal

import pandas as pd
import matplotlib.pyplot as plt
import os
print('Esperamos trabalhar no diretório')
print(os.getcwd())
print("ok")


dados = pd.read_csv('Dados_selecionados.csv')
print("ok")
# dados = dados["UF"]
dados = dados.loc["UF", "V8005", "V06111", "V4750", "V4745"]
dados
