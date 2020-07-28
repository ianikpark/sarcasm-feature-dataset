import os
from shutil import copyfile
import pandas as pd

pos = os.listdir('input/sarcastic')
ones = [1] * len(pos)
neg = os.listdir('input/non-sarcastic')
zeroes =[0] * len(neg)

outputdir = 'output/merged/'

if(not os.path.isdir(outputdir)):
	os.mkdir(outputdir)

for p in pos:
	copyfile('input/sarcastic/'+p, outputdir+p)


for n in neg:
	copyfile('input/non-sarcastic/'+n, outputdir+n)

df_pos = pd.DataFrame(data={'src_file': pos, 'label': ones}, columns= {'src_file', 'label'})
df_neg = pd.DataFrame(data={'src_file': neg, 'label': zeroes}, columns= {'src_file', 'label'})

df = pd.concat([df_pos, df_neg])
df = df.sample(frac=1).reset_index().drop('index', axis=1);

df.to_csv('output/labels.csv')