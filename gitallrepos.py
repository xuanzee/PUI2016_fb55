import pandas as pd
import os
import sys

tmp = pd.read_csv(sys.argv[1])[['GitHub Link','Net ID']]
tmp.dropna(inplace=True)
for i,n in enumerate(tmp['Net ID'].values):
        print (tmp['GitHub Link'].values[i]+"/PUI2016_"+n)
import os
for i,n in enumerate(tmp['Net ID'].values):
        os.system ("git clone " + tmp['GitHub Link'].values[i]+"/PUI2016_"+n)

