from __future__ import division
import json
import sys
#
xfile = str(sys.argv[1])
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
    sub_sub_keys = []
    # ---------------------------------------------------------------
    # ID the key fields
    #
    h = open(xfile+"_bdf3.html","w+")
    h.write("<html>\n")
    h.write("<head><title>JSON Data Dictionary</title></head>\n")
    h.write("<body>\n")
    #
    # keys = [[]]
    keys = [["" for i in range(5)] for j in range(100)]
    keys[0] = input_main[0].keys()
    #
    h.write("<b>Data Dictionary</b> for: "+xfile+".json<br/>\n")
    for i in range(len(keys[0])) :
        print "",i,keys[0][i]
        h.write(""+str(i)+": "+str(keys[0][i])+"<br/>\n")
        #
        temp = str(input_main[0][keys[0][i]])
        if (temp.find("{") > -1) :
    	    keys[1] = input_main[0][keys[0][i]].keys()
            h.write("<blockquote>\n")
            for j in range(len(keys[1])):
               print "      ",j,keys[1][j]
               h.write(""+str(j)+": "+str(keys[1][j])+"<br/>\n")
               #
               temp = str(input_main[0][keys[0][i]][keys[1][j]])
               if (temp.find("{") > -1) :
                   keys[2] = input_main[0][keys[0][i]][keys[1][j]].keys()
                   h.write("<blockquote>\n")
                   for k in range(len(keys[2])) :
                       print "          ",k,keys[2][k]
                       h.write(""+str(k)+": "+str(keys[2][k])+"<br/>\n")
                   h.write("</blockquote>\n")
                   #
                   temp = str(input_main[0][keys[0][i]][keys[1][j]][keys[2][k]])
                   if (temp.find("{") > -1) :
                       keys[3] = input_main[0][keys[0][i]][keys[1][j]][keys[2][k]].keys()
                       h.write("<blockquote>\n")
                       for m in range(len(keys[3])) :
                          print "          ",i,keys[3][m]
                          h.write(""+str(i)+": "+str(keys[3][m])+"<br/>\n")
                       h.write("</blockquote>\n")
            h.write("</blockquote>\n")
    #
    h.write("</body>\n")
    h.write("</html>\n")
    h.close()
if __name__ == "__main__" :
  main()