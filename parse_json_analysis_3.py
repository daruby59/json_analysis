from __future__ import division
import urllib2
import math
import json
import sys
#
# two arguments expected: 1) file name 2) sub-group identifier key:value
#
xfile = str(sys.argv[1])
ctest = str(sys.argv[2])
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
    # break down the second argument
    #
    characteristic = ["",""]
    if (ctest.find(":") == -1):
        characteristic[0] = "all"
        characteristic[1] = "all"
        print "Attribute",characteristic[0]
        print "\nValue",characteristic[1]
    if (ctest.find(":") > -1) :
        characteristic = ctest.split(":")
        print "Attribute",characteristic[0]
        print "\nValue",characteristic[1]
    #
    # open the file -- first argument
    #
    with open(xfile+".json") as jdata :
         yy = json.load(jdata)
    print "* Total file number of observations: ",len(yy)," *"     
    #
    # break down attributes... 'input_main' is a subset of the full data array
    #
    input_main = []
    if (characteristic[0] == "all") :
        input_main = yy
    #    
    if (characteristic[0] <> "all") :    
        for i in range(len(yy)) :
          if (yy[i][characteristic[0]]['code'] == characteristic[1]) :
              # print "Value: ",yy[i][characteristic[0]]
              input_main.append(yy[i])
    #
    airports = []
    xx = []
    #
    delayed = []
    cancelled = []
    total_flight = []
    ontime = []
    diverted = []
    ratio_delayed = []
    #
    print characteristic[0],characteristic[1] 
    print "* Number of filtered observations: ",len(input_main)  
    #
    for i in range(len(input_main)) :
         airports.append(input_main[i]['airport']['code'])
    xx = list(set(airports))     
    xx.sort()
    print "Airports: ",xx
    #
    # json structure
    #
    # "statistics": {
    #  "flights": {
    #    "cancelled": 5, 
    #    "on time": 561, 
    #    "total": 752, 
    #    "delayed": 186, 
    #    "diverted": 0
    #  }, 
    #  "# of delays": {
    #    "late aircraft": 18, 
    #    "weather": 28, 
    #    "security": 2, 
    #    "national aviation system": 105, 
    #    "carrier": 34
    #  }, 
    #  "minutes delayed": {
    #    "late aircraft": 1269, 
    #    "weather": 1722, 
    #    "carrier": 1367, 
    #    "security": 139, 
    #    "total": 8314, 
    #    "national aviation system": 3817
    #  }
    # }, 
    #
    delayed_aircraft = []
    delayed_weather = []
    delayed_carrier = []
    delayed_security = []
    delayed_nas = []
    #
    minutes_aircraft = []
    minutes_weather = []
    minutes_carrier = []
    minutes_security = []
    minutes_nas = []
    #
    carrier = []
    record_date = []
    #
    if (characteristic[0] == "all") :
      for k in range(len(xx)) : 
        for i in range(len(input_main)) :
          if (input_main[i]['airport']['code'] == xx[k]):
            airports.append(input_main[i]['airport']['name'])
            carrier.append(input_main[i]['carrier']['name'])
            record_date.append(input_main[i]['time']['label'])
            delayed.append(input_main[i]['statistics']['flights']['delayed'])
            diverted.append(input_main[i]['statistics']['flights']['diverted'])
            cancelled.append(input_main[i]['statistics']['flights']['cancelled'])
            ontime.append(input_main[i]['statistics']['flights']['on time'])
            total_flight.append(input_main[i]['statistics']['flights']['total'])
            #
            delayed_aircraft.append(input_main[i]['statistics']['# of delays']['late aircraft'])
            delayed_weather.append(input_main[i]['statistics']['# of delays']['weather'])
            delayed_carrier.append(input_main[i]['statistics']['# of delays']['carrier'])
            delayed_security.append(input_main[i]['statistics']['# of delays']['security'])
            delayed_nas.append(input_main[i]['statistics']['# of delays']['national aviation system'])
            #
            minutes_aircraft.append(input_main[i]['statistics']['minutes delayed']['late aircraft'])
            minutes_weather.append(input_main[i]['statistics']['minutes delayed']['weather'])
            minutes_carrier.append(input_main[i]['statistics']['minutes delayed']['carrier'])
            minutes_security.append(input_main[i]['statistics']['minutes delayed']['security'])
            minutes_nas.append(input_main[i]['statistics']['minutes delayed']['national aviation system'])
    #    
    if (characteristic[0] <> "all") :    
      for k in range(len(xx)):
        for i in range(len(input_main)) :
          if (input_main[i]['airport']['code'] == xx[k]):
            delayed.append(input_main[i]['statistics']['flights']['delayed'])
            diverted.append(input_main[i]['statistics']['flights']['diverted'])
            ontime.append(input_main[i]['statistics']['flights']['on time'])
            total_flight.append(input_main[i]['statistics']['flights']['total'])
            cancelled.append(input_main[i]['statistics']['flights']['cancelled'])
            ratio_delayed.append((input_main[i]['statistics']['flights']['delayed'])/(input_main[i]['statistics']['flights']['total']))
        print "Airport:",xx[k]
        mu = mean(ratio_delayed)
        sigma = standard_deviation(ratio_delayed)
        print "Mean delay: ",str(round(mu,3))
        mu = mean(diverted)
        sigma = standard_deviation(diverted)
        print "Mean diverted: ",str(round(mu,3))
        mu = mean(cancelled)
        sigma = standard_deviation(cancelled)
        print "Mean cancelled: ",str(round(mu,3))
      #
    g = open("testfile9.txt","w+")
    #
    g.write("Number of obs: "+str(len(input_main))+"\n")
    for k in range(len(xx)) :
      for i in range(len(input_main)) :
        if (input_main[i]['airport']['code'] == xx[k]):
          g.write("*"+record_date[i]+","+str(airports[k])+","+str(carrier[i])+","+str(delayed[i])+","+str(diverted[i])+","+str(ontime[i])+","+str(cancelled[i])+","+str(total_flight[i])+",")
          g.write(""+str(delayed_aircraft[i])+","+str(delayed_weather[i])+","+str(delayed_carrier[i])+","+str(delayed_security[i])+","+str(delayed_nas[i])+",")
          g.write(""+str(minutes_aircraft[i])+","+str(minutes_weather[i])+","+str(minutes_carrier[i])+","+str(minutes_security[i])+","+str(minutes_nas[i])+"\n")
    g.close()  
    # doit()
#
if __name__ == "__main__" :
   main()