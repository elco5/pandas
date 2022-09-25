import re
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

def get_step_values( ts, change_locs, window_percent=0.5 ):

    step_lengths = np.diff(change_locs)
    window_widths = (step_lengths*window_percent).astype(int)

    _step_values = np.zeros(len(change_locs) - 1)
    for i, start in enumerate(window_widths):
        _step_values[i] = np.mean(
            ts[change_locs[i+1]-window_widths[i]])
    
    return _step_values

def get_change_points(vs, threshold = 1):
    vdif = np.abs(np.diff(vs, append=vs[0] ))
    vbin = vdif > threshold
    change_points = np.where(vbin=True)[0]

