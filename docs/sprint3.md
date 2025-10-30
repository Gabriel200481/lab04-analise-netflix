# Sprint 3 (Lab04S03) — Análise Detalhada e Entrega Final

Foco: responder RQ4 (Duração e Classificação) e compilar o relatório final.

Arquivos de suporte gerados nesta sprint:
- `src/analysis_duration.py` — script que gera figuras (boxplot por rating para filmes e barras para duração de séries) e as salva em `assets/figures/`.
- `notebooks/04_analysis_duration.ipynb` — notebook que executa o script e exibe as figuras.
- `docs/report_template.md` — template do relatório final em Markdown (pode ser convertido para .docx/.pdf via Pandoc ou exportado manualmente).

1) Página 4 – "Análise de Duração e Classificação" (RQ4)
- Visual 1 (Duração de Filmes): Box Plot
  - Eixo X: `rating` (classificação)
  - Eixo Y: `duration_value` (apenas onde `duration_unit == 'min'`)
  - Observação: o script remove valores nulos e outliers triviais para melhor leitura (mas preserva a distribuição)
  - Saída: `assets/figures/boxplot_duration_by_rating.png`

- Visual 2 (Duração de Séries): Bar Chart
  - Filtrar onde `duration_unit` != 'min' (ex.: Season)
  - Agrupar por `duration_value` (ex.: 1,2,3) e contar títulos
  - Ordenar por contagem decrescente
  - Saída: `assets/figures/bar_duration_series.png`

2) Relatório final
- Template: `docs/report_template.md` (conteúdo e espaços para inserir figuras exportadas do Power BI e as figuras geradas pelo script Python)
- Recomenda-se exportar imagens de alta qualidade (PNG) do Power BI para inserir no relatório.
- Para gerar PDF final a partir do Markdown, use o Pandoc (ou exporte manualmente do Word/Google Docs):

  Exemplo (se tiver pandoc instalado):

  ```bat
  pandoc docs\report_template.md -o dashboard_netflix.pdf --pdf-engine=xelatex
  ```

3) Como rodar localmente
- Ative o venv e instale dependências (se necessário):

```bat
call venv\Scripts\activate.bat
python -m pip install -r requirements.txt
```

- Gere as figuras:

```bat
python src\analysis_duration.py
```

