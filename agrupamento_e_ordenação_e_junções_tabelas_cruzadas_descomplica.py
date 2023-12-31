# -*- coding: utf-8 -*-
"""Agrupamento e Ordenação e Junções -tabelas_cruzadas Descomplica.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JbEPmJapbffoSq-Mo3s-Rmw5kXrB19pe
"""

import pandas as pd

import numpy as np

df_prouni = pd.read_excel('/content/cursos-prouni.csv.xlsx')
df_prouni

"""//Busca do curso por estado"""

pd.crosstab(df_prouni.uf_busca, df_prouni.curso_busca)

"""//Busca do curso por estado com o subtotal por linhas: parâmetro (margins = True)"""

pd.crosstab(df_prouni.uf_busca, df_prouni.curso_busca, margins = True)

pd.crosstab(df_prouni.uf_busca, [df_prouni.curso_busca, df_prouni['nota_integral_ampla']], margins = True)

pd.crosstab([df_prouni.uf_busca], [df_prouni.curso_busca], values=df_prouni.nota_integral_ampla, aggfunc= (np.sum), margins = True)

pd.crosstab([df_prouni.uf_busca], [df_prouni.curso_busca], values=df_prouni.nota_integral_ampla, aggfunc= (np.median), margins = True)

"""// Nova coluna. Definição que o df2 será uma cópia desse novo df"""

df_prouni['total_bolsas'] = df_prouni.bolsa_integral_ampla + df_prouni.bolsa_integral_cotas

df2 = df_prouni.copy()
df2

"""// Traz a porcentagem da busca do curso por estado"""

pd.crosstab(df2.nome, df2.uf_busca, normalize= 'index')

"""//Arredondando para 4 casas e deixando em porcentagem"""

pd.crosstab(df2.nome, df2.uf_busca, normalize= 'index').round(4)*100

df_agrupamento = df_prouni.groupby('curso_busca')
df_agrupamento

"""//Renorna o numero da linha onde aparece a informação"""

df_prouni.groupby('curso_busca').groups

"""//Conta a quantidade de registros"""

df_prouni.groupby('curso_busca').size()

"""//get_group filtra aquele determinado grupo"""

df_prouni.groupby('curso_busca').get_group('Administração')

df_prouni.groupby('curso_busca').mean()

"""//Soma do total de bolsas do curso por estado"""

df2.groupby(['curso_busca', 'uf_busca'])['total_bolsas'].sum()

df3 = (df2.groupby(['curso_busca', 'uf_busca'])['total_bolsas'].sum()).copy()
df3

"""//**CONCATENAÇÃO**"""

clientes = pd.read_excel('/content/CLIENTES.xlsx')
clientes

produtos = pd.read_excel('/content/PRODUTO.xlsx')
produtos

clientes['nome_completo'] = clientes.NOME + ' ' + clientes.SOBRENOME
df_clientes = clientes.copy()
df_clientes

produtos['TOTAL_VENDA'] = produtos.QUANTIDADE * produtos.PRECO_UNIT
df_produtos = produtos.copy()
df_produtos

clientes['nome_completo2'] = clientes[['NOME', 'SOBRENOME']].apply(' ' .join, axis=1)
clientes

"""//Função merge com o parâmetro inner: faz a junção pelas chaves"""

df_merge = pd.merge(df_clientes, df_produtos, how= 'inner', on='ID')
df_merge

produtos['ID'] = produtos.ID_CLIENTE
produtos

df_produtos = produtos[['ID','PRODUTO', 'QUANTIDADE', 'PRECO_UNIT', 'TOTAL_VENDA', ]]
df_produtos

"""//Função merge com o parâmetro left: faz a junção das tabelas pelas linhas da coluna à esquerda"""

df_merge = pd.merge(df_clientes, df_produtos, how= 'left', on='ID')
df_merge

"""//Função merge com o parâmetro right: faz a junção das tabelas pelas linhas da coluna à direita"""

df_merge = pd.merge(df_clientes, df_produtos, how= 'right', on='ID')
df_merge

