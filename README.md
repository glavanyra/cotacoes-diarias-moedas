# Pipeline ETL: Cotações Diárias de Moedas 📈

Este projeto automatiza a extração, transformação e carga (ETL) de cotações de moedas (USD-BRL e EUR-BRL) utilizando Python. Os dados são acumulados localmente em formato Parquet e sincronizados automaticamente com um dataset no Kaggle.

## 🚀 Funcionalidades
- **Extração**: Obtém dados em tempo real da [AwesomeAPI](https://docs.awesomeapi.com.br/).
- **Transformação**: Limpeza e normalização dos dados com Pandas.
- **Carga Local**: Acumula o histórico de cotações num ficheiro `.parquet` de alto desempenho.
- **Integração Kaggle**: Sincroniza a base de dados acumulada com o Kaggle através da Kaggle API.

## 🛠️ Tecnologias Utilizadas
- **Python 3.12+**
- **Pandas**: Processamento de dados.
- **Requests**: Consumo de API.
- **Pyarrow**: Manipulação de ficheiros Parquet.
- **Kaggle API**: Automatização de upload.
- **Git/GitHub**: Controlo de versão.

## 📋 Como Executar o Projeto

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/glavanyra/cotacoes-diarias-moedas.git](https://github.com/glavanyra/cotacoes-diarias-moedas.git)
   cd cotacoes-diarias-moedas