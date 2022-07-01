import numpy as np
import pandas as pd
import h5py
import glob

#ignore warnings for df.append to pandas.concat
import warnings
warnings.filterwarnings("ignore")

#get all data from all files
def get_data(hf, number_of_blocks, names_of_blocks):
    
    #read names of all blocks in a file (blockXXXX/data)
    d = {}
    for i,number in enumerate(range(0, number_of_blocks)):
        d["block" + str(i)] = hf[names_of_blocks[i]+"/data"][:, index] 

    #append data from all blocks in a file (blockXXXX/data)    
    data = []
    for value in d.values():
        data.append(value)
    return data 

# get all gains and offsets from all files
def get_gain_or_offset(hf, number_of_blocks, names_of_blocks, gain=False, offset=False):

    if gain==True:

        #read names of all blocks in a file (blockXXXX/gains)
        d = {}
        for i,number in enumerate(range(0, number_of_blocks)):
            #print(index)
            d["block" + str(i)] = hf[names_of_blocks[i]+"/gains"][index] 

        #append gains from all blocks in a file (blockXXXX/gains)    
        gains = []
        for value in d.values():
            gains.append(value)
        return gains 
    
    elif offset==True:

        #read names of all blocks in a file (blockXXXX/offsets)
        d = {}
        for i,number in enumerate(range(0, number_of_blocks)):
            d["block" + str(i)] = hf[names_of_blocks[i]+"/offsets"][index]

        #append offsets from all blocks in a file (blockXXXX/offsets)      
        offset = []
        for value in d.values():
            offset.append(value)
        return offset 
    
    else:
        print("Error")
        return None 

# return keys for each file
def keys(hf):
    return [key for key in hf.keys()]

# extract filename, mean, min, max and rmse from each chanel being investigated  
def extract_mean_max_min_rmse(filename, index, cut_off_index):

    hf = h5py.File(filename, 'r')

    #return name of blocks in a file
    names_of_blocks = keys(hf)[3:]

    #total number of blocks in a file
    number_of_blocks = hf.attrs['no_blocks'] 

    #append all data from all groups for a file
    data = get_data(hf, number_of_blocks, names_of_blocks)
    
    #append all gains from all groups for a file
    gains = get_gain_or_offset(hf, number_of_blocks, names_of_blocks, gain=True)

    #append all offsets from all groups for a file
    offsets = get_gain_or_offset(hf, number_of_blocks, names_of_blocks, offset=True)

    #offset + data*gains
    values = []
    for i in range(0, number_of_blocks):               
        for j in range(0, len(hf[names_of_blocks[i]+"/data"][:,index] )):
            d = np.add(offsets[i] , np.multiply(data[i][j], gains[i]))
            values.append(d)

    #index number of file
    tmp_id = int(file.split('_')[-1].split('.')[0])

    #mean
    mean = np.mean(values[cut_off_index: ])     

    #min
    min = np.min(values[cut_off_index: ])

    #max
    max = np.max(values[cut_off_index: ]) 

    #rms
    rms = np.sqrt(np.mean(np.square(values[cut_off_index: ])))
    
    return tmp_id, filename, mean, min, max, rms
            

if __name__=='__main__':

    #index value of attribute being investigated
    indexes = [13, 41, 42, 95, 99, 131, 135, 215, 219, 299, 303, 383]

    """
    13  : Free wind speed Vy, gl. coo, of gl. pos    0.00,   0.00,-150.00
    41  : State acc x  Mbdy:tower E-nr:  10 Z-rel:1.00 coo: global  tower top fa acc
    42  : State pos y  Mbdy:tower E-nr:  10 Z-rel:1.00 coo: global  tower top ss displ
    95  : ESYS floater SENSOR	       1	surge 	displacement
    99  : ESYS floater SENSOR	       5	pitch 	displacement
    131 : ESYS floater SENSOR         37 Free-surface elevation
    135 : b'ESYS line1 SENSOR          4
    215 : b'ESYS line1 SENSOR         84
    219 : ESYS line2 SENSOR            4
    299 : ESYS line2 SENSOR           84
    303 : ESYS line3 SENSOR            4
    383 : ESYS line3 SENSOR           84
    """
      
    for index in indexes:

        # step size in time series
        step_size = 0.01

        #input time in seconds
        cut_off_time = 100

        #time taken for simulation to stabilize
        cut_off_index = int(cut_off_time/step_size)

        #read all hdf5 files present in folder
        filenames = glob.glob('wind_turb_12ms_waves_ireg_rated_*.hdf5')

        #iterate through ever file and extract mean, min, max and rmse
        for k in range(len(filenames)):
            file = filenames[k]
            if  k==0:
                data = extract_mean_max_min_rmse(file, index, cut_off_index)
                df = pd.DataFrame(np.column_stack(data), columns=["File_ID", "Filename", "Mean", "Min", "Max", "RMS"])

            else:
                data = extract_mean_max_min_rmse(file, index, cut_off_index)
                row = pd.Series(data, index = df.columns)
                df = df.append(row, ignore_index=True)

        #print dataframe to csv
        df.to_csv(f"Result_index_{index}.csv")
