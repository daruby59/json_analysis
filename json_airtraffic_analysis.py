from __future__ import division
import math
import json
import sys
#
# three arguments/parameters are  expected: 1) file name 2) sub-group identifier field:sub-field for analysis
# and 3) the date-period for analysis year:month
#
xfile = str(sys.argv[1])
ftest = str(sys.argv[2])
ctest = str(sys.argv[3])
#
def main() :
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
   if (ftest.find(":") == -1):
      characteristic.append("flights")
      characteristic.append("delayed")
      print "Field: ",characteristic[2]
      print "Sub-field: ",characteristic[3]
   if (ftest.find(":") > -1) :
      temp = ftest.split(":")
      characteristic.append(temp[0])
      characteristic.append(temp[1])
      print "Field: ",characteristic[2]
      print "Sub-field: ",characteristic[3]
   #
   # open the file -- first argument
   #
   with open(xfile+".json") as jdata :
      yy = json.load(jdata)
   print "* Total file number of observations: ",len(yy)," *" 
   #
   # break down attributes... 'input_main' is a subset of the full data array containing data for a particular month or all data.
   #
   input_main = []
   if (characteristic[0] == "all") :
       input_main = yy
   #
   if (characteristic[0] <> "all") : 
       for i in range(len(yy)) :
         if (str(yy[i]['time']['year']) == characteristic[0] and str(yy[i]['time']['month']) == characteristic[1]) :
             input_main.append(yy[i])
   #
   # initialize arrays / Lists for future use
   #
   airports = []
   airport_index = []
   carriers = []
   carrier_index = []
   carrier_name = []
   xx = []
   xy = []
   xz = []
   #
   print characteristic
   print "* Number of filtered observations: ",len(input_main)
   #
   # the following commands reads through the data file and isolates unique occurrences of each airport.
   #
   for i in range(len(input_main)) :
     airports.append(input_main[i]['airport']['code'])
   xx = list(set(airports)) 
   xx.sort()
   print "Airports ("+str(len(xx))+"): ",xx
   #
   # and do the same for unique airline carriers [codes]
   #
   for i in range(len(input_main)) :
      carriers.append(input_main[i]['carrier']['code'])
   xy = list(set(carriers)) 
   xy.sort()
   print "Carriers ("+str(len(xy))+"): ",xy
   #
   # isolate carriers [names] and match with the unique set of carrier codes
   #
   xz = ["" for j in range(len(xy))]
   for j in range(len(xy)):
     for i in range(len(input_main)) :
       if (input_main[i]['carrier']['code'] == xy[j]) :
           xz[j] = (input_main[i]['carrier']['name'])
   print "Carrier names ("+str(len(xz))+"): ",xz
   #
   record_count = [[0 for k in range(len(xx))] for j in range(len(xy))]
   sum_x = [[0 for k in range(len(xx))] for j in range(len(xy))]
   sum_y = [[0 for k in range(len(xx))] for j in range(len(xy))]
   sum_total = 0
   carrier = []
   record_date = []
   #
   if (characteristic[0] == "all") :
       for k in range(len(xx)) :
         for j in range(len(xy)) :
           for i in range(len(input_main)) :
             if ((input_main[i]['airport']['code']) == xx[k] and (input_main[i]['carrier']['code']) == xy[j]):
                  record_count[j][k] = record_count[j][k]+1
                  airports.append(input_main[i]['airport']['code'])
                  carrier.append(input_main[i]['carrier']['code'])
                  carrier_name.append(input_main[i]['carrier']['name'])
                  sum_y[j][k] = sum_y[j][k] + (input_main[i]['statistics']['flights']['total'])
                  sum_x[j][k] = sum_x[j][k] + (input_main[i]['statistics'][characteristic[2]][characteristic[3]])
                  sum_total = sum_total + (input_main[i]['statistics']['flights']['total'])
   #
   if (characteristic[0] <> "all") :
       for k in range(len(xx)) :
         for j in range(len(xy)) :
           for i in range(len(input_main)) :
             if ((input_main[i]['airport']['code']) == xx[k] and (input_main[i]['carrier']['code']) == xy[j]):
                 record_count[j][k] = record_count[j][k]+1
                 airports.append(input_main[i]['airport']['code'])
                 carrier.append(input_main[i]['carrier']['code'])
                 carrier_name.append(input_main[i]['carrier']['name'])
                 record_date.append(input_main[i]['time']['label'])
                 #
                 sum_y[j][k] = sum_y[j][k] + (input_main[i]['statistics']['flights']['total'])
                 sum_x[j][k] = sum_x[j][k] + (input_main[i]['statistics'][characteristic[2]][characteristic[3]])
                 sum_total = sum_total + (input_main[i]['statistics']['flights']['total'])
   #
   h = open("testfile5.html","w+")
   h.write("<html>\n")
   h.write("<head>\n")
   h.write("<title>Air Traffic Analysis</title>\n")
   h.write("</head>\n")
   h.write("<body>\n") 
   #
   h.write("Air Traffic: "+str(characteristic[0])+" : "+str(characteristic[1])+"<br/> # observations: "+str(len(input_main))+"<br/>")
   h.write(" Total # of flights: "+str(sum_total)+"<br/>")
   h.write("* "+str(characteristic[2])+" : "+str(characteristic[3])+"\n")
   h.write("<table border = \"1\" cellspacing = \"0\" cellpadding = \"1\"><tr>\n")
   h.write("<td style = \"background: #FFFFFF; \" width=\"75\" align=\"right\">0.0</td>\n")
   h.write("<td style = \"background: #BDF4CB; \" width=\"75\" align=\"right\">0.01 - 0.10</td>\n")
   h.write("<td style = \"background: #E1E1FF; \" width=\"75\" align=\"right\">0.11 - 0.20</td>\n")
   h.write("<td style = \"background: #DBBFF7; \" width=\"75\" align=\"right\">0.21 - 0.30</td>\n")
   h.write("<td style = \"background: #FF9797; \" width=\"75\" align=\"right\">0.31+</td>\n")
   h.write("</tr></table>")
   h.write("<table border = \"1\" cellspacing = \"0\" cellpadding = \"1\">\n")
   h.write("<tr><td width=\"75\"><b>Airline: </b></td>\n")
   for j in range(len(xy)) :
     h.write("<td style = \"background: #efefef;\"width=\"75\" valign= \"top\" align = \"center\">"+str(xz[j])+"</td>\n")
   h.write("</tr>\n<tr><td width=\"75\"><b>Airport</b></td>\n")
   for j in range(len(xz)) :
     h.write("<td style = \"background: #dedede;\" width=\"75\" align = \"center\"><b>"+str(xy[j])+"</b></td>\n")
   h.write("</tr>\n")
   #
   # based on the value of each calculated result (airport-airline), we color code the cell to discriminate among differences
   #
   mean = 0
   for k in range(len(xx)) :
     h.write("<tr><td>"+str(xx[k])+"</td>\n")
     for j in range(len(xy)) :
       mean = 0.0
       if (record_count[j][k]>0) :
           mean = sum_x[j][k]/(sum_y[j][k])
       if ((mean) > 0.30) :
           h.write("<td style = \"background: #FF9797; \" align=\"right\">"+str(round(mean,3))+"</td>\n")
       if ((mean) > 0.20 and mean <=0.30) :
           h.write("<td style = \"background: #DBBFF7; \" align=\"right\">"+str(round(mean,3))+"</td>\n")
       if ((mean) > 0.10 and mean <= 0.20) :
           h.write("<td style = \"background: #E1E1FF; \" align=\"right\">"+str(round(mean,3))+"</td>\n")
       if ((mean) > 0.0 and mean <=0.10) :
           h.write("<td style = \"background: #BDF4CB; \" align=\"right\">"+str(round(mean,3))+"</td>\n")
       if ((mean) == 0.0) :
           h.write("<td align=\"right\">"+str(round(mean,3))+"</td>\n")
   h.write("</tr></table\n")
   h.write("</body>\n")
   h.write("</html\n") 
   #
   h.close()
   #
if __name__ == "__main__" :
   main()