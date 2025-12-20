# 📈 Pipeline ETL de Cotações Diárias (API → Parquet → Kaggle)

Este projeto demonstra um fluxo completo de **Engenharia de Dados**, automatizando a extração de cotações de moedas, o armazenamento otimizado em formato colunar e a sincronização com uma base de dados pública.

## 🎯 Objetivo
O pipeline foi construído para solucionar o problema de coleta manual de dados financeiros. Ele garante que um dataset no **Kaggle** seja alimentado diariamente com as cotações de fechamento do **Dólar (USD)** e **Euro (EUR)** em relação ao Real (BRL).

## 🏗️ Arquitetura do Projeto
O fluxo de dados segue os três pilares do ETL:

1.  **Extração (Extract):** Consumo de dados em tempo real via **AwesomeAPI**.
2.  **Transformação (Transform):** Limpeza, tipagem de dados e normalização utilizando a biblioteca **Pandas**.
3.  **Carga (Load):** * **Local:** Armazenamento em arquivos `.parquet` (usando `pyarrow`) para garantir alta compressão e velocidade de leitura.
    * **Nuvem:** Upload automatizado para o **Kaggle Datasets** via API oficial.

## 🤖 Automação e Monitoramento (CI/CD)
* **GitHub Actions:** O pipeline não depende de execução manual. Um robô (Workflow) é disparado automaticamente de segunda a sexta-feira às 18:00h (horário de Brasília).
* **Observabilidade (Logs):** Implementação da biblioteca `logging` do Python para registrar cada etapa do processo, permitindo auditoria e rápida identificação de falhas.
* **Segurança:** Uso de **GitHub Secrets** para gerenciar as credenciais da API do Kaggle, seguindo as melhores práticas de DevSecOps.

## 🛠️ Tecnologias e Ferramentas
* **Linguagem:** Python 3.12
* **Manipulação de Dados:** Pandas
* **Armazenamento:** Apache Parquet (via PyArrow)
* **Consumo de API:** Requests
* **Automação:** GitHub Actions
* **Ambiente de Desenvolvimento:** Manjaro Linux + VS Code

## 🔧 Configuração do Ambiente Local

Se você deseja replicar este projeto:

1.  **Clonar o repositório:**
    ```bash
    git clone [https://github.com/glavanyra/cotacoes-diarias-moedas.git](https://github.com/glavanyra/cotacoes-diarias-moedas.git)
    cd cotacoes-diarias-moedas
    ```

2.  **Criar e ativar o ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Instalar dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar credenciais do Kaggle:**
    * Obtenha seu token em `Kaggle.com` > `Settings` > `Create New Token`.
    * Coloque o arquivo `kaggle.json` na pasta `~/.kaggle/` ou configure as variáveis de ambiente `KAGGLE_USERNAME` e `KAGGLE_KEY`.

## 🚀 Como Executar
Para rodar o pipeline manualmente e visualizar o log:
```bash
python main.py