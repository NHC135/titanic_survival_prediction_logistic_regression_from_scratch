import pandas as pd
import numpy as np
from datetime import datetime

#=========================================================
# Data Preprocessing: (Tried to create them as general as can be for some of datasets I worked on)
#=========================================================

def standardize_values(series):
    """
    Standardize a series with z score normaliztion
    (x - mean) / std
    Return: standardized series with mean = 0 and std = 1
    """
    mean = series.mean()
    std = series.std()
    standardized  = (series - mean) / std
    return standardized


def trim_all_columns(df): 
    """ 
    Trim the data frame from white spaces for string data types
    """
    trim_strings = [lambda x: x.str.strip() if x.dtype == object else x]
    clean_df = df.apply(trim_strings)
    
    return clean_df


# Handling missing data 
def handling_missing_data(df, strategy= "drop", threshold= .5): 
    """
    Examines the columns for percentage of nulls. Change the threshold
    amount to drop the column. 
    
    Parameters: 
    df: dataframe
    strategy: 'drop', 'fill_mean', 'fill_median', 'fill_mode', 'foward_fill', 'interpolate'
    Threshold: amount of missing data within a column prior to dropping    
    """
    # identify missing data 
    missing_stats = pd.DataFrame({
        'column': df.columns, 
        'missing_count': df.isnull().sum() 
        'missing_percentage': df.isnull().mean() * 100 
    })
    
    print("Missing Data Statistics: ") 
    print(missing_stats[missing_stats['missing_count'] > 0])
    
    # methods for missing data
    if strategy == 'drop': 
        columns_dropped = missing_stats[missing_stats['missing_percentage'] > threshold * 100]['column']
        df_clean = df.drop(columns= columns_dropped)
        # drop rows with any missing values in remaining columns
        df_clean = df_clean.dropna()
        
    elif strategy == 'fill_mean': 
        df_clean = df.copy()
        for col in df.select_dtypes(include= [np.number]).columns: 
            df_clean[col].fillna(df[col].mean(), inplace= True) 
    
    elif strategy == 'fill_median': 
        df_clean = df.copy() 
        for col in df.select_dtypes(include= [np.number]).columns: 
            df_clean[col].fillna(df[col].median(), inplace= True)
            
    elif strategy == 'fill_mode': 
        df_clean = df.copy() 
        for col in df.select_dtypes(include= [np.number]).columns: 
            df_clean[col.fillna(df[col].mode(), inplace= True)]
    
    elif strategy == 'foward fill': 
        df_clean = df.fillna(method= 'ffill')
    
    elif strategy == 'interpolate': 
        df_clean = df_clean.replace(method= 'linear')
        
    
    # Handle placeholder common NULL values in data
    placeholders = ['N/A', 'n/a', 'NA', 'null','NULL', '-', '?', 'unknown']
    for placeholder in placeholders: 
        df_clean = df_clean.replace(placeholder, np.nan)
        
    return df_clean


# Handling Duplicates                           
def handling_duplicate_data(df, subset= None, keep= 'first'):
    """ 
    Identify and handle duplicate records
    
    Parameters: 
    - df: pandas Dataframe
    - subset: columns in the datafram to check for duplicates
    - keep: 'first', 'last', or False (to remove all duplicates)
    """
    
    # Find exact duplicates 
    duplicates = df.duplicated(subset= subset, keep=False) 
    print(f"Number of duplicates: " {duplicates.sum()})
    
    if duplicates.sum() > 0: 
        print("\nDuplicated Rows: ")
        print(df[duplicates].sort_values(subset if subset else df.columns.tolist()))
    
    #remove exact duplicates 
    df_clean = df.drop_duplicates(subset= subset, keep= keep)
    
    print(f"\nRows AFTER cleaning: {len(df_clean)} \nRows BEFORE cleaning: {len(df)} ")
    
    return df_clean


# Standardizing Formats
def standardize_formats(df): 
    """
    Standardize common data formats
    """
    df_clean = df.copy() 
    
    def standardize_sex(df, column="Sex"): 
        """ 
        Correct the 'Sex' column values for more constistency, 'Male' & 'Female'.
        change the arg 'column' to whatever the name of the column for the gender in the dataset is.
        """
        df_clean = (
            df[column]
            .str.lower()                                                      # make the string lower case
            .apply(lambda x: "Female" if x.startswith("f") or "woman" in x    # apply to the df 
                        else "Male" if x.startswith("m") or "guy" in x 
                        else "Other")     
        )
        return df_clean
    
    def clean_date(date_str, output_format='%Y-%m-%d'): 
        # checks the entire column to fit a single format of mixed date formats, 
        # 'coerce' returns NaT instead of the original date vs. 'ignore' which keeps its
        date_obj = pd.to_datetime(date_str, format= 'mixed', errors= 'coerce') 
        
        # Quality checks if what was returned is datetime object, if chosen 'ignore' arg
        if isinstance(date_obj, pd.Timestamp): 
            return date_obj.strftime(output_format)
    
        return date_str
     
    # apply standardizations
    # run the df through the standardize funcs
    for col in df_clean.columns: 
        if 'date' in col.lower() or df_clean[col].dtype == 'object': 
            try: 
                df_clean[col] = df_clean[col].apply(clean_date)
            except: 
                pass
    
    for col in df_clean.columns: 
        if 'sex' or 'gender' in col.lower(): 
            try: 
                df_clean[col] = df_clean[col].apply(standardize_sex)
            except: 
                pass
            
    return df_clean 