import matplotlib.pyplot as plt
import numpy as np
# every_Nth_sample = 10
# vs_downsampled = vs[0:vs.size:every_Nth_sample]


# plt.figure(figsize=(16,2))
# plt.stem(vs_downsampled)


# import jenkspy
# breaks = jenkspy.jenks_breaks(vs, n_classes=15)
# # breaks

# ts: original timeseries data / ts_change_loc = step locations
# redline the change points:
def plot_change_points(ts,ts_change_loc):
    plt.figure(figsize=(16,2))
    plt.plot(ts)
    for x in ts_change_loc:
        plt.axvline(x,lw=2, color='red')

def get_midpoints(a:np.ndarray):
    '''
    a = [1,2,3,4,5]

          [2,3,4,5]
       +[1,2,3,4]
       -------------
        [3,4,5,6]/2 = [1.5, 2, 2.5, 3]
        then cast to int and truncate float part   
    '''    
    M = (a[1:] + a[:-1])/2
    K = M.astype(int)
    return K