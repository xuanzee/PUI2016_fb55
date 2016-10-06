import pandas as pd
import os
import sys

tmp = pd.read_csv(sys.argv[1])[['GitHub Link','Net ID']]
tmp.dropna(inplace=True)
puidir = os.getenv("PUI2016")
if puidir is None:
	print ("make sure the env variable PUI2016 is set up")
	sys.exit()

if not os.path.isdir(puidir):
	print ("make sure %s exists and is a directory"%pui2916)
	sys.exit()

os.system("cd %s"%pui2016)
cwd = os.getcwd()
print ("cwd")

for i,n in enumerate(tmp['Net ID'].values):
        print (tmp['GitHub Link'].values[i]+"/PUI2016_"+n)

#for i,n in enumerate(tmp['Net ID'].values):
#        os.system ("git clone " + tmp['GitHub Link'].values[i]+"/PUI2016_"+n)

