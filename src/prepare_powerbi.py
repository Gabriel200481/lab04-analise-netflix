import os
import sys
import pandas as pd

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(ROOT, 'data')
INPUT_CANDIDATES = [
    os.path.join(DATA_DIR, 'netflix_tratado_final.csv'),
    os.path.join(DATA_DIR, 'netflix_titles_CLEANED.csv'),
]


def find_input():
    for p in INPUT_CANDIDATES:
        if os.path.exists(p):
            return p
    return None


def prepare():
    inp = find_input()
    if inp is None:
        print('Arquivo de entrada nao encontrado. Execute o preprocess.py primeiro ou coloque netflix_tratado_final.csv em data/.')
        sys.exit(1)
    print('Lendo:', inp)
    df = pd.read_csv(inp)
    print('Linhas lidas:', len(df))

    country_col = 'country_exploded' if 'country_exploded' in df.columns else ('country' if 'country' in df.columns else None)
    if country_col is None:
        print('Coluna de country nao encontrada. Verifique o CSV de entrada.')
    else:
        country_counts = df.groupby(country_col).size().reset_index(name='title_count')
        country_counts = country_counts.sort_values('title_count', ascending=False)
        country_counts.to_csv(os.path.join(DATA_DIR, 'country_counts.csv'), index=False)
        country_counts.head(20).to_csv(os.path.join(DATA_DIR, 'top20_countries.csv'), index=False)
        country_counts.head(10).to_csv(os.path.join(DATA_DIR, 'top10_countries.csv'), index=False)
        print('Gerado: country_counts.csv, top10_countries.csv')

    genre_col = 'genre_exploded' if 'genre_exploded' in df.columns else ('listed_in' if 'listed_in' in df.columns else None)
    if country_col and genre_col:
        cg = df.groupby([country_col, genre_col]).size().reset_index(name='title_count')
        cg = cg.sort_values([country_col, 'title_count'], ascending=[True, False])
        cg.to_csv(os.path.join(DATA_DIR, 'country_genre_counts.csv'), index=False)
        print('Gerado: country_genre_counts.csv')

    year_col = 'added_year' if 'added_year' in df.columns else ('date_added' if 'date_added' in df.columns else None)
    type_col = 'type' if 'type' in df.columns else None
    if year_col and type_col:
        at = df.groupby([year_col, type_col]).size().reset_index(name='title_count')
        at = at.sort_values([year_col, type_col])
        at.to_csv(os.path.join(DATA_DIR, 'annual_trends.csv'), index=False)
        print('Gerado: annual_trends.csv')
    else:
        print('Colunas para annual trends nao encontradas (esperadas: added_year, type)')

    month_col = 'added_month' if 'added_month' in df.columns else None
    if year_col and month_col:
        hm = df.groupby([year_col, month_col]).size().reset_index(name='title_count')
        # opcional: pivot
        hm_pivot = hm.pivot(index=year_col, columns=month_col, values='title_count').fillna(0).astype(int)
        hm.to_csv(os.path.join(DATA_DIR, 'heatmap_month_year.csv'), index=False)
        hm_pivot.to_csv(os.path.join(DATA_DIR, 'heatmap_month_year_pivot.csv'))
        print('Gerado: heatmap_month_year.csv e heatmap_month_year_pivot.csv')
    else:
        print('Colunas para heatmap (added_month/added_year) nao encontradas.')

    print('Preparacao concluida. Arquivos salvos em:', DATA_DIR)


if __name__ == '__main__':
    prepare()
