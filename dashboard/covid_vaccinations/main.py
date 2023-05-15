import pandas as pd

from src.DataIngestor import DataIngestor
from src.DataPrerocessor import DataPreprocessor


di = DataIngestor()
dp = DataPreprocessor()

df = di.read_file(r'data_lake/raw_data/owid-covid-data.csv')

print(df.sort_values('date'))

df = dp.pipeline(df)

print(df.sort_values('date'))