import pandas as pd

class DataIngestor:

    def __init__(self):
        pass

    def read_file(self, path):

        format = path.rsplit('.')[1]

        if format == 'csv':
            return pd.read_csv(path)
        
    def save_file(self, df, path):

        format = path.rsplit('.')[1]

        if format == 'csv':
            df.to_csv(path)
        elif format == 'xlsx':
            df.to_excel(path, engine='xlsxwriter', index=False)