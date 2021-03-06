#import necessary python libraries
import pandas as pd
import reliability_stability_pkg as rs
	
#import data set
data = pd.read_csv('BodyFat.csv')

#define columns based on input column headers
column_one = data.loc[:, 'BICEPS']
column_two = data.loc[:, 'FOREARM']
column_three = data.loc[:, 'WRIST']

reliability_test_value = float('%.3f'%(rs.calc_reliability(column_one, column_two, column_three)))
assert reliability_test_value == 0.628
