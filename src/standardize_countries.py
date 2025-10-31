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
}


def normalize_name(name):
    if pd.isna(name):
        return 'Unknown'
    s = str(name).strip()
    if s == '' or s.lower() in ['nan', 'none']:
        return 'Unknown'
    s = re.sub(r"\s+", ' ', s)
    s_clean = s.strip().lower()
    if s_clean in COMMON_MAP:
        return COMMON_MAP[s_clean]
    if pycountry:
        try:
            country = pycountry.countries.lookup(s)
            return getattr(country, 'name', str(country))
        except Exception:
            for c in pycountry.countries:
                cname = getattr(c, 'name', '')
                if s_clean in cname.lower():
                    return cname
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
    map_df = pd.DataFrame(list(mapping.items()), columns=['alias','canonical'])
    map_df.to_csv(MAPPING_OUT, index=False)
    print('Salvo:', OUTPUT)
    print('Mapa de aliases salvo:', MAPPING_OUT)
    return df


if __name__ == '__main__':
    standardize()
