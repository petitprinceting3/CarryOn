import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import skew
from scipy.stats import kurtosis
import statistics

# from scipy import stats

# import dataframe
data = pd.read_csv("https://raw.githubusercontent.com/J-tin/CarryOn/master/data.csv")
print(data.columns)  # get column index获取列索引值
print(data.index)  # get range index获取行索引值
year_return = data[' value']
year = data['date']

# devide year_return into 13 groups according to the x-axis-scale

group1 = []
group2 = []
group3 = []
group4 = []
group5 = []
group6 = []
group7 = []
group8 = []
group9 = []
group10 = []
group11 = []
group12 = []
group13 = []

group_number = list(range(99))

for n in group_number:
    yr_return = data.at[n, ' value']

    if yr_return >= -60 and yr_return <= -50:
        year_name = data.at[n, 'date']
        group1.append(year_name)

    elif yr_return >= -50 and yr_return <= -40:
        year_name = data.at[n, 'date']
        group2.append(year_name)

    elif yr_return >= -40 and yr_return <= -30:
        year_name = data.at[n, 'date']
        group3.append(year_name)
    elif yr_return >= -30 and yr_return <= -20:
        year_name = data.at[n, 'date']
        group4.append(year_name)
    elif yr_return >= -20 and yr_return <= -10:
        year_name = data.at[n, 'date']
        group5.append(year_name)
    elif yr_return >= -10 and yr_return <= -0:
        year_name = data.at[n, 'date']
        group6.append(year_name)
    elif yr_return >= 0 and yr_return <= 10:
        year_name = data.at[n, 'date']
        group7.append(year_name)
    elif yr_return >= 10 and yr_return <= 20:
        year_name = data.at[n, 'date']
        group8.append(year_name)
    elif yr_return >= 20 and yr_return <= 30:
        year_name = data.at[n, 'date']
        group9.append(year_name)
    elif yr_return >= 30 and yr_return <= 40:
        year_name = data.at[n, 'date']
        group10.append(year_name)
    elif yr_return >= 40 and yr_return <= 50:
        year_name = data.at[n, 'date']
        group11.append(year_name)
    elif yr_return >= 50 and yr_return <= 60:
        year_name = data.at[n, 'date']
        group12.append(year_name)
    elif yr_return >= 60 and yr_return <= 70:
        year_name = data.at[n, 'date']
        group13.append(year_name)

# draw the plot

xbins = np.linspace(-60, 70, 14)
plt.xticks(xbins,
           ('-60%', '-50%', '-40%', '-30%', '-20%', '-10%', '0%', '10%', '20%', '30%', '40%', '50%', '60%', '70%'))
ybins = np.linspace(1, 26, 26)
plt.yticks(ybins, ('1 (1.0%)', '2 (2.0%)', '3 (3.0%)', '4 (4.0%)', '5 (5.0%)', '6 (6.0%)', '7 (7.0%)',
                   '8 (8.0%)', '9 (9.0%)', '10 (10.0%)', '11 (11.0%)', '12 (12.0%)', '13 (13.0%)', '14 (14.0%)',
                   '15 (15.0%)', '16 (16.0%)', '17 (17.0%)', '18 (18.0%)', '19 (19.0%)', '20 (20.0%)', '21 (21.0%)',
                   '22 (22.0%)', '23 (23.0%)', '24 (24.0%)', '25 (25.0%)', '26 (26.0%)'))

plt.xlabel = ("Returns DJIA in %")
plt.ylabel = ('Number of Observations(Probability in %)')
plt.title('Dow Jones Industrial Average 1920 to 2019')

n, bins, patches = plt.hist(year_return, xbins, color='#0504aa', alpha=0.75)

# tag year labels

groups = [group1, group2, group3, group4, group5, group6, group7, group8, group9, group10, group11, group12, group13]

for i in range(len(groups)):
    for n, year in enumerate(groups[i]):
        plt.text(-60 + 10 * i, n, str(year), color='white')

plt.grid(True)

# add the stat summary textbox
pos=len(list(filter(lambda x: (x >= 0), year_return)))
neg=len(list(filter(lambda x: (x < 0), year_return)))
mean=year_return.mean
mini=np.minimum(year_return)
quar25= np.quantile(year_return, .25)
quar50= np.quantile(year_return, .5)
quar75= np.quantile(year_return, .75)
maxm=np.maximum(year_return)
sta_dev=np.std(year_return)
skewness=skew(year_return)
kurto=kurtosis(year_return)

ss=[pos,neg,mean,mini,quar25,quar50,quar75,maxm,sta_dev,skewness,kurto]
text = 'Time period:' + '1921-2019'\
       '\n Index:' + 'DJIA'\
       '\n Number of years:'+ '99' \
       '\n Number of pos. years:'  + ss[0]\
       '\n Number of neg. years:' + ss[1]\
       '\n Mean:' + str (ss[2])+'%' \
       '\n Minimum:' + str (ss[3])+'%'\
       '\n 25%-Quartile:' + str(ss[4]+'%')\
       '\n 50%-Quartile:' + str(ss[5]+'%')\
       '\n 75%-Quartile:' + str(ss[6]+'%')\
       '\n Maximum:' + str(ss[7])+'%' \
       '\n Standard dev:' + str(ss[8])+'%' \
       '\n Skewness:' +  str (ss[9])+'%'\
       '\n Kurtosis:' + str(ss[10]) +'%'\


plt.text(-60, 15, str(text), size=5, bbox=dict(fc="none"), multialignment="left")

plt.show()
