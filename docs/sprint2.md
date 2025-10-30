# Sprint 2 (Lab04S02) — Análises Comparativas e Temporais

Foco: responder RQ2 (Geografia) e RQ3 (Sazonalidade/Lançamento) e preparar os dados para o Power BI.

Arquivos gerados (pré-requisito): `data/netflix_tratado_final.csv` (saída do Sprint 1).

1) Script de preparação para Power BI
- Arquivo: `src/prepare_powerbi.py`
- Objetivo: gerar CSVs resumidos para facilitar a montagem dos visuais no Power BI.
- Saídas (salvas em `data/`):
  - `country_counts.csv` — contagem de títulos por país (campo `country_exploded`).
  - `top10_countries.csv` — top 10 países por contagem de títulos.
  - `country_genre_counts.csv` — contagem por país x gênero (linha por país/genre) — útil para matriz/stacked 100%.
  - `annual_trends.csv` — contagem por `added_year` e `type` (útil para gráfico de linhas).
  - `heatmap_month_year.csv` — contagem por `added_year` x `added_month` (útil para heatmap de sazonalidade).

2) Página 2: "Estratégia de Produção Global" (RQ2)
- Visual 1 — Top 10 Países
  - Visual: Barras Horizontais (Horizontal Bar Chart)
  - Eixo Y: `country_exploded` (ou use `country_counts.csv`)
  - Eixo X: Contagem de Títulos
  - Aplicar filtro Top N = 10

- Visual 2 — Especialização de Gênero (por país Top 10)
  - Visual: Matriz ou Stacked Bar Chart 100%
  - Linhas: `country_exploded` (Top 10)
  - Colunas / Legenda: `genre_exploded`
  - Valores: contagem de títulos (`country_genre_counts.csv`)

- Visual 3 — Mapa Coroplético (Mapa de calor geográfico)
  - Localização: `country_exploded` (Power BI reconhece nomes de países; ajuste campo de localização para "Country/Region")
  - Saturação da cor: contagem de títulos (`country_counts.csv`)

3) Página 3: "Estratégia de Lançamento" (RQ3)
- Visual 1 — Tendência Anual
  - Visual: Gráfico de Linhas
  - Eixo X: `added_year`
  - Eixo Y: Contagem de Títulos
  - Legenda: `type` (Movie / TV Show)
  - Fonte: `annual_trends.csv`

- Visual 2 — Sazonalidade (Heatmap)
  - Visual: Matrix with conditional formatting or heatmap visual
  - Eixo X: `added_month` (1-12)
  - Eixo Y: `added_year`
  - Saturação da cor: contagem de títulos (`heatmap_month_year.csv`)

4) O que apresentar na aula (Lab04S02)
- Mostrar Página 2: explicar top países, especialização de gêneros e destacar insights do mapa.
- Mostrar Página 3: tempos de adição por ano, evidências de sazonalidade por mês/ano.

5) Observações técnicas
- Se os nomes de países não forem reconhecidos pelo Power BI, padronize (ex.: "United States" vs "USA"). Eu posso ajudar a mapear aliases se precisar.
- O script `src/prepare_powerbi.py` tenta localizar `data/netflix_tratado_final.csv`. Caso não exista, rode primeiro o `src/preprocess.py` do Sprint 1.

Próximo passo sugerido
- Gerar os CSVs com `src/prepare_powerbi.py` e abrir o Power BI, carregar os CSVs para montar as Páginas 2 e 3.
- Se preferir, posso criar um notebook com exemplos de gráficos em Python (matplotlib/plotly) que espelhem os visuais do Power BI como rascunho.
