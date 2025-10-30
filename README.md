# Análise da Estratégia de Conteúdo da Netflix (LAB04)

<p align="center">
  <img src="https://img.shields.io/badge/Linguagem-Python-3776AB?logo=python" alt="Linguagem Python">
  <img src="https://img.shields.io/badge/Ferramenta-Power BI-F2C811?logo=powerbi" alt="Ferramenta Power BI">
  <img src="https://img.shields.io/badge/Disciplina-Experimentação de Software-brightgreen" alt="Disciplina">
</p>

## 📖 Descrição do Projeto

Este repositório contém os scripts Python, o dashboard e os artefatos desenvolvidos como parte do **LAB04** ("Trabalho Alternativo") da disciplina *Laboratório de Experimentação de Software*.

O objetivo principal é realizar uma análise de Business Intelligence (BI) sobre o catálogo público da Netflix (obtido do Kaggle). Para isso, o projeto implementa um **pipeline de ETL (Extração, Transformação e Carga)** robusto e reprodutível em Python (Pandas) para limpar, processar e pré-agregar os dados.

Os dados tratados alimentam um dashboard interativo no **Microsoft Power BI**, que é utilizado para responder a **4 Questões de Pesquisa (RQs)** sobre a estratégia de conteúdo da Netflix, focando em evolução, distribuição geográfica, sazonalidade e formatos de duração.

O projeto completo, incluindo a discussão dos *insights*, está documentado no `relatorio_final.md`.

---

## 🗂️ Estrutura do Repositório e Ficheiros

- **`src/`**: Contém os scripts Python do pipeline de ETL.
  - **`preprocess.py`**: Script principal que limpa os dados brutos, trata múltiplos valores (ex: `country`, `genre`) e extrai dados complexos (ex: `duration`).
  - **`prepare_powerbi.py`**: Script que gera os CSVs pré-agregados para otimizar a performance do dashboard.
- **`data/`**: Diretório para os arquivos de dados.
  - **`netflix_titles_CLEANED.csv`**: O *input* de dados brutos (deve ser baixado do Kaggle).
  - **`netflix_tratado_final.csv`**: O *output* principal do `preprocess.py`, com dados limpos e "explodidos".
  - **`annual_trends.csv`**, **`top10_countries.csv`**, etc.: CSVs pré-agregados, prontos para o BI.
- **`dashboard.pbix`**: O arquivo-fonte do dashboard final, para ser aberto no Power BI Desktop.
- **`relatorio_final.md`**: O relatório final completo com a metodologia, análise dos resultados, discussão estratégica e o apêndice técnico.

---

## ✨ Funcionalidades do Pipeline

- Limpeza de dados brutos do Kaggle, tratando valores ausentes e corrigindo tipos de dados.
- Extração e parse de colunas complexas (ex: `duration` é separado em `duration_value` [numérico] e `duration_unit` [categórico]).
- Tratamento de colunas com múltiplos valores (como `country` e `listed_in`) através da técnica de `explode()`, permitindo análises granulares precisas.
- Geração de CSVs pré-agregados para alimentar o Power BI, garantindo alta performance no dashboard (ex: `annual_trends.csv`, `heatmap_month_year.csv`).
- Toda a metodologia de limpeza é documentada e reprodutível através dos scripts Python.

---

## 🧾 Colunas do CSV Processado (`netflix_tratado_final.csv`)

- **show_id**: ID único do título.
- **type**: 'Movie' ou 'TV Show'.
- **title**: Título.
- **release_year**: Ano de lançamento original.
- **rating**: Classificação etária (ex: 'PG-13', 'TV-MA').
- **... (outras colunas originais)**
- **duration_value**: (Nova) O valor numérico da duração (ex: 90, 2).
- **duration_unit**: (Nova) A unidade da duração (ex: 'min', 'Season').
- **added_year**: (Nova) O ano em que o título foi adicionado à Netflix.
- **added_month**: (Nova) O mês em que o título foi adicionado.
- **country_exploded**: (Nova) Coluna "explodida" contendo um único país por linha.
- **genre_exploded**: (Nova) Coluna "explodida" contendo um único gênero por linha.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

- [Python 3.10+](https://www.python.org/)
- Bibliotecas Python listadas no `requirements.txt` (principalmente `pandas`).
- [Microsoft Power BI Desktop](https://powerbi.microsoft.com/pt-br/desktop/) (para visualizar o dashboard).

### Passos para Reproduzir a Análise

1.  **Clone o repositório:**
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO]
    cd [NOME_DA_PASTA]
    ```

2.  **Crie e ative o ambiente virtual:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Adicione os dados brutos:**
    - Baixe o dataset "Netflix Movies and TV Shows" do Kaggle.
    - Renomeie-o para `netflix_titles_CLEANED.csv` e coloque-o dentro da pasta `data/`.

5.  **Execute o pipeline de ETL (Python):**
    ```bash
    python src/preprocess.py
    python src/prepare_powerbi.py
    ```
    (Ou execute outros scripts em `src/` conforme documentado no `Apêndice A` do relatório).

6.  **Visualize o Dashboard:**
    - Abra o arquivo `dashboard.pbix` com o Power BI Desktop.
    - Se solicitado, clique em "Atualizar" na barra amarela para que o Power BI recarregue os dados dos CSVs que você acabou de gerar.

---

## 📈 Relatório Técnico (Resumo dos Resultados)

A análise dos dados, detalhada no `relatorio_final.md`, investigou 4 Questões de Pesquisa (RQs) para desvendar a estratégia de conteúdo da Netflix.

| Questão de Pesquisa (RQ) | Métrica(s) Analisada(s) |
| :--- | :--- |
| **RQ01: Evolução** | `added_year`, `type` |
| **RQ02: Geografia** | `country_exploded`, `genre_exploded` |
| **RQ03: Sazonalidade** | `added_year`, `added_month` |
| **RQ04: Formato** | `duration_value`, `duration_unit`, `rating` |

O relatório completo, com a discussão detalhada dos *insights* (incluindo a mudança para Séries, a estratégia "glocal" e o dominante modelo de "1 Temporada"), a metodologia de depuração de dados no Power BI e o apêndice técnico completo, pode ser encontrado no arquivo `relatorio_final.md`.

---

## 📝 Licença

Este projeto está sob a licença **MIT**.

---

## 👥 Autores

- Gabriel Afonso Infante Vieira
- Rafael de Paiva Gomes
- Rafaella Cristina de Sousa Sacramento

---

<p align="center"><em>Projeto desenvolvido para a disciplina de Laboratório de Experimentação de Software - PUC Minas</em></p>
