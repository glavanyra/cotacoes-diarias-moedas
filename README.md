# Pipeline de Extração de Cotações (ETL) 🚀

Este é um projeto de Engenharia de Dados para iniciantes que demonstra um pipeline ETL (Extract, Transform, Load) modularizado, removendo a necessidade de Notebooks e focando em boas práticas de engenharia de software.

## 📋 Objetivo
Extrair diariamente as cotações de Dólar (USD) e Euro (EUR) para Real (BRL) através de uma API pública, processar os dados para garantir tipagem correta e armazenar o resultado final em formato **Parquet**.

## 🏗️ Arquitetura
O projeto foi estruturado de forma modular para facilitar a manutenção e testes:

- **Extract**: Consome a API `AwesomeAPI`.
- **Transform**: Limpeza de dados com Pandas e conversão de tipos (String -> Float).
- **Load**: Persistência dos dados em formato colunar (.parquet).



## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.x
- **Bibliotecas:** Pandas, Requests, Pyarrow
- **Testes:** Pytest
- **Formato de Saída:** Parquet (ideal para compressão e performance em Big Data)

## 📂 Estrutura do Projeto
```text
├── data/               # Arquivos Parquet gerados
├── src/
│   ├── extract.py      # Lógica de extração
│   ├── transform.py    # Lógica de transformação
│   └── load.py         # Lógica de carga
├── tests/              # Testes unitários do pipeline
├── main.py             # Orquestrador principal
├── requirements.txt    # Dependências do projeto
└── README.md