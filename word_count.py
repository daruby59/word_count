import urllib2
import sys
import json

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
#
def publishResults(count, xx2):
    f = open(xfile+"07_07_2017.html","w+")
    f.write("<html>\n")
    f.write("<body width=\"800px\">")
    f.write("<div style=\"display:block; width: 800px;\">")
    #
    j = 1
    k = 0
    xx2.sort()
    word_instance   = ["" for x_i in range(count)]
    word_count = [0 for x_i in range(count)]
    for i in range(count-1):
        if (xx2[i] <> xx2[i+1]):
             word_instance[k] = xx2[i]
             word_count[k] = j
             j = 1
             k = k+1
        if (xx2[i] == xx2[i+1]):
             j=j+1
    print "Word count: ", count
    print "Unique words: ",k
    for i in range(k):
         # print word_instance[i], word_count[i]
         fsize = 36-word_count[i]*3
         f.write(" <span style = \"font-size: "+str(fsize)+"px; color: navy;\">"+word_instance[i]+"</span> ")
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
    xx2 = xx.split(" ")
    count = len(xx2)
    publishResults(count, xx2)
    #
if __name__ == "__main__":
    main()