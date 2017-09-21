from __future__ import division
import urllib2
import math
import json
import sys
#
# two arguments expected: 1) file name 2) sub-group identifier key:value
#
xfile = str(sys.argv[1])
# ctest = str(sys.argv[2])
# ctest = str(sys.argv[3])
# ftest = str(sys.argv[2])
#
# key work here
#
# (1)
def mean(x):
    count = len(x)
    sumx = sum(x)
    return sumx/count
# (2)
def data_range(x):
    return max(x) - min(x)
# (3)
def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]
# (4)
def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n)
# (5) 
def standard_deviation(x):
    return math.sqrt(variance(x))
# (6)
def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))
# (7)
def sum_of_squares(v):
    return dot(v, v)
# (8)
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)
# (9)
def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0 # if no variation, correlation is zero
# (10)
def predict(alpha, beta, x_i):
    return beta * x_i + alpha
# (11)
def error(alpha, beta, x_i, y_i):
    return y_i - predict(alpha, beta, x_i)
# (12)
def sum_of_squared_errors(alpha, beta, x, y):
    return sum(error(alpha, beta, x_i, y_i) ** 2
               for x_i, y_i in zip(x, y))
# (13)
def least_squares_fit(x,y):
    beta = correlation(x, y) * standard_deviation(y) / standard_deviation(x)
    alpha = mean(y) - beta * mean(x)
    return alpha, beta
# (14)
def total_sum_of_squares(y):
    return sum(v ** 2 for v in de_mean(y))
# (15)
def r_squared(alpha, beta, x, y):
    return 1.0 - (sum_of_squared_errors(alpha, beta, x, y) /
                  total_sum_of_squares(y))
# (16)
def squared_error(x_i, y_i, theta):
    alpha, beta = theta
    return error(alpha, beta, x_i, y_i) ** 2
# (17)
def total_sum_of_squares(y):
    return sum(v ** 2 for v in de_mean(y))
# (18)
def r_squared(alpha, beta, x, y):
    return 1.0 - (sum_of_squared_errors(alpha, beta, x, y) /
                  total_sum_of_squares(y))
#
# end of routines
#
def main() :
     #
     # open the file -- first argument
     #
     with open(xfile+".json") as jdata :
          yy = json.load(jdata)
     #
     input_main = yy
     key_fields = []
     sub_keys = []
     # ---------------------------------------------------------------
     # ID the key fields
     #
     key_fields = input_main[0].keys()
     print "\nKeys: ",key_fields
     # for i in range(len(key_fields)) :
     #   print "*", key_fields[i], input_main[0][key_fields[i]]
     print "***"
     density = 0
     hh_size = 0
     for i in range(len(input_main)) :
        print "\n* State: ",input_main[i]['geography']['stateName']
        print "Population: ",input_main[i]['demographics']['info']['population']
        print "Area: ",input_main[i]['demographics']['info']['totalArea']
        density = input_main[i]['demographics']['info']['population']/input_main[i]['demographics']['info']['totalArea']
        print "Population density: ",density
        print "Housing units: ",input_main[i]['demographics']['info']['housingUnits']
        hh_size = input_main[i]['demographics']['info']['population']/input_main[i]['demographics']['info']['housingUnits']
        print "Household size: ",hh_size
        print "Bachelor degree +:", input_main[i]['demographics']['education']['educationBachelorOrGreater']
        print "!* University download speed: ",input_main[i]['communityAnchorInstitutions']['universityCollegeOtherPostSecundary']['download']['downloadSpeedGr1g']

     #
     print "* Total file number of observations: ",len(yy)," *"  
if __name__ == "__main__" :
   main()