import pandas as pd
import re

def read_csv(file_path):
    """Reads a CSV file and returns a pandas DataFrame.
    
    Args:
        file_path (str): The path to the CSV file.
        
    Returns:
        pd.DataFrame: The loaded data as a pandas DataFrame.
    """
    assert isinstance(file_path, str), "file_path must be a string"
    df = pd.read_csv(file_path)
    return df

def merge_data_frames(df1, df2):
    """Merges two pandas DataFrames on the 'City' column using an outer join.
    
    Args:
        df1 (pd.DataFrame): First DataFrame to merge.
        df2 (pd.DataFrame): Second DataFrame to merge.
        
    Returns:
        pd.DataFrame: The merged DataFrame.
    """
    assert isinstance(df1, pd.DataFrame) and isinstance(df2, pd.DataFrame), "Inputs must be pandas DataFrames"
    merged_df = df1.merge(df2, on="City", how="left")
    return merged_df

def process_city_names(df):
    """Processes city names in the DataFrame by splitting at certain characters and creating new rows for each segment.
    
    Args:
        df (pd.DataFrame): The DataFrame to process.
        
    Returns:
        pd.DataFrame: The DataFrame with processed city names.
    """
    assert isinstance(df, pd.DataFrame), "Input must be a pandas DataFrame"
    df = df.copy()
    for column_name in ["City", "CSA Title"]:
        if column_name in df.columns:
            new_rows = []
            for index, row in df.iterrows():
                if "-" in str(row[column_name]):
                    segments = re.split(', |_|-|!|\+', row[column_name])
                    for i, segment in enumerate(segments):
                        if i != len(segments) - 1:
                            new_row = row.copy()
                            new_row["City"] = segment + ", " + segments[-1]
                            new_rows.append(new_row)
            if new_rows:
                df = pd.concat([df, pd.DataFrame(new_rows)], ignore_index=True)
    df = df.drop_duplicates(subset=["City"])
    return df

def save_to_csv(df, file_name):
    """Saves the DataFrame to a CSV file.
    
    Args:
        df (pd.DataFrame): The DataFrame to save.
        file_name (str): The file name or path to save the DataFrame.
    """
    assert isinstance(df, pd.DataFrame) and isinstance(file_name, str), "Invalid input types"
    df.to_csv(file_name, index=False)

baseURL = "./dataset/"
happ = read_csv(baseURL + "Happiness_index.csv")
CSBA_List_1 = read_csv(baseURL + "list1_2023.csv")
CSBA_List_2 = read_csv(baseURL + "list2_2023.csv")
CSBA_df = pd.concat([CSBA_List_1, CSBA_List_2]).reset_index(drop=True).rename(columns={"CBSA Title": "City", "CBSA Code": "CBSA"})

CSBA_df = process_city_names(CSBA_df)
happiness_index_merged = merge_data_frames(happ, CSBA_df)

save_to_csv(happiness_index_merged, baseURL + "Happiness_index_merged.csv")
save_to_csv(CSBA_df, baseURL + "list_2023_filtered.csv")
