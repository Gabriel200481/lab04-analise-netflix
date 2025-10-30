from pathlib import Path
import glob, os
p=Path('data')
files=['netflix_tratado_final.csv','netflix_tratado_final_canonical.csv','country_counts.csv','top10_countries.csv','country_genre_counts.csv','annual_trends.csv','heatmap_month_year.csv']
for f in files:
    fp=p/f
    print(f, fp.exists(), fp.stat().st_size if fp.exists() else 'NA')
print('\nInteractive HTMLs:')
for h in glob.glob('assets/interactive/*.html'):
    print(' -', h, os.path.getsize(h))
print('\nFigures:')
for img in glob.glob('assets/figures/*.png'):
    print(' -', img, os.path.getsize(img))
print('\nOutput docx exists:', Path('output/dashboard_netflix.docx').exists(), Path('output/dashboard_netflix.docx').stat().st_size if Path('output/dashboard_netflix.docx').exists() else 'NA')
