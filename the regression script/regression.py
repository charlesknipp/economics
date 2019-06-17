import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fredapi import Fred
import statsmodels.formula.api as smf
import statsmodels.stats.api as sms


# convert pandas ts to an mpl readable ts only for graphing
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# this is a very rudimentary login system so we can each use our own api keys
name = str(input('\nnew script, who dis? '))
answer = str(input('%s, u have a FRED api key? ' % name))

yay = ['yes', 'yeah', 'yup', 'y', 'yuh', 'of course', 'duh', 'yay']
nay = ['no', 'nah', 'nope', 'n', 'naw', 'negative', 'kinda', 'well...']

for response in range(0, len(yay)):
    if answer.lower() == yay[response]:
        key = str(input('enter ur FRED api key: '))
        fred = Fred(api_key=key)
        x = 1
        break

    elif answer.lower() == nay[response]:
        print('u should get one using the link in the instructions')
        x = 0
        break

    else:
        x = 0


# this conditional houses our work
if x == 1:
    # I eventually want to iterate this process so you can manually input any
    # amount of datasets as long as they exist in FRED

    '''
    txt = str(input('which FRED datasets u want? '))
    txt_nospaces = txt.replace(' ', '')
    datasets = txt_nospaces.split(',')
    '''

    # now this is where I think I fucked up but I don't know for sure
    # I think I can use a .append to create a list of series, but with the
    # way the api calls each series I have to be careful about iterating

    '''
    ser = fred.get_series(datasets[0]).to_frame()
    df_init = ser.to_frame(name=datasets[0])

    for s in datasets:
        if datasets.index(s) == 0:
            continue

        ser_loop = fred.get_series(datasets[s])
        df_loop = ser_loop.to_frame(name=datasets[s])

        if datasets.index(s) == 1:
            df1 = df_init.join(df_loop)

        elif datasets.index(s) > 1:
            df = df1.join(df_loop)
    '''

    # or maybe I could try something like this... I hope...

    '''
    for y in datasets:
        ser_alt = ['']
        ser_alt.append(fred.get_series(datasets[y]))
    df_alt = df[0].join(df[1:])
    '''

    # take the series from FRED and convert it to a ts data frame
    ser1 = fred.get_series('GDP')
    df1 = ser1.to_frame(name='GDP')
    ser2 = fred.get_series('CPIAUCSL')
    df2 = ser2.to_frame(name='CPI')

    # join that shit
    df = df1.join(df2)

    # print that shit
    print(df.tail(10))

    # regress that shit
    lm = smf.ols('GDP ~ CPI', data=df).fit()


    # a quick breusch pagan test
    bptest = sms.het_breuschpagan(lm.resid, lm.model.exog)

    if bptest[1] < .05:
        lmadj = smf.ols('GDP ~ CPI', data=df).fit(cov_type='HC0')
        # this is for hederoskedasticity

    else:
        lmadj = smf.ols('GDP ~ CPI', data=df).fit(cov_type='none')
        # this is for homoskedasticity

    print(lmadj.summary())
    coefficients = lmadj.params
    print('\nthese are the coefficients:\n', coefficients)

    i = 1    # i := independent vairables

    '''
    i = len(datasets)
    ''' # this bit is for when I complete the user input functionality

    if i < 2:
        if lmadj.pvalues[i] < .05:
            print('reject the null')

        else:
            print('lmao u thought')


elif x == 0:
    print('that ain\'t it cheif\nu prolly derive smallest')
    x = 0
