r"""
Gerar figuras para a Sprint 3 (RQ4):
- Boxplot de duração (filmes) por rating
- Bar chart de durações de séries (ex.: 1 Season, 2 Seasons)

Saídas (PNG): assets/figures/boxplot_duration_by_rating.png
                 assets/figures/bar_duration_series.png

Uso: python src\analysis_duration.py
"""

import os
import sys
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(ROOT, 'data')
FIG_DIR = os.path.join(ROOT, 'assets', 'figures')
INPUT_CANDIDATES = [
    os.path.join(DATA_DIR, 'netflix_tratado_final.csv'),
    os.path.join(DATA_DIR, 'netflix_titles_CLEANED.csv'),
]

os.makedirs(FIG_DIR, exist_ok=True)


def find_input():
    for p in INPUT_CANDIDATES:
        if os.path.exists(p):
            return p
    return None


def load_df(path):
    print('Lendo', path)
    return pd.read_csv(path)


def boxplot_duration_by_rating(df):
    col_dur = 'duration_value' if 'duration_value' in df.columns else 'duration'
    col_unit = 'duration_unit' if 'duration_unit' in df.columns else None
    rating_col = 'rating' if 'rating' in df.columns else None

    if col_unit is None or rating_col is None or col_dur not in df.columns:
        print('Colunas necessárias para boxplot nao encontradas (expected: duration_value, duration_unit, rating)')
        return None

    df_films = df[(df[col_unit] == 'min') & df[col_dur].notna()]
    df_films = df_films.copy()
    df_films.loc[:, col_dur] = pd.to_numeric(df_films[col_dur], errors='coerce')
    df_films = df_films[df_films[col_dur].notna()]

    plt.figure(figsize=(12,8))
    gb = df_films.groupby('rating')[col_dur].apply(lambda s: s.dropna().tolist())
    labels = list(gb.index)
    data = [gb[label] for label in labels]
    if len(data) == 0:
        print('Nenhum dado válido para boxplot')
        return None
    plt.boxplot(data)
    plt.xticks(range(1, len(labels) + 1), labels, rotation=45)
    plt.xlabel('Rating')
    plt.ylabel('Duração (minutos)')
    plt.title('Distribuição da duração dos filmes por rating')
    out = os.path.join(FIG_DIR, 'boxplot_duration_by_rating.png')
    plt.tight_layout()
    plt.savefig(out, dpi=300)
    plt.close()
    print('Gerado:', out)
    return out


def bar_duration_series(df):
    col_dur = 'duration_value' if 'duration_value' in df.columns else 'duration'
    col_unit = 'duration_unit' if 'duration_unit' in df.columns else None
    type_col = 'type' if 'type' in df.columns else None

    if col_unit is None or col_dur not in df.columns:
        print('Colunas necessárias para bar chart de series nao encontradas (expected: duration_value, duration_unit)')
        return None

    df_series = df[df[col_unit] != 'min']
    df_series = df_series.copy()
    df_series.loc[:, col_dur] = pd.to_numeric(df_series[col_dur], errors='coerce')
    df_series = df_series[df_series[col_dur].notna()]

    counts = df_series.groupby(col_dur).size().reset_index(name='title_count')
    counts = counts.sort_values('title_count', ascending=False)

    plt.figure(figsize=(10,6))
    y_labels = counts[col_dur].astype(str)
    x_vals = counts['title_count']
    if len(x_vals) == 0:
        print('Nenhum dado válido para bar chart de series')
        return None
    plt.barh(y_labels, x_vals, color='C0')
    plt.xlabel('Contagem de Títulos')
    plt.ylabel('Duração (seasons)')
    plt.title('Duração mais comum em séries (em seasons)')
    out = os.path.join(FIG_DIR, 'bar_duration_series.png')
    plt.tight_layout()
    plt.savefig(out, dpi=300)
    plt.close()
    print('Gerado:', out)
    return out


def main():
    inp = find_input()
    if inp is None:
        print('Arquivo de entrada nao encontrado. Coloque data\\netflix_tratado_final.csv ou rode src/preprocess.py')
        sys.exit(1)
    df = load_df(inp)
    a = boxplot_duration_by_rating(df)
    b = bar_duration_series(df)
    print('Concluido. Figuras geradas (se possiveis).')


if __name__ == '__main__':
    main()
