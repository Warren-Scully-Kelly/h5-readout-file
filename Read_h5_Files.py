# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 15:57:26 2025

@author: wscullykelly
"""

import matplotlib.pyplot as mplt
import h5py
filename = "MKIDs_data_20250409.h5"

with h5py.File(filename, "r") as f:
    print("Keys: %s" % f.keys())

def read_pulse(group):
    with h5py.File(filename, "r") as f:
        # Print all root level object names (aka keys) 
        # these can be group or dataset names 
        
        # get first object name/key; may or may NOT be a group
        a_group_key = list(f.keys())[group]
    
        # If a_group_key is a group name, 
        # this gets the object names in the group and returns as a list
        # non pulse data
        data = list(f[a_group_key])
        
        # pulse datar
        I_data = f[a_group_key]['I'][()]
        Q_data = f[a_group_key]['Q'][()]
        adc_ch1_data = f[a_group_key]['adc_ch1'][()]
        adc_ch2_data = f[a_group_key]['adc_ch2'][()]
        phase_data = f[a_group_key]['phase'][()]
        time_us_data = f[a_group_key]['time_us'][()]
    
        # If a_group_key is a dataset name, 
        # this gets the dataset values and returns as a list
        data = list(f[a_group_key])
        # preferred methods to get dataset values:
        ds_obj = f[a_group_key]      # returns as a h5py dataset object
        #ds_arr = f[a_group_key][()]  # returns as a numpy array
        
        return data, I_data, Q_data, adc_ch1_data, adc_ch2_data, phase_data, time_us_data


#end_point = number of pulses + 4
end_point = 48
for i in range(3,end_point):
    pulse = read_pulse(i)
    
    # 0 = data, 1 = I_data, 2 = Q_data, 3 = adc_ch1_data, 4 = adc_ch2_data
    # 5 = phase_data, 6 = time_us_data
    print(max(pulse[5]))
    
    
    
