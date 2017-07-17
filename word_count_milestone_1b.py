from __future__ import division
import sys
import random
 
xfile = str(sys.argv[1])
limit = str(sys.argv[2])
count = 0
tagcount = 0
#
# color references...
#
color_array = ["red","maroon","magenta","orange","#6094DB","green","teal","olive","purple","blue","navy","#0088dd","#6755E3","#B6BA18","black"]
#
def mean(x):
   count = len(x)
   sumx = sum(x)
   return sumx/count
#
def syllable_count(word_instance,k):
   syl_sum = 0
   syllable = [0 for x_i in range(k)]
   for i in range(k) :
       if (len(word_instance[i]) < 6) :
            syllable[i] = 1
       if (len(word_instance[i]) >= 6 and len(word_instance[i]) < 9) :
            syllable[i] = 2
       if (len(word_instance[i]) >=9 and len(word_instance[i]) < 13) :
            syllable[i] = 3  
       if (len(word_instance[i]) >=13) :
            syllable[i] = 4
   return(syllable)
#
def avg(syllable) :
   return(sum(ss for ss in syllable)/(len(syllable)))
#
def publishResults(sentence_count, count, net_count, word_length, xx2):
   f = open(xfile+"_cloud.html","w+")
   f.write("<html>\n")
   f.write("<body>")
   #
   h = open(xfile+"_table.html","w+")
   h.write("<html>\n")
   h.write("<body>\n")
   j = 1
   k = 0
   #
   for i in range(net_count):
       xx2[i] = str.lower(xx2[i])
   word_instance   = ["" for x_i in range(net_count)]
   word_count = [0 for x_i in range(net_count)]
   xx2.sort()
   # new code here -- get rid of plurals
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
   #
   ratio_unique = (k/net_count)*100.0
   sentence_avg = count/sentence_count
   syllable = syllable_count(word_instance,k)
   average_syllable = avg(syllable)
   print "*", len(syllable)
   #
   # FKRA = (0.39 x ASL) + (11.8 x ASW) - 15.59
   #
   # FKRE = 206.835 - 1.015x ASL - 84.6xASW
   fkra = (0.39*sentence_avg) + (11.8*average_syllable) - 15.59
   fkre = 206.835 - (1.015*sentence_avg) - (84.6*average_syllable)
   fk_formula = (sentence_avg + average_syllable)*0.4
   sentence_hundred = 100.0/sentence_avg
   syllables_hundred = average_syllable*100.0
   #
   f.write("<table border=\"1\" cellspacing=\"0\" cellpadding = \"1\" width=\"1000px\"><tr>")
   f.write("<td width = \"50%\" valign=\"top\">")
   f.write("<span style = \"text-align: center; font-size: 16px; color: navy;\">Text Analysis (Reading level)</span><br/>")
   f.write("<p>Input file: "+xfile+".doc</p>")
   f.write("<ul>")
   f.write("<li>Sentence count: "+str(sentence_count)+"")
   f.write("<li>Average words per sentence: "+str(round(sentence_avg,1))+"</li>")
   f.write("<li>Total Word count: "+str(count)+"</li>")
   f.write("<li>Net Word count (less stop words): "+str(net_count)+"</li>")
   f.write("<li>Unique words: "+str(k)+" -- % of Net: "+str(round(ratio_unique,2))+"% </li>")
   f.write("<li>Average word length: "+str(round(word_length,1))+" characters</li>")
   f.write("<li>Average number of syllables per word: "+str(round(average_syllable,2))+"</li>")
   f.write("<li>FKRA (Flesch-Kincaid) Reading Level - Grade: "+str(round(fk_formula,1))+"</li>")
   f.write("<li>FKRE (Flesch-Kincaid) Reading Level - ease: "+str(round(fkre,1))+"</li>")
   f.write("<li>Sentences per 100 words: "+str(round(sentence_hundred,1))+"")
   f.write("<li>Syllables per 100 words: "+str(round(syllables_hundred,1))+"</li>")
   f.write("</ul></td>")
   f.write("<td width=\"50%\">")
   #
   h.write("<table cellspacing = \"0\" cellpadding = \"1\" border=\"1\" width = \"600\">")
   h.write("<tr><td bgcolor=\"#dedede\" width=\"300\" align=\"center\"><b>Word Instance</b></td>")
   h.write("<td bgcolor=\"#dedede\" width=\"100\" align=\"center\"><b>Syllables</b></td>")
   h.write("<td bgcolor=\"#dedede\" width = \"100\" align=\"center\"><b>Count</b> ( > "+limit+")</td>")
   h.write("<td bgcolor=\"#dedede\" width = \"100\" align=\"center\"><b>Frequency</b></td></tr>")
   freq = mean(word_count)
   print "Mean: ",freq
   nn = 0
   #
   fsize = 10
   for i in range(k):
        if (word_instance[i] > "aa" and word_count[i] > float(limit)) :
            # print word_instance[i], word_count[i]
            # new code
            duo = 0
            for duo in range(16) :
                 if (word_count[i] >= (2**duo) and word_count[i] < (2**(duo+1))) :
                      fsize = 14 + duo*4
            #
            relative_count = (word_count[i]/k)*100.0
            ccx = int(random.random()*14)
            color_choice = color_array[ccx]
            nn = nn+1
            f.write("<span style = \"font-size: "+str(fsize)+"px; color: "+color_choice+";\">"+word_instance[i]+"</span> ")
            h.write("<tr><td width=\"300\">"+str(nn)+". "+word_instance[i]+"</td>")
            h.write("<td width=\"100\" align=\"center\">"+str(syllable[i])+"</td>")
            h.write("<td width = \"100\" align=\"right\">"+str(word_count[i])+"</td>")
            h.write("<td width = \"100\" align=\"right\">"+str(round(relative_count,2))+"% </td></tr>")
   #
   f.write("</td></tr></table>")
   f.write("</body>")
   f.write("</html>")
   f.close()
   #
   h.write("</table>")
   h.write("</body>")
   h.write("</html>")
   h.close()
   #
def main():
   g = open(xfile+".txt", 'r')
   xx = g.read()
   #
   # sentence count
   #
   xx = xx.replace("? ",". ")
   xx = xx.replace("! ",". ")
   xx0 = xx.split(". ")
   sentence_count = len(xx0)
   #
   # eliminate punctuation
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
   xx = xx.replace(";","")
   xx1 = xx
   #
   null_words = ["A "," a "," all "," also ","All "," am ","An "," an "," and ","And "," are ","Are "," as ","As "," at ","At ",
   " be "," but ","But "," by ","By "," can "," do "," for "," from "," had "," has "," have "," how ","How "," I "," if ","If ",
   " in ","In "," is "," it ","It "," its "," if ","If "," my ","My "," no "," not "," on ","On "," or ","Or "," of "," our ","Our ", " so ","So ",
   " that "," the ","The "," these ","These "," there "," they ","They "," this ","This "," their "," to "," too "," us ","You "," you ",
   "Your "," your "," was ","Was "," what ","What "," we ","We "," when ","When "," where ","Where "," which ",
   "Why "," why "," who ","Who "," will "," with ","With "," would "," yet "]
   #
   for i in range(len(null_words)):
        xx1 = xx1.replace(null_words[i]," ")
   xx1 = xx1.replace("  "," ")
   #
   xx2 = xx.split(" ")
   count = len(xx2)
   word_length = sum(len(word) for word in xx2)/count
   xx2 = xx1.split(" ")
   net_count = len(xx2)
   publishResults(sentence_count,count,net_count, word_length,xx2)
   #
if __name__ == "__main__":
   main()