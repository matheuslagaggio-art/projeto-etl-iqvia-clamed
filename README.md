
# Projeto ETL IQVIA - CLAMED

## 📌 Descrição
Este projeto implementa um processo de ETL (Extract, Transform, Load) utilizando Python, Pandas e PostgreSQL.
O objetivo é tratar dados de vendas da IQVIA e cruzá-los com informações internas de filiais e bricks da CLAMED.

## 🛠 Tecnologias Utilizadas
- Python 3
- Pandas
- PostgreSQL
- psycopg2
- Git/GitHub
- Jupyter Notebook (validação)
- Matplotlib
  
 ---
 
O banco foi modelado em PostgreSQL utilizando:
- Tabela dimensão: dim_filial_brick
- Tabela fato: fact_vendas_iqvia

O modelo relacional foi criado no pgAdmin4.


## 📁 Estrutura do Projeto
