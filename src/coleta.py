# %%
import requests
import zipfile
import io
import pandas as pd
import sqlite3
# %%
# Candidatos_2024
url_zip = 'https://cdn.tse.jus.br/estatistica/sead/odsele/consulta_cand/consulta_cand_2024.zip'
nome_csv = 'consulta_cand_2024_BRASIL.csv'
nome_tabela = 'tb_candidatos_2024'
nome_db = '..\\data\\processed\\db_dadostse.sqlite3'
# %%
# Fazer o download do arquivo ZIP extrair o CSV e carregar no SQLite
try:
        response = requests.get(url_zip)
        response.raise_for_status()
        print("Download concluído com sucesso!")

        zip_file = zipfile.ZipFile(io.BytesIO(response.content))

        with zip_file.open(nome_csv) as csv_file:            
            df = pd.read_csv(csv_file, encoding='latin1', sep=';')
            print("CSV lido com sucesso!")
            print("Primeiras 5 linhas do DataFrame:")
            print(df.head())

        conn = sqlite3.connect(nome_db)
        print("Conexão com o banco de dados estabelecida!")

        df.to_sql(nome_tabela, conn, if_exists='replace', index=False)
        print("Dados exportados com sucesso!")

        conn.close()
        print("Conexão com o banco de dados fechada.")

except requests.exceptions.RequestException as e:
    print(f"Erro ao baixar o arquivo: {e}")
except zipfile.BadZipFile:
    print("O arquivo baixado não é um arquivo ZIP válido.")
except KeyError:
    print(f"O arquivo '{nome_csv}' não foi encontrado dentro do ZIP.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

