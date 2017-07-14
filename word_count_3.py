from __future__ import division
import sys
import random
# 
xfile = str(sys.argv[1])
count = 0
#
# color references...
#
color_array = ["red","maroon","magenta","orange","#6094DB","green","teal","olive","purple","blue","navy","#0088dd","#6755E3","#B6BA18","black"]
#
def publishResults(count, net_count, xx2):
    f = open(xfile+"07_10_2017b.html","w+")
    f.write("<html>\n")
    f.write("<body width=\"800px\">")
    f.write("<div style=\"display:block; width: 800px;\">")
    #
    j = 1
    k = 0
    #
    for i in range(net_count):
        xx2[i] = str.lower(xx2[i])
    word_instance   = ["" for x_i in range(net_count)]
    word_count = [0 for x_i in range(net_count)]
    xx2.sort()
    # new code here
    for i in range(net_count-1):
        if (xx2[i] == xx2[i+1][:-1]):
            xx2[i+1] = xx2[i]
    #         
    for i in range(net_count-1):
        if ((xx2[i] <> xx2[i+1])):
             word_instance[k] = xx2[i]
             word_count[k] = j
             j = 1
             k = k+1
        if (xx2[i] == xx2[i+1]):
             j=j+1
    print "Total Word count: ", count
    print "Net Word count: ",net_count
    print "Unique words: ",k
    sum = 0
    for i in range(k):
         rel_count = (word_count[i]/k)*100.0
         if (rel_count > 1.00) :
              print word_instance[i], word_count[i], round(rel_count,3)
              sum = sum + rel_count
         fsize = word_count[i]*4 +14
         if (fsize > 36) :
              fsize = 36
         ccx = int(random.random()*14)
         color_choice = color_array[ccx]
         f.write(" <span style = \"font-family: Arial; font-size: "+str(fsize)+"px; color: "+color_choice+";\">"+word_instance[i]+"</span> ")
    print "Total: ",sum
    f.write("</div>")
    f.write("</body>")
    f.write("</html>")
    f.close()
    #
def main():
    g = open(xfile+".txt", 'r')
    xx = g.read()
    #
    # replace punctuation
    #
    xx = xx.replace(".","")
    xx = xx.replace(",","")
    xx = xx.replace("\'","")
    xx = xx.replace("\/"," ")
    xx = xx.replace("\n","")
    xx = xx.replace("(","")
    xx = xx.replace(")","")
    xx = xx.replace("?","")
    xx = xx.replace("!","")
    xx = xx.replace(":","")
    xx1 = xx
    #
    null_words = ["A "," a "," all "," also ","All "," am ","An "," an "," and ","And "," are ","Are "," as ","As "," at ","At ",
    " be "," but ","But "," by ","By "," can "," do "," for "," from "," had "," has "," have "," how ","How "," I "," if ","If "," in ","In "," is "," it "," its "," if "," my ","My ",
    " no "," not "," on ","On "," or ","Or "," of "," our ","Our ", " so ","So "," that "," the ","The "," these ","These ",
    " there "," they ","They "," this ","This "," their "," to "," too "," us "," was ","Was "," what ","What "," we ","We ",
    " where ","Where "," which "," why "," who ","Who "," will "," with "," yet "]
    #
    for i in range(len(null_words)):
          xx1 = xx1.replace(null_words[i]," ")
    xx1 = xx1.replace("  "," ") 
    #
    xx2 = xx.split(" ")
    count = len(xx2)
    xx2 = xx1.split(" ")
    net_count = len(xx2)
    publishResults(count,net_count, xx2)
    #
if __name__ == "__main__":
    main()
