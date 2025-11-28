import json
import os

arquivo = 'banco_dados.json'

# Se o arquivo já existir, carrega os dados; senão, cria uma lista vazia
if os.path.exists(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            pessoas = json.load(f)
    except json.JSONDecodeError:
        pessoas = []

else:
    pessoas = []

# ---- Novo registro e adicionar ----
nome = input('Digite seu nome: ')
nascimento = input('Digite sua data de nascimento (XX/XX/XXXX): ')
endereco = input('Digite seu endereço: ')

# ID automático
novo_id = len(pessoas) + 1

dados = {
    'id': novo_id,
    'nome': nome,
    'nascimento': nascimento,
    'endereco': endereco
}

pessoas.append(dados)

# Salvar tudo na base de dados
with open(arquivo, 'w', encoding='utf-8') as f:
    json.dump(pessoas, f, indent=4, ensure_ascii=False)

print('Registro salvo com sucesso!')
