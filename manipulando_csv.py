import csv

with open('dados.csv', 'w') as f:
    escritor = csv.writer(f)
    escritor.writerow(['nome', 'idade']) # writerow: escreva na linha
    escritor.writerow(['Lucas', 26])

# Lendo um arquivo evitando problemas com linhas em branco e com acentos
with open('dados.csv', newline='', encoding='utf-8') as f:
    leitor = csv.reader(f)
    for linha in leitor:
        print(linha)
'''
['nome', 'idade']
['Lucas', '26']
'''

'''
O newline='' não remove linhas em branco. Ele apenas evita o problema do sistema operacional de ler o arquivo incorretamente
e acabar criando linhas novas, deixando-as em branco.
'''

# Adicionando novos dados no arquivo .csv
with open('dados.csv', 'a', newline='', encoding='utf-8') as f:
    escritor = csv.writer(f)
    escritor.writerow(['Pamela', 22])
    escritor.writerow(['Bruno', 24])

'''
No csv, a primeira linha é chamada de "header"
O header costuma ser o "cabeçalho"
As demais linhas são chamadas de "row" (linha)
'''
