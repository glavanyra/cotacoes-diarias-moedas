import requests

def buscar_cotacao():
    """Busca cotação de USD e EUR para BRL"""
    # Lista 
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL"
    try: 
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()

        # Vamos pegar a data da cotação do Dólar como referência
        data_cotacao =  dados['USDBRL']['create_date']
        print(f"Dados obtidos! Data da cotação da API: {data_cotacao}")

        return dados
    except Exception as e:
        print(f"Erro na extração: {e}")
        return None