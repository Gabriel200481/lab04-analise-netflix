r"""
Standardiza nomes de países e gera um CSV canônico.

Entrada: data/netflix_tratado_final.csv (linha por país/genre/director)
Saída:
 - data/netflix_tratado_final_canonical.csv
 - data/country_aliases_mapping.csv

Uso:
    python src\standardize_countries.py
"""
import os
import sys
import pandas as pd
import re

try:
    import pycountry
except Exception:
    pycountry = None

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(ROOT, 'data')
INPUT = os.path.join(DATA_DIR, 'netflix_tratado_final.csv')
OUTPUT = os.path.join(DATA_DIR, 'netflix_tratado_final_canonical.csv')
MAPPING_OUT = os.path.join(DATA_DIR, 'country_aliases_mapping.csv')

COMMON_MAP = {
    'usa': 'United States',
    'us': 'United States',
    'u.s.': 'United States',
    'u.s.a.': 'United States',
    'united states of america': 'United States',
    'uk': 'United Kingdom',
    'england': 'United Kingdom',
    'south korea': 'South Korea',
    'korea, south': 'South Korea',
    'russia': 'Russian Federation',
    'laos': 'Lao People\'s Democratic Republic',
    # adicione mais aliases conforme necessário
}


def normalize_name(name):
    if pd.isna(name):
        return 'Unknown'
    s = str(name).strip()
    if s == '' or s.lower() in ['nan', 'none']:
        return 'Unknown'
    # remove extra whitespace and unify commas
    s = re.sub(r"\s+", ' ', s)
    s_clean = s.strip().lower()
    # direct common map
    if s_clean in COMMON_MAP:
        return COMMON_MAP[s_clean]
    # try pycountry lookup
    if pycountry:
        try:
            # try by common name
            country = pycountry.countries.lookup(s)
            # pycountry returns dynamic objects; use getattr to avoid static type checker
            return getattr(country, 'name', str(country))
        except Exception:
            # fallback: try partial matches
            for c in pycountry.countries:
                cname = getattr(c, 'name', '')
                if s_clean in cname.lower():
                    return cname
    # capitalize words as fallback (Title Case)
    return s.title()


def standardize():
    if not os.path.exists(INPUT):
        print('Arquivo de entrada nao encontrado:', INPUT)
        sys.exit(1)
    df = pd.read_csv(INPUT)
    col = 'country_exploded' if 'country_exploded' in df.columns else ('country' if 'country' in df.columns else None)
    if col is None:
        print('Coluna de country nao encontrada no CSV de entrada.')
        sys.exit(1)

    orig = df[col].fillna('Unknown').astype(str)
    mapping = {}
    canonical = []
    for v in orig:
        key = v.strip()
        canon = normalize_name(key)
        canonical.append(canon)
        if key not in mapping:
            mapping[key] = canon

    df['country_canonical'] = canonical
    df.to_csv(OUTPUT, index=False)
    # save mapping
    map_df = pd.DataFrame(list(mapping.items()), columns=['alias','canonical'])
    map_df.to_csv(MAPPING_OUT, index=False)
    print('Salvo:', OUTPUT)
    print('Mapa de aliases salvo:', MAPPING_OUT)
    return df


if __name__ == '__main__':
    standardize()
