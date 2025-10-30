r"""
Preprocessamento do dataset Netflix

Entrada esperada: data/netflix_titles_CLEANED.csv
Saída: data/netflix_tratado_final.csv

O script realiza:
- leitura do CSV (detecta nome de coluna comum para países/genres/directors)
- conversão de date_added para datetime e criação de added_year, added_month
- tratamento da coluna duration em duration_value e duration_unit
- tratamento de nulos para countries/listed_in/directors
- split + explode para countries, listed_in e directors (gera uma linha por combinação)
- gravação do CSV final

Uso (executar a partir da raiz do projeto):
    python src\preprocess.py

"""

import os
import re
import sys
import pandas as pd

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(ROOT, 'data')
INPUT_CSV_CANDIDATES = [
    os.path.join(DATA_DIR, 'netflix_titles_CLEANED.csv'),
    os.path.join(ROOT, 'netflix_titles_CLEANED.csv'),
]
OUTPUT_CSV = os.path.join(DATA_DIR, 'netflix_tratado_final.csv')


def find_input_csv():
    for p in INPUT_CSV_CANDIDATES:
        if os.path.exists(p):
            return p
    return None


def choose_column(df, candidates):
    for c in candidates:
        if c in df.columns:
            return c
    return None


def parse_duration(value):
    """Retorna (value:int or None, unit:str or None)."""
    if pd.isna(value):
        return (None, None)
    s = str(value).strip()
    if s == '':
        return (None, None)
    # Ex: '90 min', '2 Seasons', '1 Season', '45 min'
    m = re.search(r"(?P<val>\d+)", s)
    u = None
    val = None
    if m:
        try:
            val = int(m.group('val'))
        except Exception:
            val = None
    # unit: check for 'min' or 'season'
    if 'min' in s.lower():
        u = 'min'
    elif 'season' in s.lower():
        u = 'Season'
    elif 'seasons' in s.lower():
        u = 'Season'
    else:
        # fallback: take last word
        parts = s.split()
        if len(parts) > 1:
            u = parts[-1]
    return (val, u)


def split_to_list(series):
    # turn NaN into 'Unknown' and then split on comma
    return series.fillna('Unknown').astype(str).str.split(r",\s*")


def preprocess(input_path, output_path, verbose=True):
    if verbose:
        print('Lendo:', input_path)
    df = pd.read_csv(input_path)
    if verbose:
        print('Linhas originais:', len(df))

    # detect common column names
    date_col = choose_column(df, ['date_added', 'dateAdded', 'Date Added'])
    duration_col = choose_column(df, ['duration', 'duration_str', 'Duration'])
    country_col = choose_column(df, ['country', 'countries', 'Country', 'Countries'])
    listed_col = choose_column(df, ['listed_in', 'listedIn', 'listed in', 'listed'])
    director_col = choose_column(df, ['director', 'directors', 'Director', 'Directors'])

    # 1) date_added -> datetime + added_year, added_month
    if date_col:
        df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
        df['added_year'] = df[date_col].dt.year
        df['added_month'] = df[date_col].dt.month
    else:
        if verbose:
            print('Coluna de data nao encontrada; pulando added_year/added_month')

    # Preserve/normalize release_year if present in original CSV (ano de lançamento)
    if 'release_year' in df.columns:
        # convert to numeric, keep NA if invalid
        df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce').astype('Int64')

    # 2) duration -> duration_value, duration_unit
    if duration_col:
        parsed = df[duration_col].apply(parse_duration)
        df['duration_value'] = parsed.apply(lambda x: x[0])
        df['duration_unit'] = parsed.apply(lambda x: x[1])
    else:
        if verbose:
            print('Coluna duration nao encontrada; pulando processamento de duration')
        df['duration_value'] = pd.NA
        df['duration_unit'] = pd.NA

    # 3) tratar nulos e preparar listas para explode
    if country_col:
        df['countries_list'] = split_to_list(df[country_col])
    else:
        df['countries_list'] = [['Unknown']] * len(df)

    if listed_col:
        df['listed_in_list'] = split_to_list(df[listed_col])
    else:
        df['listed_in_list'] = [['Unknown']] * len(df)

    if director_col:
        df['directors_list'] = split_to_list(df[director_col])
    else:
        df['directors_list'] = [['Unknown']] * len(df)

    # 4) explode: cria uma linha por combinacao de country, genre e director
    df_exploded = df.explode('countries_list')
    df_exploded = df_exploded.explode('listed_in_list')
    df_exploded = df_exploded.explode('directors_list')

    # opcional: renomear colunas de lista para nomes amigaveis
    df_exploded = df_exploded.rename(columns={
        'countries_list': 'country_exploded',
        'listed_in_list': 'genre_exploded',
        'directors_list': 'director_exploded'
    })

    if verbose:
        print('Linhas apos explode:', len(df_exploded))
        print('Salvando arquivo:', output_path)

    # salvar
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df_exploded.to_csv(output_path, index=False)
    if verbose:
        print('Pronto.')
    return df_exploded


if __name__ == '__main__':
    input_csv = find_input_csv()
    if input_csv is None:
        print('Arquivo de entrada nao encontrado. Coloque data\\netflix_titles_CLEANED.csv ou informe o caminho.')
        sys.exit(1)
    preprocess(input_csv, OUTPUT_CSV)
