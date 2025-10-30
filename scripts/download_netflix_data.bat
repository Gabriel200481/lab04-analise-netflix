@echo off
REM Uso: scripts\download_netflix_data.bat <URL>
REM Baixa o arquivo netflix_titles_CLEANED.csv para a pasta data\

if "%1"=="" (
  echo ERRO: informe a URL do arquivo como primeiro argumento.
  echo Ex: scripts\download_netflix_data.bat "https://exemplo.com/netflix_titles_CLEANED.csv"
  exit /b 1
)

set URL=%1
set OUTFILE=%~dp0..\data\netflix_titles_CLEANED.csv

echo Baixando %URL% para %OUTFILE% ...
powershell -NoProfile -Command "try { Invoke-WebRequest -Uri '%URL%' -OutFile '%OUTFILE%' -UseBasicParsing; Write-Host 'Download concluido.' } catch { Write-Host 'Erro ao baixar o arquivo:'; Write-Host $_; exit 1 }"

echo Pronto.
exit /b 0
