import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import plotly.express as px

from wt_import import Wt_Importer

volt_watt_sample = "C:\\Users\\ecountrywood\\dev\\pandas\\data\\volt-watt\\VW_CH1_100_sample_fix.csv"

dfr= Wt_Importer(volt_watt_sample).df_raw
dfr.head()