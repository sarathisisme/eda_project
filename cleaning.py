import pandas as pd

def clean_data(df_in):
    """
    Cleans the raw dataframe and returns a cleaned version
    """
    df = df_in.copy()


    #imputing missing values
    df['sqft_basement'] = df['sqft_basement'].fillna(df['sqft_living'] - df['sqft_above'])
    df['yr_renovated'] = df['yr_renovated'].fillna(0) # 0 for unrenovated
    df['waterfront'] = df['waterfront'].fillna(int(df['waterfront'].mode()))
    df['view'] = df['view'].fillna(int(df['view'].mode()))

    #correcting value
    df['yr_renovated'] = df.yr_renovated.apply(lambda x: x/10)

    #correcting data types
    df = df.astype({'bedrooms': int, 
                'sqft_living': int,
                'sqft_lot': int,
                'floors': int,
                'condition': int,
                'grade': int,
                'sqft_above': int,
                'yr_built': int,
                'zipcode': int,
                'sqft_living15': int,
                'sqft_lot15': int,
                'price': int,
                'waterfront': int,
                'view': int,
                'sqft_basement': int,
                'yr_renovated': int})

    #correcting date data type
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')


    return df