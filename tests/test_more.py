import os
import pandas as pd

from src import preprocess
from src import standardize_countries


def test_parse_duration_edge_cases():
    # spaces, uppercase, no space
    assert preprocess.parse_duration('120 min') == (120, 'min')
    assert preprocess.parse_duration('120min') == (120, 'min')
    assert preprocess.parse_duration('1 Season') == (1, 'Season')
    assert preprocess.parse_duration('2 seasons') == (2, 'Season')
    assert preprocess.parse_duration('N/A') == (None, 'N/A') or preprocess.parse_duration('N/A') == (None, None)


def test_split_to_list_and_empty():
    s = pd.Series(['A, B', None, 'C'])
    lists = preprocess.split_to_list(s)
    assert isinstance(lists.iloc[0], list)
    assert lists.iloc[0] == ['A', 'B'] or lists.iloc[0] == ['A', ' B']
    assert lists.iloc[1] == ['Unknown']


def test_normalize_name_pycountry_fallback():
    # common lower-case country name should map to title case or official name
    out = standardize_countries.normalize_name('brazil')
    assert out.lower().startswith('brazil') or 'brazil' in out.lower()
