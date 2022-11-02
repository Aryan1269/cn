
# naive Bayes

import pandas as pd
df = pd.read_csv('play_tennis.csv')
print(df)
print('\n')
df['Play Tennis'] = df['play']
print(df)
print('\n')
df.drop(columns='Play Tennis', inplace=True)
print(df)
print('\n')
df.play.value_counts()
print(df)
print('\n')
p_yes = 9 / 14
print(p_yes)
p_no = 5 / 14
print(p_no)
# Outloo
print(pd.crosstab(df.outlook, df.play))
print('\n')
p_overcast_no = (0/5)
p_overcast_yes = (4/9)
p_Rain_no = (2/5)
p_Rain_yes = (3/9)
p_Sunny_no = (3/5)
p_Sunny_yes = (2/9)
# Temperature
print(pd.crosstab(df.temp, df.play))
print('\n')
p_cool_no = (1/5)
p_cool_yes = (3/9)
p_Hot_no = (2/5)
p_Hot_yes = (2/9)
p_Mild_no = (2/5)
p_Mild_yes = (4/9)
# Humidity
print(pd.crosstab(df.humidity, df.play))
print('\n')
p_high_no = (4/5)
p_high_yes = (3/9)
p_normal_no = (1/5)
p_normal_yes = (6/9)
# Wind
print(pd.crosstab(df.wind, df.play))
print('\n')
p_strong_yes = 3/9
p_strong_no = 3/5
p_weak_yes = 6/9
p_weak_no = 2/5
# problem 1
print('Problem 1')
#outlook = sunny, Temp = hot , humidity = high, wind = weak
p_yes_os_th_hh_ww = p_yes*p_Sunny_yes*p_Hot_yes*p_high_yes*p_weak_yes
print(p_yes_os_th_hh_ww)
p_no_os_th_hh_ww = p_no*p_Sunny_no*p_Hot_no*p_high_no*p_weak_no
print(p_no_os_th_hh_ww)
print('\n')
# problem 2
print('Problem 2')
#outlook = Overcast, Temp = cold , humidity = low, wind = weak
p_yes_oo_tc_hl_ww = p_yes*p_overcast_yes*p_cool_yes*p_normal_yes*p_weak_yes
print(p_yes_oo_tc_hl_ww)
p_no_oo_tc_hl_ww = p_no*p_overcast_no*p_cool_no*p_normal_no*p_weak_no
print(p_no_oo_tc_hl_ww)
