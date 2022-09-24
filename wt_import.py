import pandas as pd
import numpy as np



class Wt_Importer:
    '''
    clean wt3000 csv output file: 
    - remove bloat at top 
    - index (row names) with observation numbers 
    - use measured quantity names as column names
    '''

    def __init__(self, path_to_csv:str) -> None:
        self.path_to_csv = path_to_csv
        self.df = None
        self.df_raw = None
        self.column_name_index = None
        self.column_names = [""]
        self.load(self.path_to_csv)
        self.process()

    def load(self, path_to_csv: str) -> None:
        self.df_raw = pd.read_csv(path_to_csv)

    def process(self) -> None:
        self.apply_column_names()
        self.apply_index()
        self.trim_dataframe()

    def find_column_name_index(self) -> int:
        # search the first column of the data to find the row that contains the column names.
        # Column names are the physical quantities measured like voltage and current
        search_term = "Store No."
        for index, entry in enumerate(self.df_raw.iloc[:, 0]):
            if entry == search_term:
                return index

    def get_column_names(self, index: int) -> np.ndarray:
        # return an array of strings to be used as column headers
        self.column_names = self.df_raw.iloc[index, :].to_numpy(dtype=str)
        return self.column_names

    def apply_column_names(self):
        # find and set the new column names
        self.column_name_index = self.find_column_name_index()
        column_names = self.get_column_names(self.column_name_index)
        self.df_raw.columns = column_names
        return

    def apply_index(self):
        # use Store Numbers as index
        self.df_raw.index = self.df_raw.iloc[:, 0].to_numpy()
        return

    def trim_dataframe(self):
        # trim the top of the data frame - leaving only the data below the column names row
        self.df = self.df_raw.iloc[self.column_name_index + 1:, :]





# print(pandas.read_csv(filename).to_markdown(index=False))
# print(wt.df_raw.iloc[0:5,:])
# print(wt.find_column_name_index())
# print(wt.df)
# print(wt.column_names)
