import urllib2
import sys
import json
import random

xfile = str(sys.argv[1])
count = 0
tagcount = 0
xx3 = ""
xx4 = ""
xx5 = ""
temp =""
table = 0
row = 0
col = 0
#
# color references...
#
# sb_code = [0,7869463, 1270682, 1865266, 4013458, 9333913, 2461666, 4704305, 14778913, 13773105, 8684676, 999999, 555555, 0]
# rr_code =   [128, 000, 000, 000, 102, 000, 000, 255, 225, 240, 255, 224, 000]
# gg_code = [000, 153, 128, 102, 102, 000, 225, 102, 000, 240, 255, 224, 000] 
# bb_code = [000, 255, 000, 204, 255, 128, 000, 000, 000, 240, 255, 224, 000] 
color_array = ["red","maroon","magenta","orange","yellow","green","teal","olive","purple","blue","navy","aqua","gray","black"]
#
def publishResults(count, net_count, xx2):
    f = open(xfile+"07_07_2017.html","w+")
    f.write("<html>\n")
    f.write("<body width=\"800px\">")
    f.write("<div style=\"display:block; width: 800px;\">")
    #
    j = 1
    k = 0
    xx2.sort()
    for i in range(net_count):
        xx2[i] = str.lower(xx2[i])
    word_instance   = ["" for x_i in range(net_count)]
    word_count = [0 for x_i in range(net_count)]
    for i in range(net_count-1):
        if ((xx2[i] <> xx2[i+1])):
             word_instance[k] = xx2[i]
             word_count[k] = j
             j = 1
             k = k+1
        if ((xx2[i] == xx2[i+1])):
             j=j+1
    print "Total Word count: ", count
    print "Net Word count: ",net_count
    print "Unique words: ",k
    for i in range(k):
         # print word_instance[i], word_count[i]
         fsize = word_count[i]*4 +14
         ccx = int(random.random()*14)
         color_choice = color_array[ccx]
         f.write(" <span style = \"font-size: "+str(fsize)+"px; color: "+color_choice+";\">"+word_instance[i]+"</span> ")
    f.write("</div>")
    f.write("</body>")
    f.write("</html>")
    f.close()
    #
def main():
    g = open(xfile+".txt", 'r')
    xx = g.read()
    xx = xx.replace(".","")
    xx = xx.replace(",","")
    xx = xx.replace("  "," ")
    xx = xx. replace("/'","")
    xx = xx.replace("/n","")
    xx = xx.replace("(","")
    xx = xx.replace(")","")
    xx1 = xx
    #
    xx1 = xx1.replace(" and "," ")
    xx1 = xx1.replace(" in "," ")
    xx1 = xx1.replace(" or "," ")
    xx1 = xx1.replace(" to "," ")
    xx1 = xx1.replace(" too "," ")
    xx1 = xx1.replace(" not "," ")
    xx1 = xx1.replace(" that "," ")
    xx1 = xx1.replace(" the "," ")
    xx1 = xx1.replace(" with "," ")
    xx1 = xx1.replace(" our "," ")
    xx1 = xx1.replace(" we "," ")
    xx1 = xx1.replace("We ","")
    xx1 = xx1.replace("And ","")
    xx1 = xx1.replace("The ","")
    xx1 = xx1.replace("Our ","")
    xx1 = xx1.replace("In ","")
    xx1 = xx1.replace(" I "," ")
    xx1 = xx1.replace(" their "," ")
    xx1 = xx1.replace(" there "," ")
    xx1 = xx1.replace(" these "," ")
    xx1 = xx1.replace(" has "," ")
    xx1 = xx1.replace(" have "," ")
    xx1 = xx1.replace(" had "," ")
    xx1 = xx1.replace(" are "," ")
    xx1 = xx1.replace(" is "," ")
    xx1 = xx1.replace(" it "," ")
    xx1 = xx1.replace(" no "," ")
    xx1 = xx1.replace(" if "," ")
    xx1 = xx1.replace(" of "," ")
    xx1 = xx1.replace(" for "," ")
    xx1 = xx1.replace(" a "," ")
    xx1 = xx1.replace(" an "," ")
    #
    xx2 = xx.split(" ")
    count = len(xx2)
    xx2 = xx1.split(" ")
    net_count = len(xx2)
    publishResults(count,net_count, xx2)
    #
if __name__ == "__main__":
    main()