from __future__ import division
import sys
import random
import re
 
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
def syllable_count(xx1,count):
     syl_sum = 0
     syllable = [0 for x_i in range(count)]
     for i in range(count):
         word = xx1[i]
         syllable[i] = sylco(word)
     return(syllable)
#
# function from: m.emre aydin (2013) eayd.in/p=232
#
def sylco(word) :
    word = word.lower()
    # exception_add are words that need extra syllables
    # exception_del are words that need less syllables
    exception_add = ['serious','crucial']
    exception_del = ['fortunately','unfortunately']
    co_one = ['cool','coach','coat','coal','count','coin','coarse','coup','coif','cook','coign','coiffe','coof','court']
    co_two = ['coapt','coed','coinci']
    pre_one = ['preach']
    syls = 0 #added syllable number
    disc = 0 #discarded syllable number
    #
    # 1) if letters < 3 : return 1
    #
    if len(word) <= 3 :
        syls = 1
        return syls
    #
    # 2) if doesn't end with "ted" or "tes" or "ses" or "ied" or "ies", discard "es" and "ed" at the end.
    # if it has only 1 vowel or 1 set of consecutive vowels, discard. (like "speed", "fled" etc.)
    #
    if word[-2:] == "es" or word[-2:] == "ed" :
        doubleAndtripple_1 = len(re.findall(r'[eaoui][eaoui]',word))
        if doubleAndtripple_1 > 1 or len(re.findall(r'[eaoui][^eaoui]',word)) > 1 :
            if word[-3:] == "ted" or word[-3:] == "tes" or word[-3:] == "ses" or word[-3:] == "ied" or word[-3:] == "ies" :
                pass
            else :
                disc+=1
    #
    # 3) discard trailing "e", except where ending is "le" 
    #
    le_except = ['whole','mobile','pole','male','female','hale','pale','tale','sale','aisle','whale','while']
    if word[-1:] == "e" :
        if word[-2:] == "le" and word not in le_except :
            pass
        else :
            disc+=1
    #
    # 4) check if consecutive vowels exists, triplets or pairs, count them as one.
    #
    doubleAndtripple = len(re.findall(r'[eaoui][eaoui]',word))
    tripple = len(re.findall(r'[eaoui][eaoui][eaoui]',word))
    disc+=doubleAndtripple + tripple
    #
    # 5) count remaining vowels in word.
    #
    numVowels = len(re.findall(r'[eaoui]',word))
    #
    # 6) add one if starts with "mc"
    #
    if word[:2] == "mc" :
        syls+=1
    #
    # 7) add one if ends with "y" but is not surrouned by vowel
    #
    if word[-1:] == "y" and word[-2] not in "aeoui" :
        syls +=1
    #
    # 8) add one if "y" is surrounded by non-vowels and is not in the last word.
    #
    for i,j in enumerate(word) :
        if j == "y" :
            if (i != 0) and (i != len(word)-1) :
                if word[i-1] not in "aeoui" and word[i+1] not in "aeoui" :
                    syls+=1
    #
    # 9) if starts with "tri-" or "bi-" and is followed by a vowel, add one.
    #
    if word[:3] == "tri" and word[3] in "aeoui" :
        syls+=1
    if word[:2] == "bi" and word[2] in "aeoui" :
        syls+=1
    #
    # 10) if ends with "-ian", should be counted as two syllables, except for "-tian" and "-cian"
    #
    if word[-3:] == "ian" :
    # and (word[-4:] != "cian" or word[-4:] != "tian") :
        if word[-4:] == "cian" or word[-4:] == "tian" :
            pass
        else :
            syls+=1
    #
    # 11) if starts with "co-" and is followed by a vowel, check if exists in the double syllable dictionary, if not, check if in single dictionary and act accordingly.
    #
    if word[:2] == "co" and word[2] in 'eaoui' :
        if word[:4] in co_two or word[:5] in co_two or word[:6] in co_two :
            syls+=1
        elif word[:4] in co_one or word[:5] in co_one or word[:6] in co_one :
            pass
        else :
            syls+=1
    #
    # 12) if starts with "pre-" and is followed by a vowel, check if exists in the double syllable dictionary, if not, check if in single dictionary and act accordingly.
    #
    if word[:3] == "pre" and word[3] in 'eaoui' :
        if word[:6] in pre_one :
            pass
        else :
            syls+=1
    #
    # 13) check for "-n't" and cross match with dictionary to add syllable.
    #
    negative = ["doesn't", "isn't", "shouldn't", "couldn't","wouldn't"]
    if word[-3:] == "n't" :
        if word in negative :
            syls+=1
        else :
            pass 
    #
    # 14) Handling the exceptional words.
    #
    if word in exception_del :
        disc+=1
    if word in exception_add :
        syls+=1   
    #
    # calculate the output
    #
    return (numVowels - disc + syls)
