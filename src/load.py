import pandas as pd
import os
from kaggle.api.kaggle_api_extended import KaggleApi

def salvar_parquet(df_novo, caminho="data/cotacoes.parquet"):
    """
    Salva os dados em formato Parquet, acumulando novas informações
    ao arquivo existente (Carga Incremental)."""
    # Garante que a pasta 'data' existe
    os.makedirs(os.path.dirname(caminho), exist_ok=True)

    if os.path.exists(caminho):
        print(f"Arquivo existente encontrado em {caminho}. Lendo histórico...")
        # 1. Lê o histórico existente
        df_historico = pd.read_parquet(caminho)

        # 2. Une o histórico com os novos dados
        # drop_duplicates garante que se você rodar o script 2x no mesmo dia, 
        # ele não vai duplicar a mesma linha.
        df_final = pd.concat([df_historico, df_novo], ignore_index=True).drop_duplicates()

        print(f"Novos dados adicionado. Total de registros: {len(df_final)}")

    else:
        print("Primeira execução. Criando novo arquivo histórico...")
        df_final = df_novo

    # 3. Salva o resultado final (histórico atualizado)
    df_final.to_parquet(caminho, index=False)
    print(f"Arquivo salvo com sucesso em: {caminho}")



def upload_to_kaggle():
    # Estas linhas permitem que o script use os Secrets do GitHub
    os.environ['KAGGLE_USERNAME'] = os.getenv('KAGGLE_USERNAME')
    os.environ['KAGGLE_KEY'] = os.getenv('KAGGLE_KEY')
    """
    dataset_id: seu_usuario/nome-do-dataset
    file_path: caminho para o seu arquivo .parquet ou .csv
    """
    api = KaggleApi()
    api.authenticate()

    # Atualiza o dataset com a nova versão do arquivo
    api.dataset_create_version(
        folder= "data/",
        version_notes="Atualização automática via Python Pipeline"
    )
    print("Dados enviados para o Kaggle")