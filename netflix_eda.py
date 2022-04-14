import pandas as pd
import numpy as np
import re

df=pd.read_csv("~/documents/info_4206/netflix_titles.csv")

df['date_added'] = df['date_added'].fillna(df['date_added'].mode()[0])

date = pd.DataFrame(df['date_added'])
added = date['date_added'].str.split(', ',expand = True)
date['MD'] = added[0]
date['Year'] = added[1]
date.head()

def get_month(row):
    mon = row['MD'].split(' ')
    if len(mon) == 2:
        return mon[0]
    else:
        return mon[1]

def get_day(row):
    mon = row['MD'].split(' ')
    if len(mon) == 2:
        return mon[1]
    else:
        return mon[2]

date['Month'] = date.apply(get_month,axis=1)
date['Day'] = date.apply(get_day,axis=1)
date = date.drop(['date_added','MD'], axis=1, errors='ignore')

#df['year_added']=str.split(',', 1).str

stats=df.describe()
stat=date.describe()

print(date.head())
print(df)
print(stats)

