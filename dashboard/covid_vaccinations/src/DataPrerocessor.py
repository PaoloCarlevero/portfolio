import pandas as pd
from datetime import date

class DataPreprocessor:

    def __init__(self):
        pass

    def pipeline(self, df):
        df['date'] = pd.to_datetime(df['date'])
        df = self.remove_out_of_bound_dates(df)

        return df

    def remove_out_of_bound_dates(self, df, inplace = False):
        """ Removes inplace all records whose date is earlier than the date in wich the dataset claim to track (Jan 3, 2020)
        or later than today.

        Arg:
            df: pd.DataFrame
                The pd.DataFrame to check
        """
        df.drop(df[ ( df['date'] < pd.Timestamp(2020, 1, 3) ) | ( df['date'] > pd.Timestamp(date.today()) )].index, inplace = False)

    def add_missing_location_record(self, df):

        