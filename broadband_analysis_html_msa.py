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
# ftest = str(sys.argv[3])
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
     #
     # break down the second and third argument (** do this on a split -- type:year:month...
     #
     characteristic = ["","","","",""]
     temp = ["",""]
     if (ctest.find(":") == -1):
        characteristic[0] = "all"
        characteristic[1] = "all"
        print "Year",characteristic[0]
        print "Month",characteristic[1]
     if (ctest.find(":") > -1) :
        characteristic = ctest.split(":")
        print "Year",characteristic[0]
        print "Month",characteristic[1]
     #
     density = 0
     hh_size = 0
     download_speed = 0
     f1 = 'communityAnchorInstitutions'
     f2 = 'universityCollegeOtherPostSecundary'
     f3 = 'download'
     #
     h = open(xfile+".html", "w+")
     #
     h.write("<html>\n")
     h.write("<head>\n")
     h.write("<title>Broadband Analysis by State</title>\n")
     h.write("</head>\n")
     h.write("<body>\n") 
     #
     h.write("<table border = \"1\" cellspacing = \"0\" cellpadding = \"1\"><tr>\n")
     h.write("<td style = \"background: #FFFFdF; \" width=\"300\" align=\"center\"><b>MSA</b></td>\n")
     h.write("<td style = \"background: #FFFFdF; \" width=\"100\" align=\"center\"><b>Population</b></td>\n")
     h.write("<td style = \"background: #FFFFdF; \" width=\"100\" align=\"center\"><b>Area</b></td>\n")
     h.write("<td style = \"background: #FFFFdF; \" width=\"100\" align=\"center\"><b>Density</b></td>\n")
     h.write("<td style = \"background: #FFFFdF; \" width=\"100\" align=\"center\"><b>Housing Units</b></td>\n")
     h.write("<td style = \"background: #FFFFdF; \" width=\"100\" align=\"center\"><b>Household Size</b></td>\n")
     h.write("<td style = \"background: #FFFFdF; \" width=\"100\" align=\"center\"><b>Hispanic</b></td>\n")
     h.write("<td style = \"background: #FFFFdF; \" width=\"100\" align=\"center\"><b>White</b></td>\n")
     h.write("<td style = \"background: #FFFFdF; \" width=\"100\" align=\"center\"><b>Black</b></td>\n")
     h.write("<td style = \"background: #FFFFdF; \" width=\"100\" align=\"center\"><b>Asian</b></td>\n")
     h.write("<td style = \"background: #FFFFdF; \" width=\"100\" align=\"center\"><b>Native American</b></td>\n")
     h.write("<td style = \"background: #FFFFdF; \" width=\"100\" align=\"center\"><b>Age (5-19)</b></td>\n")
     h.write("<td style = \"background: #FFFFdF; \" width=\"100\" align=\"center\"><b>Age (20 - 34)</b></td>\n")
     #
     h.write("<td style = \"background: #FFFFdF; \" width=\"100\" align=\"center\"><b>Income (below poverty)</b></td>\n")
     h.write("<td style = \"background: #FFFFdF; \" width=\"100\" align=\"center\"><b>Median Income</b></td>\n")
     #
     h.write("<td style = \"background: #FFFFdF; \" width=\"100\" align=\"center\"><b>H.S. Degree</b></td>\n")
     h.write("<td style = \"background: #FFFFdF; \" width=\"100\" align=\"center\"><b>College Degree</b></td>\n")
     h.write("<td style = \"background: #FFFFdF; \" width=\"100\" align=\"center\"><b>Download Speed 10mbps+</b></td>\n")
     h.write("</tr>\n")
     #
     for i in range(len(input_main)) :
        download_speed  = 100*(1 - (input_main[i][f1][f2][f3]['downloadSpeed768kto1pt5m'] + input_main[i][f1][f2][f3]['downloadSpeed1pt5mto3m'] 
        +input_main[i][f1][f2][f3]['downloadSpeed3mto6m'] + input_main[i][f1][f2][f3]['downloadSpeed6mto10m']))
        #
        if (download_speed <= 100.0) :
          h.write("<tr>\n")
          h.write("<td align = \"left\"><b>"+str(input_main[i]['geography']['Name'])+"</b></td>\n")
          h.write("<td align = \"right\">"+str(input_main[i]['demographics']['info']['population'])+"</td>\n")
          h.write("<td align = \"right\">"+str(round(input_main[i]['demographics']['info']['totalArea'],2))+" </td>\n")
          density = input_main[i]['demographics']['info']['population']/input_main[i]['demographics']['info']['totalArea']
          h.write("<td align = \"right\">"+str(round(density,2))+"</td>\n")
          h.write("<td align = \"right\">"+str(input_main[i]['demographics']['info']['housingUnits'])+"</td>\n")
          hh_size = input_main[i]['demographics']['info']['population']/input_main[i]['demographics']['info']['housingUnits']
          #
          h.write("<td align = \"right\">"+str(round(hh_size,1))+"</td>\n")
          h.write("<td align = \"right\">"+str(input_main[i]['demographics']['race']['hispanic'])+"</td>\n")
          h.write("<td align = \"right\">"+str(input_main[i]['demographics']['race']['white'])+"</td>\n")
          h.write("<td align = \"right\">"+str(input_main[i]['demographics']['race']['black'])+"</td>\n")
          h.write("<td align = \"right\">"+str(input_main[i]['demographics']['race']['asian/pacific-islander'])+"</td>\n")
          h.write("<td align = \"right\">"+str(input_main[i]['demographics']['race']['nativeAmerican'])+"</td>\n")
          #
          h.write("<td align = \"right\">"+str(input_main[i]['demographics']['age']['ageBetween5to19'])+"</td>\n")
          h.write("<td align = \"right\">"+str(input_main[i]['demographics']['age']['ageBetween20to34'])+"</td>\n")
          #
          h.write("<td align = \"right\">"+str(input_main[i]['demographics']['income']['incomeBelowPoverty'])+"</td>\n")
          h.write("<td align = \"right\">"+str(input_main[i]['demographics']['income']['medianIncome'])+"</td>\n")
          #
          h.write("<td align = \"right\">"+str(round(input_main[i]['demographics']['education']['educationHighSchoolGraduate']*100,2))+"%</td>\n")
          h.write("<td align = \"right\">"+str(round(input_main[i]['demographics']['education']['educationBachelorOrGreater']*100,2))+"%</td>\n")
          #
          h.write("<td align = \"right\">"+str(round(download_speed,2))+"% </td>\n")
          h.write("</tr>\n")
     #
     h.write("</table>")
     h.write("</body>")
     h.write("</html>")
     h.close()
     print "* Total file number of observations: ",len(yy)," *"  
if __name__ == "__main__" :
   main()