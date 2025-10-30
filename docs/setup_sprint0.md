# Setup do ambiente (Sprint 0)

Este documento descreve os passos para deixar o ambiente pronto no Windows (cmd.exe) antes da Sprint 1.

1) Instalar ferramentas recomendadas
 - Python: instale via Anaconda (https://www.anaconda.com) ou do site oficial (https://www.python.org/downloads/). Se usar o instalador do python.org, marque "Add Python to PATH".
 - Power BI Desktop (opcional para análises/visualizações): https://powerbi.microsoft.com/desktop

2) Preparar a pasta do projeto
 - A estrutura do repositório já contém: `src/`, `notebooks/`, `data/`, `scripts/`, `requirements.txt`.

3) Criar e ativar ambiente Python (cmd.exe)
 - Abra o "Command Prompt" (cmd.exe) na raiz do projeto.
 - Rode o script de setup:

```
scripts\setup_env.bat
```

O script criará um virtual environment em `venv\`, instalará dependências (pandas, jupyter) e exibirá instruções para iniciar o Jupyter Notebook.

Se preferir executar manualmente:

```
python -m venv venv
call venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

4) Abrir Jupyter Notebook

Com o ambiente ativado, rode:

```
jupyter notebook
```

Abra `notebooks/01_setup.ipynb` e execute as células para verificar versões e arquivos.

5) Baixar os dados (netflix_titles_CLEANED.csv)

 - Coloque o arquivo `netflix_titles_CLEANED.csv` dentro da pasta `data/`.
 - Se tiver uma URL direta, use:

```
scripts\download_netflix_data.bat "https://exemplo.com/netflix_titles_CLEANED.csv"
```

O script salvará o arquivo em `data\netflix_titles_CLEANED.csv`.

6) Verificação rápida

 - No notebook `notebooks/01_setup.ipynb` execute as células — ele mostrará a versão do Python, a versão do pandas e indicará se `data/netflix_titles_CLEANED.csv` existe.
