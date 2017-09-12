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
# def doit() :
  
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
    sum_delayed = 0
    sum_cancelled = 0
    for i in range(len(input_main)) :
      temp = input_main[i] 
      # print "*",(temp['statistics']['flights']['delayed'])
      # print "\n*",(temp['statistics']['flights']['cancelled'])
      sum_delayed = sum_delayed+(temp['statistics']['flights']['delayed'])
      sum_cancelled = sum_cancelled +(temp['statistics']['flights']['cancelled'])
    print characteristic[0],characteristic[1] 
    print "# observations: ",len(input_main)  
    print "Average delay: ",sum_delayed/len(input_main)
    print "Average # cancelled: ",sum_cancelled/len(input_main)  
    # doit()
#
if __name__ == "__main__" :
   main()