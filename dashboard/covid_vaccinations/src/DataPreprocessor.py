import pandas as pd
import numpy as np
from datetime import timedelta

class DataPreprocessor:

    def __init__(self):
        self.location_columns = ['iso_code','continent','location', 'location_type']
        self.pupulation_columns = [
            'population_density', 'median_age', 'aged_65_older', 'aged_70_older',
            'gdp_per_capita', 'extreme_poverty', 'cardiovasc_death_rate',
            'diabetes_prevalence', 'female_smokers', 'male_smokers',
            'handwashing_facilities', 'hospital_beds_per_thousand',
            'life_expectancy', 'human_development_index', 'population'
            ]
        self.covid_related_cumulative_columns = [
            'total_cases', 'total_deaths', 'total_cases_per_million', 'total_deaths_per_million', 'positive_rate',
            'tests_per_case', 'tests_units', 'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated',
            'total_boosters', 'total_vaccinations_per_hundred', 'people_vaccinated_per_hundred',
            'people_fully_vaccinated_per_hundred', 'total_boosters_per_hundred'
            ]

    def pipeline(self, df):
        df['date'] = pd.to_datetime(df['date'])
        self.drop_out_of_bound_dates(df)
        self.add_missing_records(df)
        df['location_type'] = df['location'].apply(self.get_location_type)
        df.sort_values(['location_type', 'continent', 'location', 'date'], inplace=True)
        df.reset_index(drop=True, inplace = True)
        df[self.location_columns] = df.groupby('location')[self.location_columns].ffill().bfill()
        df[self.pupulation_columns] = df.groupby('location')[self.pupulation_columns].ffill().bfill()
        df[self.covid_related_cumulative_columns] = df.groupby('location')[self.covid_related_cumulative_columns].ffill()
        df['continent'].fillna(df['location'], inplace = True)
        df['iso_code'].replace(to_replace='NAM', value='NTA', inplace=True)
        df['iso_code'].replace(to_replace='SAM', value='STA', inplace=True)
        df['iso_code'] = df['iso_code'].str[-3:]


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
        """Add missing records.
        
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