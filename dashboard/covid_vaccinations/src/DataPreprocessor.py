import pandas as pd
import numpy as np
from datetime import timedelta

class DataPreprocessor:

    def __init__(self):
        self.pupulation_columns = ['iso_code','continent','population_density', 'median_age', 'aged_65_older', 'aged_70_older',
       'gdp_per_capita', 'extreme_poverty', 'cardiovasc_death_rate',
       'diabetes_prevalence', 'female_smokers', 'male_smokers',
       'handwashing_facilities', 'hospital_beds_per_thousand',
       'life_expectancy', 'human_development_index', 'population']

    def pipeline(self, df):
        df['date'] = pd.to_datetime(df['date'])
        self.drop_out_of_bound_dates(df)
        self.add_missing_records(df)
        df['location_type'] = np.NaN
        df['location_type'] = df['location'].apply(self.get_location_type)
        for column in self.pupulation_columns:
            df[column] = self.fillna_pairs_based(df, 'location', column)

        return df

    def drop_out_of_bound_dates(self, df):
        """Remove all records with out of bound dates.
        
        Remove all records whose date is earlier than the date in which the dataset
        claim to track (Jan 3, 2020) or later than today.

        Arg:
            df: pd.DataFrame
                The pd.DataFrame to check
        Return: DataFrame or None
            DataFrame without the out-of-bound records.
        """
        
        df.drop(df[ ( df['date'] < pd.Timestamp(2020, 1, 3) ) | ( df['date'] > pd.Timestamp.today() )].index, inplace = True)


        
    def add_missing_records(self, df):
        """ Add missing records.
        
        Create a tuple of all unique locations in the dataset.
        Iterate each date and check if there are records about all locations in the tuple,
        if some are missing they are add as a row containing only the date and the missign location.

        Arg:
            df: DataFrame
                The DataFrame to check for missing record.
        Return: None
                The rows are added inplace.
        """
        locations_list = tuple(df['location'].unique())

        current_date = df['date'].min()
        end_date  = df['date'].max()
        index = df.index.max() + 1

        while current_date <= end_date:

            slice = df.loc[df['date'] == current_date]
            slice_locations = set(slice['location'])

            for location in locations_list:
                if location not in slice_locations:
                    df.loc[index] = {'location': location, 'date': current_date}
                    index += 1

            current_date = current_date + timedelta(days=1)

    def get_location_type(self, item):

        if item in ('Africa', 'Asia', 'Europe', 'South America', 'North America', 'Oceania'):
            return 'continent'
        elif item in ('European Union'):
            return 'economic_uninon'
        elif item in ('High income', 'Low income', 'Lower middle income', 'Upper middle income'):
            return 'income'
        elif item == 'World':
            return 'world'
        else:
            return 'country'
        
    def fillna_pairs_based(self, df, key_col, value_col):

        pairs = df[[key_col, value_col]].drop_duplicates().dropna()
        pairs = dict(zip(pairs[key_col], pairs[value_col]))

        df[value_col] = df.apply(
            lambda row: pairs[row[key_col]] if (pd.isnull(row[value_col]) and row[key_col] in pairs.keys()) else row[value_col],
            axis=1
        )

        return df[value_col]