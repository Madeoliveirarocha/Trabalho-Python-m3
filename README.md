📘 Atividades Práticas – Numpy, Pandas e Matplotlib

Este repositório contém as três atividades práticas da disciplina, envolvendo operações com NumPy, manipulação de dados com Pandas e visualização de dados com Matplotlib.
As atividades exploram desde operações matemáticas de baixo nível até processamento e visualização de dados meteorológicos reais.

🟦 Atividade Prática 1 – Operações com NumPy
🎯 Objetivo

Comparar o desempenho entre uma multiplicação de matrizes feita apenas com Python nativo e a multiplicação feita com NumPy, medindo o tempo de execução de cada abordagem.

✔️ Etapas

Implementar uma função em Python puro que realiza multiplicação de matrizes (sem NumPy).

Criar duas matrizes 10.000 x 10.000 usando listas nativas.

Medir o tempo de execução da função criada usando a biblioteca time.

Converter as matrizes para arrays NumPy.

Multiplicar utilizando numpy.matmul e medir o tempo de execução.

Comparar o desempenho entre a solução nativa e o NumPy.

📝 Resultados esperados

Demonstração clara da diferença de performance entre Python nativo e NumPy.

Entendimento da vantagem de operações vetorizadas otimizadas.

🟩 Atividade Prática 2 – Manipulação de Dados com Pandas
🎯 Objetivo

Ler, processar e analisar dados meteorológicos reais usando Pandas.

📄 Dataset utilizado

Arquivo CSV disponível em:
https://github.com/Malekai/Downloading-Data/blob/master/sitka_weather_2014.csv

✔️ Etapas

Criar um DataFrame a partir do arquivo CSV.

Identificar as colunas de:

Datas

Temperaturas Máximas

Temperaturas Mínimas

Extrair esses dados utilizando métodos do Pandas.

Calcular estatísticas descritivas básicas das temperaturas:

Mínimo

Máximo

Média

📝 Resultados esperados

Compreensão do uso básico de DataFrames.

Análise estatística simples de dados numéricos.

🟥 Atividade Prática 3 – Visualização com Matplotlib
🎯 Objetivo

Criar um gráfico de linhas com as temperaturas máximas e mínimas obtidas na atividade anterior.

✔️ Etapas

Utilizar os dados extraídos na Atividade 2.

Gerar um gráfico único mostrando:

Linha das temperaturas máximas

Linha das temperaturas mínimas

Adicionar título, legenda e nomear eixos adequadamente.

Formatar datas no eixo X para melhorar a visualização.

📝 Resultados esperados

Visualização clara da variação de temperatura ao longo do ano.

Familiaridade com matplotlib e manipulação de datas no eixo X.

📂 Estrutura sugerida do repositório
📁 projeto-meteorologia
│
├── atividade_1/
│   ├── matriz_python.py
│   ├── matriz_numpy.py
│   └── resultados.md
│
├── atividade_2/
│   ├── analise_pandas.py
│   └── sitka_weather_2014.csv  (opcional)
│
├── atividade_3/
│   ├── grafico_temperaturas.py
│   └── grafico.png
│
└── README.md

🚀 Como executar
Atividade 1
python atividade_1/matriz_python.py
python atividade_1/matriz_numpy.py

Atividade 2
python atividade_2/analise_pandas.py

Atividade 3
python atividade_3/grafico_temperaturas.py

📌 Tecnologias utilizadas

Python 3

NumPy

Pandas

Matplotlib