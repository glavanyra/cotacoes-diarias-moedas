from src.extract import buscar_cotacao
from src.transform import transformar_dados
from src.load import salvar_parquet, upload_to_kaggle # Importe a nova função

def executar_pipeline():
    # 1. Extração
    print("Extraindo dados...")
    dados = buscar_cotacao()
    
    # 2. Transformação
    print("Transformando dados...")
    df_final = transformar_dados(dados)
    
    # 3. Carga Local (Acumulando dados)
    print("Salvando localmente...")
    salvar_parquet(df_final)

    # 4. Upload para Kaggle
    print("Publicando no Kaggle...")
    try:
        upload_to_kaggle()
    except Exception as e:
        print(f"Erro ao subir para Kaggle: {e}")

if __name__ == "__main__":
    executar_pipeline()