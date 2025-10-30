echo "Execute comandos para criar venv, instalar dependências e configurar variáveis."
@echo off
REM -----------------------------------------------------------------
REM Script: scripts\setup_env.bat
REM Objetivo: criar/ativar um ambiente virtual Python e instalar dependências
REM Uso: abra cmd.exe na raiz do projeto e execute: scripts\setup_env.bat
REM Observação: este script cria uma venv local em .\venv
REM -----------------------------------------------------------------

echo ================================
echo Preparando ambiente Python
echo ================================

REM 1) Verifica se python está disponível
python --version >nul 2>&1
if errorlevel 1 (
	echo Python nao encontrado no PATH. Instale o Python (Anaconda ou python.org) e repita.
	pause
	exit /b 1
)

REM 2) Criar virtualenv
if not exist venv (
	echo Criando virtual environment em .\venv ...
	python -m venv venv
) else (
	echo Virtual environment ja existe: .\venv
)

REM 3) Ativar venv (cmd.exe)
echo Ativando virtual environment...
call venv\Scripts\activate.bat

REM 4) Atualizar pip e instalar dependências do requirements.txt
if exist requirements.txt (
	echo Instalando dependencias de requirements.txt ...
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt
) else (
	echo requirements.txt nao encontrado. Instalando pandas e jupyter por padrao...
	python -m pip install --upgrade pip
	python -m pip install pandas jupyter
)

echo
echo Ambiente pronto. Para abrir um Jupyter Notebook rode:
echo    jupyter notebook
echo Ou rode o notebook de verificacao: notebooks\01_setup.ipynb

echo Para baixar os dados (se possuir uma URL):
echo    scripts\download_netflix_data.bat <URL>

pause