#
def avg(syllable) :
   return(sum(ss for ss in syllable)/(len(syllable)))
#
def publishResults(sentence_count, xx1, xx2):
   f = open(xfile+"_cloud.html","w+")
   f.write("<html>\n")
   f.write("<body>")
   #
   h = open(xfile+"_table.html","w+")
   h.write("<html>\n")
   h.write("<body>\n")
   j1 = 1
   k1 = 0
   j2 = 1
   k2 = 0
   #
   count = len(xx1)
   word_length = sum(len(word) for word in xx1)/count
   #
   for i in range(count) :
        xx1[i] = str.lower(xx1[i])
   #
   xx1.sort()
   #
   syllable = syllable_count(xx1,count)
   average_syllable = avg(syllable)
   print "*", len(syllable)
   #    
   # new code here -- get rid of plurals
   #
   total_word_instance   = ["" for x_i in range(count)]
   total_word_count = [0 for x_i in range(count)]
   total_word_syllable = [0 for x_i in range(count)]
   for i in range(count-1):
       if (xx1[i] == xx1[i+1][:-1]):
           xx1[i+1] = xx1[i]
   #        
   for i in range(count-1):
       if ((xx1[i] <> xx1[i+1])):
            total_word_instance[k1] = xx1[i]
            total_word_syllable[k1] = syllable[i]
            total_word_count[k1] = j1
            j1 = 1
            k1 = k1+1
       if (xx1[i] == xx1[i+1]):
            j1=j1+1
   #
   net_count = len(xx2)
   for i in range(net_count):
       xx2[i] = str.lower(xx2[i])
   word_instance   = ["" for x_i in range(net_count)]
   word_count = [0 for x_i in range(net_count)]
   xx2.sort()
   #
   for i in range(net_count-1):
       if (xx2[i] == xx2[i+1][:-1]):
           xx2[i+1] = xx2[i]
   #        
   for i in range(net_count-1):
       if ((xx2[i] <> xx2[i+1])):
            word_instance[k2] = xx2[i]
            word_count[k2] = j2
            j2 = 1
            k2 = k2+1
       if (xx2[i] == xx2[i+1]):
            j2=j2+1
   #
   ratio_unique = (k1/count)*100.0
   sentence_avg = count/sentence_count
   #
   # FKRA = (0.39 x ASL) + (11.8 x ASW) - 15.59
   #
   # FKRE = 206.835 - 1.015x ASL - 84.6xASW
   #
   fkra = (0.39*sentence_avg) + (11.8*average_syllable) - 15.59
   fkre = 206.835 - (1.015*sentence_avg) - (84.6*average_syllable)
   fk_formula = (sentence_avg + average_syllable)*0.4
   sentence_hundred = 100.0/sentence_avg
   syllables_hundred = average_syllable*100.0
   #
   f.write("<table border=\"1\" cellspacing=\"0\" cellpadding = \"1\" width=\"1200px\"><tr>")
   f.write("<td width = \"40%\" valign=\"top\">")
   f.write("<span style = \"text-align: center; font-size: 16px; color: navy;\">Text Analysis (Reading level)</span><br/>")
   f.write("<p>Input file: "+xfile+".doc</p>")
   f.write("<ul>")
   f.write("<li>Sentence count: "+str(sentence_count)+"")
   f.write("<li>Average words per sentence: "+str(round(sentence_avg,1))+"</li>")
   f.write("<li>Total Word count: "+str(count)+"</li>")
   f.write("<li>Net Word count (less stop words): "+str(net_count)+"</li>")
   f.write("<li>Unique words: "+str(k1)+" -- % of Total: "+str(round(ratio_unique,2))+"% </li>")
   f.write("<li>Average word length: "+str(round(word_length,1))+" characters</li>")
   f.write("<li>Average number of syllables per word: "+str(round(average_syllable,2))+"</li>")
   f.write("</ul>")
   f.write("<ul>")
   f.write("<li>FKRA (Flesch-Kincaid) Reading Level - Grade: "+str(round(fk_formula,1))+"</li>")
   f.write("<li>FKRE (Flesch-Kincaid) Reading Level - (alt): "+str(round(fkra,1))+"</li>")
   f.write("<li>Sentences per 100 words: "+str(round(sentence_hundred,1))+"")
   f.write("<li>Syllables per 100 words: "+str(round(syllables_hundred,1))+"</li>")
   f.write("</ul></td>")
   f.write("<td width=\"60%\">")
   #
   # separate reference table
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
   for i in range(k1):
      relative_count = (total_word_count[i]/k1)*100.0      
      h.write("<tr><td width=\"300\">"+total_word_instance[i]+"</td>")
      h.write("<td width=\"100\" align=\"center\">"+str(total_word_syllable[i])+"</td>")
      h.write("<td width = \"100\" align=\"right\">"+str(total_word_count[i])+"</td>")
      h.write("<td width = \"100\" align=\"right\">"+str(round(relative_count,2))+"% </td></tr>")
   #   
   # word cloud
   #
   for i in range(k2):
        if (word_instance[i] > "aa" and word_count[i] > float(limit)) :
            # print word_instance[i], word_count[i]
            # new code
            duo = 0
            for duo in range(16) :
                 if (word_count[i] >= (2**duo) and word_count[i] < (2**(duo+1))) :
                      fsize = 14 + duo*4
            #
            ccx = int(random.random()*14)
            color_choice = color_array[ccx]
            nn = nn+1
            f.write("<span style = \"font-size: "+str(fsize)+"px; color: "+color_choice+";\">"+word_instance[i]+"</span> ")        
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
   # sentence count [xx0]
   #
   xx = xx.replace("? ",". ")
   xx = xx.replace("! ",". ")
   xx0 = xx.split(". ")
   sentence_count = len(xx0)
   #
   # eliminate punctuation
   #
   xx = xx.replace(".\n",". ")
   xx = xx.replace(".","")
   xx = xx.replace(",","")
   xx = xx.replace("\'","")
   xx = xx.replace("\"","")
   xx = xx.replace("\/"," ")
   xx = xx.replace("\n","")
   xx = xx.replace("(","")
   xx = xx.replace(")","")
   xx = xx.replace("?","")
   xx = xx.replace("!","")
   xx = xx.replace(":","")
   xx = xx.replace(";","")
   xx = xx.replace("  "," ")
   #
   # all words [xx1]
   #
   xx1 = xx.split(" ")
   #
   # less stop words [xx2]
   #
   null_words = ["A "," a "," all ","All "," also ","Also "," am "," an ","An "," and ","And "," are ","Are "," as ","As "," at ","At ",
   " be "," but ","But "," by ","By "," can "," do "," for "," from "," had "," has "," have "," how ","How "," I ","I "," if ","If ",
   " in ","In "," is ","Is "," it ","It "," its "," if ","If "," my ","My "," no "," not "," on ","On "," or ","Or "," of "," our ","Our ", " so ","So ",
   " that "," the ","The "," these ","These "," there "," they ","They "," this ","This "," their "," to "," too "," us ","You "," you ",
   "Your "," your "," was ","Was "," what ","What "," we ","We "," when ","When "," where ","Where "," which ","Which ",
   " why ","Why "," who ","Who "," will "," with ","With "," would "," yet "]
   #
   for i in range(len(null_words)):
        xx = xx.replace(null_words[i]," ")
   xx = xx.replace("  "," ")
   #
   xx2 = xx.split(" ")
   publishResults(sentence_count, xx1, xx2)
   #
if __name__ == "__main__":
   main()