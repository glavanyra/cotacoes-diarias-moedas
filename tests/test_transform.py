import pandas as pd
from src.transform import transformar_dados

def test_transformar_dados_deve_retornar_coluna_valor_como_float():
    # Criamos um dado "falso" para testar
    mock_json = {
        "USDBRL": {"code": "USD", "bid": "5.20", "create_date": "2023-01-01"}
    }
    df = transformar_dados(mock_json)
    
    # Verificamos se o valor virou número (float) e não texto
    assert isinstance(df.iloc[0]['valor'], float)
    assert df.shape[0] == 1 # Verifica se tem 1 linha