import pandas as pd
import matplotlib as mpl
import numpy as np
import math

df = pd.read_csv('kickingStats2019.csv')

under20a = df['0-19'].sum()
under20m = df['0-19.1'].sum()
leagueUnder20 = under20a/under20m

under30a = df['20-29'].sum()
under30m = df['20-29.1'].sum()
leagueUnder30 = under30a/under30m

under40a = df['30-39'].sum()
under40m = df['30-39.1'].sum()
leagueUnder40 = under40a/under40m

under50a = df['40-49'].sum()
under50m = df['40-49.1'].sum()
leagueUnder50 = under50a/under50m

over49a = df['50+'].sum()
over49m = df['50+.1'].sum()
leagueOver49 = over49a/over49m

for index, row in df.iterrows():
    if(math.isnan(row['0-19'])):
        under20a = 0
        under20m = 0
        under20Percentage = 0
    else:
        under20a = row['0-19']
        under20m = row['0-19.1']
        under20Percentage = under20a/under20m

    if(math.isnan(row['20-29'])):
        under30a = 0
        under30m = 0
        under30Percentage = 0
    else:
        under30a = row['20-29']
        under30m = row['20-29.1']
        under30Percentage = under30a/under30m

    if(math.isnan(row['30-39'])):
        under40a = 0
        under40m = 0
        under40Percentage = 0
    else:
        under40a = row['30-39']
        under40m = row['30-39.1']
        under40Percentage = under40a/under40m

    if(math.isnan(row['40-49'])):
        under50a = 0
        under50m = 0
        under50Percentage = 0
    else:
        under50a = row['40-49']
        under50m = row['40-49.1']
        under50Percentage = under50a/under50m

    if(math.isnan(row['50+.1'])):
        over50a = 0
        over50m = 0
        over50Percentage = 0
    else:
        over49a = row['50+']
        over49m = row['50+.1']
        over49Percentage = over49a/over49m
    
    totalKicks = under20a + under30a + under40a + under50a + over49a

    wFGRAA = (under20Percentage - leagueUnder20)*(under20a/totalKicks)+(under30Percentage - leagueUnder30)*(under30a/totalKicks)+(under40Percentage - leagueUnder40)*(under40a/totalKicks)+(under50Percentage - leagueUnder50)*(under50a/totalKicks)+(over49Percentage - leagueOver49)*(over49a/totalKicks)
    print(row['Player'], under20Percentage, wFGRAA)
