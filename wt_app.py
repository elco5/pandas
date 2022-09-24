from wt_import import Wt_Importer

wt_micro_sample = "C:\\Users\\count\\dev\\pandas\\data\\PA_micro.csv"
wt_full_sample = 'C:\\Users\\count\\dev\\pandas\\data\\PA_sample_data.csv'
wt_short_sample = 'C:\\Users\\count\\dev\\pandas\\data\\PA_sample_data_short.csv'
wt_micro_sample = "C:\\Users\\count\\dev\\pandas\\data\\PA_micro.csv"

print('\n')

df = Wt_Importer(wt_micro_sample).df


