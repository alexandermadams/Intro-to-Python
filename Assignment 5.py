# -*- coding: utf-8 -*-
#Import and format data per example
    import pandas as pd
    
    dp = '\\Users\\alexa\\Documents\\Grad School\\BIS 497\\PStudent2020\\Intro-to-Python\\'
    
    filep = dp+ 'Yellow_Sample.csv'
    
    # Read in csv file
    YT = pd.read_csv(filep)
    
    # Use pd.set_option to apply the format globally:
    pd.set_option('display.float_format', lambda x: '%.5f' % x)
    
    YT[['total_amount','VendorID']].astype('category').memory_usage(deep=True)
    
    # Converting columns to more usable types
    YT['pickup'] = pd.to_datetime(YT['tpep_pickup_datetime'],
                                  infer_datetime_format=True)
    del YT['tpep_pickup_datetime']
    YT['dropoff'] = pd.to_datetime(YT['tpep_dropoff_datetime'],
                                  infer_datetime_format=True)
    del YT['tpep_dropoff_datetime']
    YT['duration'] = YT['dropoff'] - YT['pickup']

# Assignment 5: Curate Data Per Lab Criteria
    # Retain Trip Distance <= 100
    YT['trip_distance'].describe()
    YT['valid'] = YT['trip_distance'] <= 100
    YT[['trip_distance','valid']].head()
    YT['trip_distance'].describe()
    YT = YT[YT.valid == True]
    YT['trip_distance'].describe()
    
    #Retain Passenger > 0
    YT['passenger_count'].describe()
    YT['valid'] = YT['passenger_count'] > 0
    YT = YT[YT.valid == True]
    YT['passenger_count'].describe()
    
    #Retain Trip Distance > 0
    YT['trip_distance'].describe()
    YT['valid'] = YT['trip_distance'] > 0
    YT = YT[YT.valid == True]
    YT['trip_distance'].describe()
    
    #Retain Fare >0 but less than 10,000
    YT['fare_amount'].describe()
    YT['valid'] = YT['fare_amount'] > 0
    YT = YT[YT.valid == True]
    YT['valid'] = YT['fare_amount'] <1000
    YT = YT[YT.valid == True]
    YT['fare_amount'].describe()
    
    #Provide Descriptive Data
    YT.describe()

    # Saving the altered data set
    YT.to_csv('YT_curated.csv', index = False)
