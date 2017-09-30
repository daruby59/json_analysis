from __future__ import division
import json
import sys
#
xfile = str(sys.argv[1])
#
def main() :
    #  
    def start(idx) :
      for i in range(len(keys[idx])) :
        #  
        print "               ",i,keys[idx][i]
        h.write(""+str(i)+": "+str(keys[idx][i])+"<br/>\n") 
        ref[idx+1] = ref[idx][keys[idx][i]]
        if (str(ref[idx+1]).find("{") > -1) :
            idx += 1
            keys[idx] = ref[idx].keys()
            h.write("<blockquote>\n")
            start(idx)  
            idx -= 1    
      h.write("</blockquote>\n")         
    #
    # open the file
    #
    with open(xfile+".json") as jdata :
         yy = json.load(jdata)
    #
    input_main = yy
    #
    # initialize the HTML
    #
    h = open(xfile+"_dictionary2.html","w+")
    h.write("<html>\n")
    h.write("<head><title>JSON Data Dictionary</title></head>\n")
    h.write("<body>\n")
    h.write("<b>Data Dictionary</b> for: "+xfile+".json<br/>\n")
    #
    # initial round of variable / key values
    #
    ref = ["" for i in range(20)]
    keys = [["" for i in range(20)] for j in range(100)]
    idx = 0
    keys[idx] = input_main[idx].keys()
    ref[idx] = input_main[idx]
    #
    # go!
    #
    start(idx)  
    #
    # close the HTML
    #      
    h.write("</body>\n")
    h.write("</html>\n")
    h.close()
    #
if __name__ == "__main__" :
  main()