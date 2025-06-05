📊 Análise Financeira - MS Sample

Este projeto consiste em um dashboard interativo desenvolvido com Streamlit e Python, utilizando um conjunto de dados financeiros da Microsoft para analisar vendas, lucros e evolução temporal por país, segmento e produto.

🚀 Objetivo

Visualizar dados financeiros de forma clara e intuitiva, com gráficos dinâmicos que ajudam a entender:

🌍 Quais países mais vendem

🏷️ Quais segmentos são mais lucrativos

📅 Como as vendas evoluíram ao longo do tempo

💰 Quais produtos geram mais lucro

🛠️ Tecnologias Utilizadas

Python 3.x

Streamlit

Pandas

📁 Dataset

O arquivo utilizado é MS_Financial Sample.csv, contendo informações como:

País, segmento e produto

Preço de venda, fabricação, unidades vendidas, descontos

Lucro e custo

Datas (com ano, mês, dia)

Importante: o arquivo CSV deve estar na mesma pasta do arquivo app.py.

🧩 Etapas do Projeto

1. Instalação do Python
   
Antes de tudo, é necessário ter o Python instalado em sua máquina:
Link para download: https://www.python.org/downloads/

Para verificar se a instalação foi concluída com sucesso, abra o terminal e digite:

python --version

2. Criação de Ambiente Virtual (opcional, mas recomendado)

No Windows:

python -m venv venv

venv\Scripts\activate

No Linux/Mac:

python3 -m venv venv

source venv/bin/activate

3. Instalação das bibliotecas necessárias
   
Com o ambiente virtual ativado, instale as dependências:

pip install streamlit pandas

🧠 Como o código funciona

Leitura e limpeza de dados

O arquivo CSV é carregado com separador ;.

Os nomes das colunas são limpos para remover espaços em branco.

Os valores monetários são tratados para converter strings como $1.234,56 em números (float), e valores como "-" são substituídos por 0.0.

Conversão de datas

A coluna Date é convertida para o tipo datetime, com suporte ao formato brasileiro (dd/mm/yyyy).

Visualizações no Dashboard

Vendas por País: mostra os países que mais venderam.

Lucro por Segmento: mostra quais segmentos são mais lucrativos.

Evolução das Vendas: exibe a variação de vendas ao longo do tempo.

Lucro por Produto: mostra os produtos mais lucrativos.

▶️ Como executar o projeto

Certifique-se de que o arquivo MS_Financial Sample.csv está na mesma pasta que o app.py.

No terminal, execute:

streamlit run app.py

O navegador abrirá automaticamente com o link:

http://localhost:8501

🧼 Tratamento de Erros

O projeto inclui um tratamento especial para limpar os dados antes da análise, lidando com:

Símbolos como $

Números formatados com . e ,

Strings vazias ou com "-"

Isso garante que o app funcione sem travar, mesmo com dados inconsistentes.

👩‍💻 Desenvolvido por

Samantha Alves

