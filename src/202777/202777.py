import os

base_url = 'https://raw.github.com/practical-jupyter/sample-data/master/anime/'
anime_csv = os.path.join(base_url, 'anime.csv')
print(anime_csv)

import pandas as pd

anime_csv = os.path.join(base_url, 'anime.csv')
print(pd.read_csv(anime_csv).head())
