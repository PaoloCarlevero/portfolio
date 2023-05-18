import pandas as pd

from src.DataIngestor import DataIngestor
from src.DataPreprocessor import DataPreprocessor


di = DataIngestor()
dp = DataPreprocessor()

df = di.read_file(r'data_lake/raw_data/owid-covid-data.csv')

print(df)
print(df.isna().sum())
df = dp.pipeline(df)
print(df)
print(df.isna().sum())

di.save_file(df, r'data_lake/processed_data/covid_data.csv')
di.save_file(df, r'data_lake/processed_data/covid_data.xlsx')
print('Done!')