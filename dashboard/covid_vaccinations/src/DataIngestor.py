import pandas as pd

class DataIngestor:

    def __init__(self):
        pass

    def read_file(self, file):

        format = file.rsplit('.')[1]

        if format == 'csv':
            return pd.read_csv(file)