from src.extract import buscar_cotacao
from src.transform import transformar_dados
from src.load import salvar_parquet, upload_to_kaggle # Importe a nova função
import logging

# Configuração do "Diário de Bordo" (Log)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler() # Isso faz o log aparecer no GitHub Actions
    ]
)

def executar_pipeline():
    logging.info("Iniciando o pipeline de cotações...")

    # 1. Extração
    dados = buscar_cotacao()

    # Adicionar verificação ("filtro" de segurança)
    if dados is None:
        logging.error("Falha na extração: API indisponível ou limite excedido.")
        return
    
    # 2. Transformação
    try:
        df_final = transformar_dados(dados)
        logging.info(f"Transformação concluída. {len(df_final)} linhas processadas.")
    except Exception as e:
        logging.error(f"Erro na transformação: {e}")
        return
    
    # 3. Carga Local (Acumulando dados)
    logging.info("Salvando localmente...")
    salvar_parquet(df_final)

    # 4. Upload para Kaggle
    logging.info("Iniciando upload para o Kaggle...")
    try:
        upload_to_kaggle()
        logging.info("Pipeline finalizado com sucesso!")
    except Exception as e:
        print(f"Erro ao subir para Kaggle: {e}")

if __name__ == "__main__":
    executar_pipeline()