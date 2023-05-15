import pandas as pd

from src.DataIngestor import DataIngestor
from src.DataPreprocessor import DataPreprocessor


di = DataIngestor()
dp = DataPreprocessor()

df = di.read_file(r'data_lake/raw_data/owid-covid-data.csv')

df = dp.pipeline(df)

print(df.isna().sum())