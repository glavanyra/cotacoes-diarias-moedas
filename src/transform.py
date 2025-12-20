import pandas as pd

def transformar_dados(dados_json):
    """Transforma o JSON da API em um DataFrame limpo"""
    # Criando lista com os dados que queremos
    lista_limpa = []
    for moeda in dados_json.values():
        lista_limpa.append({
            "moeda": moeda["code"],
            "valor": float(moeda["bid"]),
            "data_consulta": moeda["create_date"]
        })
    
    df = pd.DataFrame(lista_limpa)
    return df