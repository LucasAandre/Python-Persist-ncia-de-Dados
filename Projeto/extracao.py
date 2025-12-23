import json
import requests
import os
import csv

class Extracao:
    url = 'http://127.0.0.1:8000/estudantes/'
    data_base_json = 'Projeto/db.json'
    data_base_csv = 'Projeto/db.csv'

    @classmethod
    def extracao(cls):
        '''Extração dos dados e retorno em formato JSON'''
        response = requests.get(cls.url)

        if response.status_code != 200:
            return {'Erro': 'Não foi possível localizar a API.'}
        
        dados = response.json()
        
        return dados

    @classmethod
    def salvar_json(cls):
        '''Método responsável em salvar os dados extraídos em arquivo .json'''
        # Cria a pasta se não existir
        os.makedirs(os.path.dirname(cls.data_base_json), exist_ok=True)

        dados = cls.extracao()

        with open(cls.data_base_json, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

        print('JSON salvo com sucesso!')

    @classmethod
    def salvar_csv(cls):
        '''Método responsável em salvar os dados extraídos em arquivo .csv'''
        os.makedirs(os.path.dirname(cls.data_base_csv), exist_ok=True)

        dados = cls.extracao()

        # Se a extração falhar e vier dict de erro, não tenta salvar CSV
        if isinstance(dados, dict) and 'Erro' in dados:
            print(dados)
            return

        if not dados:  # lista vazia
            print("Nenhum dado para salvar.")
            return

        campos = list(dados[0].keys())  # ['name', 'birth_date', 'id']

        with open(cls.data_base_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            writer.writerows(dados)

        print('CSV salvo com sucesso!')
