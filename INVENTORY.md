# INVENTORY — Lab04: Análise do Catálogo da Netflix

Este arquivo lista, de forma organizada, todos os artefatos gerados no repositório, incluindo código, scripts, dados, visualizações e documentos. Use-o como referência rápida para localizar outputs e funções principais.

> Gerado em: 2025-10-30

## Resumo executivo
- Pipeline completo implementado: ETL (preprocess) → canonicalização de países → agregações para Power BI → visualizações interativas (Plotly) → figuras estáticas (matplotlib) → relatório `.docx`.

## Código fonte (`src/`)
- `src/preprocess.py` — funções: `preprocess`, `parse_duration`. Gera `data/netflix_tratado_final.csv`.
- `src/standardize_countries.py` — funções: `normalize_name`, `standardize`. Gera `data/netflix_tratado_final_canonical.csv` e `data/country_aliases_mapping.csv`.
- `src/prepare_powerbi.py` — função: `prepare`. Gera CSVs agregados para Power BI.
- `src/generate_plotly.py` — funções para criar HTML interativos: `top10_countries`, `country_genre_matrix`, `annual_trends`, `heatmap_month_year`.
- `src/analysis_duration.py` — funções: `boxplot_duration_by_rating`, `bar_duration_series`. Gera PNGs em `assets/figures/` (backend `Agg`).
- `src/generate_report_docx.py` — função: `generate`. Gera `output/dashboard_netflix.docx`.
- `src/main.py` (opcional) — runner/entry-point que orquestra a pipeline (placeholder).

## Scripts (`scripts/`)
- `scripts/setup_env.bat` — cria venv e instala dependências do `requirements.txt` (Windows).
- `scripts/download_netflix_data.bat` — helper para baixar/colocar o CSV na pasta `data/`.
- `scripts/check_outputs.py` — checa existência e tamanhos dos artefatos gerados.

## Dados (`data/`)
- `data/netflix_titles_CLEANED.csv` — input original (colocado manualmente pelo usuário).
- `data/netflix_tratado_final.csv` — resultado do `preprocess.py` (exploded) — ~25.895 linhas reportadas.
- `data/netflix_tratado_final_canonical.csv` — pós-canonicalização de países.
- `data/country_aliases_mapping.csv` — mapeamento alias → canonical (revisável manualmente).
- Agregados para Power BI gerados por `prepare_powerbi.py`:
  - `data/country_counts.csv`
  - `data/top10_countries.csv`
  - `data/country_genre_counts.csv`
  - `data/annual_trends.csv`
  - `data/heatmap_month_year.csv`

## Visualizações estáticas (`assets/figures/`)
- `boxplot_duration_by_rating.png` — boxplot duração por rating (~220 KB).
- `bar_duration_series.png` — série temporal da duração média/mediana (~100 KB).

## Visualizações interativas (`assets/interactive/`)
- `top10_countries.html` — Plotly interativo (top 10 países) (~4–5 MB).
- `country_genre_matrix.html` — matriz interativa país x gênero.
- `annual_trends.html` — tendências anuais interativas.
- `heatmap_month_year.html` — heatmap mês x ano interativo.

## Relatórios e Notebooks
- `output/dashboard_netflix.docx` — relatório final gerado (~288 KB).
- Notebooks (guias e exemplos):
  - `notebooks/01_setup.ipynb`
  - `notebooks/02_preprocessing.ipynb`
  - `notebooks/03_prepare_powerbi.ipynb`
  - `notebooks/04_analysis_duration.ipynb`
  - `notebooks/06_powerbi_steps.ipynb`

## Testes (`tests/`)
- `tests/test_all_smoke.py` — smoke tests.
- `tests/test_more.py` — casos adicionais.
Status: testes executados e passaram (7 passed).

## Configurações e metadata
- `requirements.txt` — dependências do projeto (pandas, matplotlib, plotly, python-docx, pycountry, kaleido, pytest, etc.).
- `.vscode/settings.json` — configurações do workspace (aponta venv e `python.analysis.extraPaths`).
- `.github/workflows/` — workflow CI (templates básicos).
- `README.md`, `README_pt.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `LICENSE`, `.gitignore`, `.editorconfig`.

## Funções / componentes chave (mapa rápido)
- `parse_duration` — extrai valor e unidade de string de duração (min/season).
- `normalize_name` — canonicaliza nomes de países com `pycountry` + `COMMON_MAP`.
- `prepare` — cria agregados CSV para Power BI.
- `*plotly*` — gera HTMLs interativos.
- `boxplot_duration_by_rating` / `bar_duration_series` — figuras PNG para o relatório.
- `generate` (docx) — monta o relatório final `.docx`.

## Observações e recomendações
- `data/country_aliases_mapping.csv` deve ser revisado e ajustado para corrigir aliases incomuns antes da publicação do dashboard final.
- A conversão DOCX → PDF não está automatizada (requer Word/LibreOffice/Pandoc). Para um PDF rápido, gere a partir dos PNGs (podemos automatizar isso se desejar).
- Em datasets muito maiores, considere processar com chunks ou usar Dask/Polars para performance.

---

Se quiser, faço um commit com este `INVENTORY.md` e também posso gerar um `output/dashboard_netflix.pdf` simples a partir dos PNGs (opção rápida), ou tentar converter o DOCX para PDF se tiver Word instalado. Diga qual ação prefere em seguida.
