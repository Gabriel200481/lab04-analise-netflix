import os
import sys
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(ROOT, 'data')
OUT_DIR = os.path.join(ROOT, 'assets', 'interactive')
INPUT = os.path.join(DATA_DIR, 'netflix_tratado_final_canonical.csv')
if not os.path.exists(OUT_DIR):
    os.makedirs(OUT_DIR, exist_ok=True)


def find_input():
    if os.path.exists(INPUT):
        return INPUT
    alt = os.path.join(DATA_DIR, 'netflix_tratado_final.csv')
    if os.path.exists(alt):
        return alt
    return None


def top10_countries(df):
    col = 'country_canonical' if 'country_canonical' in df.columns else 'country_exploded'
    counts = df.groupby(col).size().reset_index(name='title_count')
    counts = counts.sort_values('title_count', ascending=False).head(10)
    fig = px.bar(counts, x='title_count', y=col, orientation='h', title='Top 10 Países por número de títulos')
    out = os.path.join(OUT_DIR, 'top10_countries.html')
    fig.write_html(out)
    print('Gerado:', out)
    return out


def country_genre_matrix(df):
    col = 'country_canonical' if 'country_canonical' in df.columns else 'country_exploded'
    genre = 'genre_exploded' if 'genre_exploded' in df.columns else 'listed_in'
    cg = df.groupby([col, genre]).size().reset_index(name='title_count')
    pivot = cg.pivot(index=col, columns=genre, values='title_count').fillna(0)
    fig = go.Figure(data=go.Heatmap(z=pivot.values, x=pivot.columns, y=pivot.index, colorscale='Viridis'))
    fig.update_layout(title='Especialização de Gênero por País (matriz)')
    out = os.path.join(OUT_DIR, 'country_genre_matrix.html')
    fig.write_html(out)
    print('Gerado:', out)
    return out


def annual_trends(df):
    year = 'added_year' if 'added_year' in df.columns else None
    typ = 'type' if 'type' in df.columns else None
    if year is None or typ is None:
        print('Colunas para annual trends nao encontradas')
        return None
    at = df.groupby([year, typ]).size().reset_index(name='title_count')
    fig = px.line(at, x=year, y='title_count', color=typ, title='Tendência anual de adição de títulos')
    out = os.path.join(OUT_DIR, 'annual_trends.html')
    fig.write_html(out)
    print('Gerado:', out)
    return out


def heatmap_month_year(df):
    year = 'added_year' if 'added_year' in df.columns else None
    month = 'added_month' if 'added_month' in df.columns else None
    if year is None or month is None:
        print('Colunas para heatmap nao encontradas')
        return None
    hm = df.groupby([year, month]).size().reset_index(name='title_count')
    hm_pivot = hm.pivot(index=year, columns=month, values='title_count').fillna(0)
    fig = go.Figure(data=go.Heatmap(z=hm_pivot.values, x=hm_pivot.columns, y=hm_pivot.index, colorscale='Blues'))
    fig.update_layout(title='Sazonalidade: contagem por mês e ano')
    out = os.path.join(OUT_DIR, 'heatmap_month_year.html')
    fig.write_html(out)
    print('Gerado:', out)
    return out


def main():
    inp = find_input()
    if inp is None:
        print('Arquivo de entrada nao encontrado para gerar plotly. Execute standardize_countries e preprocess primeiro.')
        sys.exit(1)
    df = pd.read_csv(inp)
    top10_countries(df)
    country_genre_matrix(df)
    annual_trends(df)
    heatmap_month_year(df)


if __name__ == '__main__':
    main()
