# Projeto / Repositório

Este repositório foi inicializado com uma estrutura profissional para receber o trabalho.

## Estrutura criada
- src/ - código-fonte do projeto
- tests/ - testes automatizados
- docs/ - documentação do projeto (guides, reference)
- .github/ - templates e workflows
- scripts/ - scripts de automação e setup
- assets/ - imagens e recursos
- examples/ - exemplos e demos

## Como usar
1. Personalize o `README_pt.md` e `docs/setup.md` com informações do seu projeto.
2. Adicione o código em `src/` e testes em `tests/`.

---

(Arquivo gerado automaticamente como placeholder)

## Notas específicas do Lab04 - Análise do Catálogo da Netflix

1) `release_year` vs `added_year`

- O preprocess (`src/preprocess.py`) agora preserva e normaliza a coluna `release_year` (ano de lançamento) se ela existir no CSV original. O pipeline também gera `added_year`/`added_month` (ano/mês de adição ao catálogo). Use `release_year` quando quiser analisar tendências por ano de lançamento; use `added_year` para tendências de adição ao catálogo.

2) Preparando o Power BI

- Um notebook com passos e dicas para montar as páginas do Power BI foi adicionado em `notebooks/06_powerbi_steps.ipynb`.
- Fluxo recomendado:
	- Rode: `python src\preprocess.py` para gerar `data/netflix_tratado_final.csv` (linha por país/gênero/diretor).
	- Rode: `python src\prepare_powerbi.py` para gerar agregados (top10, heatmap, annual trends).
	- Importe `data/netflix_tratado_final.csv` e/ou os CSVs agregados no Power BI Desktop.

3) Entrega rápida (PDF composto)

- Se precisar de uma entrega rápida sem abrir o Power BI, use o script que será criado para concatenar as imagens geradas (`assets/figures/`) e gerar `output/dashboard_netflix.pdf` — contate-me para gerar este PDF automaticamente.
