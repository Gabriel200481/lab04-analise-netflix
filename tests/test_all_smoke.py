import os
import pandas as pd
import shutil

from src import preprocess
from src import standardize_countries
from src import prepare_powerbi
from src import generate_plotly
from src import analysis_duration
from src import generate_report_docx


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(ROOT, 'data')
ASSETS_FIG = os.path.join(ROOT, 'assets', 'figures')
ASSETS_INT = os.path.join(ROOT, 'assets', 'interactive')
OUT_DIR = os.path.join(ROOT, 'output')


def setup_module(module):
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(ASSETS_FIG, exist_ok=True)
    os.makedirs(ASSETS_INT, exist_ok=True)
    os.makedirs(OUT_DIR, exist_ok=True)
    for fn in ['country_counts.csv', 'top10_countries.csv', 'country_genre_counts.csv',
               'annual_trends.csv', 'heatmap_month_year.csv']:
        p = os.path.join(DATA_DIR, fn)
        if os.path.exists(p):
            os.remove(p)


def test_parse_duration_examples():
    assert preprocess.parse_duration('90 min') == (90, 'min')
    assert preprocess.parse_duration('2 Seasons') == (2, 'Season')
    assert preprocess.parse_duration(None) == (None, None)


def test_normalize_name_common():
    assert standardize_countries.normalize_name('usa') == 'United States'
    assert standardize_countries.normalize_name('') == 'Unknown'


def test_smoke_prepare_and_visuals_and_report():
    df = pd.DataFrame([
        {'title': 'A', 'country_exploded': 'United States', 'genre_exploded': 'Drama', 'added_year': 2020, 'added_month': 5, 'type': 'Movie', 'duration_value': 90, 'duration_unit': 'min', 'rating': 'PG-13'},
        {'title': 'B', 'country_exploded': 'United States', 'genre_exploded': 'Comedy', 'added_year': 2021, 'added_month': 6, 'type': 'TV Show', 'duration_value': 2, 'duration_unit': 'Season', 'rating': 'TV-MA'},
        {'title': 'C', 'country_exploded': 'Brazil', 'genre_exploded': 'Drama', 'added_year': 2020, 'added_month': 5, 'type': 'Movie', 'duration_value': 100, 'duration_unit': 'min', 'rating': 'PG'},
    ])
    csv_path = os.path.join(DATA_DIR, 'netflix_tratado_final.csv')
    df.to_csv(csv_path, index=False)

    prepare_powerbi.prepare()

    assert os.path.exists(os.path.join(DATA_DIR, 'country_counts.csv'))
    assert os.path.exists(os.path.join(DATA_DIR, 'top10_countries.csv'))

    df_loaded = pd.read_csv(csv_path)
    out1 = generate_plotly.top10_countries(df_loaded)
    out2 = generate_plotly.country_genre_matrix(df_loaded)
    at = generate_plotly.annual_trends(df_loaded)
    hm = generate_plotly.heatmap_month_year(df_loaded)
    assert os.path.exists(out1)
    assert os.path.exists(out2)

    p1 = analysis_duration.boxplot_duration_by_rating(df_loaded)
    p2 = analysis_duration.bar_duration_series(df_loaded)
    assert p1 is None or os.path.exists(p1)
    assert p2 is None or os.path.exists(p2)

    docx_out = generate_report_docx.generate()
    assert os.path.exists(docx_out)

