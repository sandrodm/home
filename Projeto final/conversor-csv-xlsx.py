"""
Assunto: Projeto Python Final.
Descrição: Esse programa extrai um arquivo '.csv' da Web e converte para um arquivo '.xlsx'.
Autor: Sandro Donadel Moscardini.
Versão: 1.0.0.
Data: 12/09/2022.
Modo de uso: python3 conversor-csv-xlsx.py
"""

import requests, pandas, openpyxl

url = 'http://dados.tce.rs.gov.br/dados/municipal/balancete-despesa/2022.csv'
dados = requests.get(url)

arquivo_csv = open('balancete.csv', 'wb')
arquivo_csv.write(dados.content)
arquivo_csv.close()

balancete = pandas.read_csv('balancete.csv')
balancete.to_excel('balancete.xlsx')

novo_balancete = openpyxl.open('balancete.xlsx')
novo_balancete.save('novo_balancete.xlsx')

