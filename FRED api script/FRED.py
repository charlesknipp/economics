import pandas as pd
import statsmodels.formula.api as smf
from fredapi import Fred


# declare your datasets uisng the series id; for example SP500 and GDP
datasets = ['GDP','SP500']

# need to have an api key
fred = Fred(api_key = open('FRED api script/api_key.txt','r').read())

ser = fred.get_series('GDP')
df = ser.to_frame(name=str(datasets))

print(ser)

'''
for set in datasets:
    if datasets.index(set) == 0:
        continue
    ser1 = fred.get_series(set)
    df1 = ser1.to_frame(name=set)
    df = pd.concat([df, df1], axis=1)

    print(df)
'''