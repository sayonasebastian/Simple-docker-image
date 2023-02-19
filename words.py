import os
import socket    
# 1. List name of all the text file at location: /home/data
ls=os.listdir('/home/data')
lsStr = "List name of all the text file at location (/home/data): "+ str(ls)
# 2. Read the two text files and count total number of words in each text files - IF.txt and Limerick.txt
IfFile = open('/home/data/IF.txt', 'r')
IfSeperated = IfFile.read().replace(',','').replace('.','').split()
ifCount = len(IfSeperated)
Ifstr = "Word count in file IF.txt: " +str(ifCount)
limerickFile = open('/home/data/Limerick.txt', 'r')
limerickSeperated = limerickFile.read().split()
limerickCount = len(limerickSeperated)
limestr = "Word count in file Limerick.txt: " + str(limerickCount)
# 3. Total number of words in both files
total = "Total word count from both files: "+ str(ifCount+limerickCount)
# 4. List the top 3 words with maximum number of counts in IF.txt with their counts
d = {}
for word in IfSeperated:
    word = word.lower()
    if word in d:
        d.update({word: d.get(word)+1})
    else:
        d[word] = 1

d = sorted(d.items(), key=lambda x:x[1], reverse=True)
top3words = "The top 3 words with max counts in IF.txt are: "+str(d[0])+", "+str(d[1])+", "+str(d[2])+""
# 5. Printing IP address of machine
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)
IPAddrStr = "IP address of current system: " + str(IPAddr)
# 6. Writing all the output to a text file at location: /home/output/result.txt 
f = open("/home/output/result.txt", "w")
resultSTR = lsStr+"\n\n"+Ifstr+"\n\n"+limestr+"\n\n"+total+"\n\n"+ top3words+"\n\n"+IPAddrStr
f.write(resultSTR)
f.close()
# 7. Printing the information on console from result.txt file
f1 = open('/home/output/result.txt', 'r')
print( f1.read())
f1.close()
