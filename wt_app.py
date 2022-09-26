from wt_import import Wt_Importer
import pandas as pd
wt_micro_sample = "C:\\Users\\count\\dev\\pandas\\data\\PA_micro.csv"
wt_full_sample = 'C:\\Users\\count\\dev\\pandas\\data\\PA_sample_data.csv'
wt_short_sample = 'C:\\Users\\count\\dev\\pandas\\data\\PA_sample_data_short.csv'
wt_micro_sample = "C:\\Users\\count\\dev\\pandas\\data\\PA_micro.csv"
vv_data_sample = "C:\\Users\\ecountrywood\\dev\\pandas\\data\\volt-var\\EUT_20_2.csv"
vvc2 = 'C:\\Users\\ecountrywood\\dev\\pandas\\data\\volt-var\\VVc2_Vr240.csv'


print('\n')

df = Wt_Importer(vv_data_sample).df

for column in df.columns:
    if column  not in ['Date', 'Time']:
        
        pd.to_numeric(df[column], errors='coerce')

