import json

dados = {
    'nome': 'Lucas',
    'idade': 26,
    'endereços': ['Rua Amábile Della Torre', 'Av Otávio Spigarollo']
}

with open('dados.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f, indent=4, ensure_ascii=False)
 
'''
indent=4: Coloca quebras de linha e espaços para deixar bonito e legível. Sem isso, tudo fica em uma única linha.

ensure_ascii=False: Define se caracteres “especiais” devem ser convertidos para Unicode escapado. Sem isso, seria assim:
{"nome": "Lucas", "endere\u00e7os": ["Rua Am\u00e1bile"]}
'''

# Lendo o arquivo JSON
with open('dados.json', 'r', encoding='utf-8') as f:
    dados_lidos = json.load(f)

print(dados_lidos)
