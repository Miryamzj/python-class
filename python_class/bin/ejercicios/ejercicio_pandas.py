import pandas as pd 
#s = pd.Series([10, 20, 30], index=['a','b', 'c'])
#print (s)

data = {
    'Gene': ['thrL', 'thrA', 'thr8'], 
    'Longitud': [117, 2340, 1461]
}    
df = pd.DataFrame.from_dict(data)
print (df)