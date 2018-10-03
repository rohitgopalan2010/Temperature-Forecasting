# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 10:31:35 2018

@author: rohit
"""

def predictMissingTemperature(startDate, endDate, temperature, n):
    num_temp = len(temperature)
    num_days = num_temp/24
    year,month,day = startDate.split('-')
    year = int(year)
    month = int(month)
    day = int(day)
    for i in range(num_days):
        if i>=1:
            p = generate_next_date(day,month,year)
            year = p[0]
            month = p[1]
            day = p[2]

        data = []
        for j in range(24):
            data.append([year,month,day,j])


    clf = ensemble.GradientBoostingRegressor(n_estimators=30, learning_rate=1.0, max_depth=2, random_state=0,
                                                 loss='ls')
    clf.fit(data, temperature)

    year, month, day = endDate.split('-')
    year = int(year)
    month = int(month)
    day = int(day)
    for i in range(n):
        p = generate_next_date(day, month, year)
        year = p[0]
        month = p[1]
        day = p[2]
        predict_data = []
        for j in range(24):
            predict_data.append([year, month, day, j])


    predictions = clf.predict(predict_data)

    return predictions


def generate_next_date(day,month,year):

    if((year%400==0 or year%4==0) and month==2):
        next_day=day+1
        next_month=month
        next_year=year
    elif(month==2 and day==28):
        next_day=1
        next_month=month+1
        next_year=year
    elif(month==12 and day==31):
        next_day=1
        next_month=1
        next_year=year+1
    elif(day==31 ):
        next_day=1
        next_month=month+1
        next_year=year
    elif((day==30) and (month==4 or month==6 or month==9 or month==11)):
        next_day=1
        next_month=month+1
        next_year=year
    else:
        next_day=day+1
        next_month=month
        next_year=year

    return [next_year,next_month,next_day]