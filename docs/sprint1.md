# Sprint 1 (Lab04S01) — Pré-Processamento e Caracterização

Objetivo: limpar o dataset e preparar a base para o dashboard (Power BI).

1) Script Python (preprocessamento)
- Arquivo: `src/preprocess.py`
- Entrada esperada: `data/netflix_titles_CLEANED.csv`
- Saída: `data/netflix_tratado_final.csv` (linhas explodidas por `country`, `genre` e `director`)

Principais passos realizados no script:
- Leitura do CSV original (procura em `data/` automaticamente).
- Conversão de `date_added` para datetime e criação das colunas `added_year` e `added_month`.
- Tratamento da coluna `duration`: criação de `duration_value` (numérico) e `duration_unit` (ex.: `min`, `Season`).
- Tratamento de valores nulos em `country`/`listed_in`/`director` (substitui por `Unknown` antes do split).
- Separação (`.str.split(', ')`) e `.explode()` para `country`, `listed_in` (gêneros) e `director` — gera uma linha por combinação.
- Exportação do CSV limpo em `data/netflix_tratado_final.csv`.

2) Notebook de execução
- Arquivo: `notebooks/02_preprocessing.ipynb` — notebook que chama o script e explica as etapas.

3) Power BI — Página 1: Caracterização e Evolução do Catálogo
- Carregar: `data/netflix_tratado_final.csv` no Power BI.
- Página: "Caracterização e Evolução do Catálogo"
  - KPIs (Cartões):
    - Contagem total de títulos (use a contagem de `show_id` ou `title`).
    - % de Filmes (type == 'Movie').
    - % de Séries (type == 'TV Show' / 'Series').
  - Visualização (RQ1): Gráfico de Áreas Empilhadas
    - Eixo X: `release_year`
    - Eixo Y: contagem de títulos
    - Legenda/pilha: `type` (Filme / Série)
  - Filtro (Slicer): `release_year` (permite navegar pela evolução temporal)

4) O que apresentar na aula
- Mostrar o script `src/preprocess.py` e explicar decisões:
  - Por que explodimos `country`/`listed_in`/`director` (contagens corretas e análises por entidade).
  - Como tratamos `duration` (separando valor e unidade) e datas (added_year / added_month).
- Demonstrar o dashboard Power BI com a Página 1 pronta (KPIs + RQ1 + filtro).
