import pandas as pd
import re

happ = pd.read_csv("Happiness_index.csv")
#print(happ["City"])
CSBA_List_1 = pd.read_csv("list1_2023.csv")
CSBA_List_2 = pd.read_csv("list2_2023.csv")
CSBA_df = pd.concat([CSBA_List_1,CSBA_List_2])
print(CSBA_df.columns)
#print(dinkle["County/County Equivalent"])
CSBA_df = CSBA_df.rename(columns={"CBSA Title": "City", "CBSA Code": "CBSA"})
CSBA_df = CSBA_df.reset_index()
print(len(CSBA_df))
for index, row in CSBA_df.iterrows():

    if "-" in row["City"]:
        segments = re.split(', |_|-|!|\+', row["City"])
        #print(index)
        for i,cit in enumerate(segments):
            if not i == len(segments):
                new_row = row.copy()
                new_row["City"] = cit + ", " + segments[-1]
                CSBA_df.loc[len(CSBA_df)] = new_row


for index, row in CSBA_df.iterrows():
    if "-" in str(row["CSA Title"]):
        segments = re.split(', |_|-|!|\+', row["CSA Title"])
        for i,cit in enumerate(segments):
            if not i == len(segments):
                new_row = row.copy()
                new_row["City"] = cit + ", " + segments[-1]
                CSBA_df.loc[len(CSBA_df)] = new_row


CSBA_df = CSBA_df.drop_duplicates(subset=["City"])

happiness_index_merged = happ.merge(CSBA_df,on="City",how="left")

happiness_index_merged.to_csv("Happiness_index_merged.csv")

CSBA_df.to_csv("list_2023_filtered.csv")