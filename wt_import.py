import pandas as pd
import numpy as np
import typing
import string

class Wt_Importer:

    def __init__(self,path_to_csv: str) -> None:
        self.df = None
        self.df_raw = pd.read_csv(path_to_csv)
        self.column_name_index = None
        self.column_names = [""]
        self.apply_column_names()
        self.apply_index()
        self.trim_dataframe()
        

    def find_column_name_index(self) -> int:
    # search the first column of the data to find the row that contains the column names.
    # Column names are the physical quantities measured like voltage and current
        search_term = "Store No."
        for index, entry in enumerate(self.df_raw.iloc[:,0]):
            if entry == search_term:
                return index        

    def get_column_names(self, index: int) -> np.ndarray:
        # return an array of strings to be used as column headers
        self.column_names = self.df_raw.iloc[index,:].to_numpy(dtype=str) 
        return self.column_names

    def apply_column_names(self):
        # find and set the new column names
        self.column_name_index = self.find_column_name_index()
        column_names = self.get_column_names(self.column_name_index)
        self.df_raw.columns = column_names
        return

    def apply_index(self):
        self.df_raw.index = self.df_raw.iloc[:,0].to_numpy() #use Store Numbers as index
        return
    
    def trim_dataframe(self):
        # trim the top of the data frame - leaving only the data below the column names row
        self.df = self.df_raw.iloc[self.column_name_index + 1:, :]




############# DRIVER #################
wt_full_sample = 'C:\\Users\\count\\dev\\pandas\\data\\PA_sample_data.csv'
wt_short_sample = 'C:\\Users\\count\\dev\\pandas\\data\\PA_sample_data_short.csv'
wt_micro_sample = "C:\\Users\\count\\dev\\pandas\\data\\PA_micro.csv"
f = wt_full_sample

wt = Wt_Importer(f)
print(wt.df)

# print(wt.df_raw.iloc[0:5,:])
# print(wt.find_column_name_index())
# print(wt.df)
# print(wt.column_names)
