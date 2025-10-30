# Setup do ambiente

Este arquivo deve conter os passos para preparar o ambiente de desenvolvimento:

(Preencha de acordo com a stack escolhida.)
# Setup do ambiente

Este arquivo descreve como preparar o ambiente de desenvolvimento para este projeto (Windows, cmd.exe).

## 1) Dependências
- Python 3.11+ (foi usado Python 3.13 durante o desenvolvimento). Verifique com:

```cmd
python --version
```

- Ferramentas opcionais:
	- Microsoft Visual C++ Build Tools (se alguma dependência precisar ser compilada).
	- Microsoft Word / LibreOffice / Pandoc (caso queira converter DOCX → PDF automaticamente).

## 2) Criar e ativar virtualenv (Windows - cmd.exe)

No diretório do projeto (ex.: `d:\Desktop\labDeChatisse`) execute:

```cmd
python -m venv venv
venv\Scripts\activate
```

Se usar PowerShell execute `venv\Scripts\Activate.ps1`.

## 3) Instalar dependências

Com o venv ativado:

```cmd
pip install --upgrade pip
pip install -r requirements.txt
```

`requirements.txt` inclui: pandas, matplotlib, plotly, python-docx, pycountry, kaleido, pytest, pillow (opcional), entre outros.

## 4) Verificações rápidas

```cmd
pip show pandas matplotlib plotly python-docx pycountry pytest
```

## 5) Como rodar a pipeline (sequência recomendada)

Execute os scripts em sequência a partir da raiz do projeto (venv ativado):

```cmd
python src\preprocess.py
python src\standardize_countries.py
python src\prepare_powerbi.py
python src\generate_plotly.py
python src\analysis_duration.py
python src\generate_report_docx.py
python scripts\check_outputs.py
```

Se algum passo falhar por arquivo ausente, volte para o passo anterior (ex.: rode `preprocess.py` antes de `prepare_powerbi.py`).

## 6) Rodar testes

Instale pytest (se ainda não instalado) e execute:

```cmd
pip install pytest
pytest -q
```

Os testes do repositório são rápidos (smoke + alguns casos). Na verificação final foram executados com sucesso (7 passed).

## 7) Gerar PDF simples a partir das PNGs (opcional)

Exemplo rápido usando Pillow (gera `output\dashboard_netflix.pdf` a partir das imagens em `assets/figures/`):

```cmd
pip install pillow
python - <<EOF
from PIL import Image
imgs = [Image.open(p) for p in [r"assets/figures/boxplot_duration_by_rating.png", r"assets/figures/bar_duration_series.png"]]
imgs[0].save(r"output\dashboard_netflix.pdf", save_all=True, append_images=imgs[1:])
EOF
```

## 8) Converter DOCX → PDF (opcional)

Conversão automática mais polida geralmente requer Microsoft Word (Windows). Exemplo com `docx2pdf`:

```cmd
pip install docx2pdf
python - <<EOF
from docx2pdf import convert
convert(r"output\dashboard_netflix.docx", r"output\dashboard_netflix.pdf")
EOF
```

Se não tiver o Word, use LibreOffice / Pandoc para conversões alternativas.

## 9) Troubleshooting rápido
- Matplotlib/Tk: os scripts usam `Agg` (headless) — não precisa de Tk/Tcl para gerar PNGs.
- Pylance/static analysis: avisos sobre objetos dinâmicos (`pycountry`) foram atenuados com `getattr`; se persistirem, verifique `.vscode/settings.json` e o Python interpreter selecionado.
- Nomes de países no Power BI: verifique `data/country_aliases_mapping.csv` para ajustar aliases antes de importar no Power BI.

## 10) Scripts úteis / atalhos

```cmd
# ativar o ambiente
venv\Scripts\activate

# instalar requisitos
pip install -r requirements.txt

# rodar pipeline completa
python src\preprocess.py && python src\standardize_countries.py && python src\prepare_powerbi.py && python src\generate_plotly.py && python src\analysis_duration.py && python src\generate_report_docx.py

# rodar testes
pytest -q

# checar outputs
python scripts\check_outputs.py
```

Se quiser, eu posso criar um `scripts\run_all.bat` que automatiza a sequência e opcionalmente gera o PDF simples. Diga se deseja que eu o crie.
