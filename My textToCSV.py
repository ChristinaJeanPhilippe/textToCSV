#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os

filenameList = []

#directory = r'/Users/bill/Dropbox (UFL)/OPS Annotators/Christina/Wk 2'
directory = r'C:\Users\cjean\University of Florida\NEH Team CompLing - Christina\Wk 3'
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        print(os.path.join(directory, filename))
        filenameList.append(filename)
    else:
        continue

for name in filenameList:
    currentFile = open("./Wk 3/"+name,"r")
    currentText = currentFile.read()
    nameWOutTXT = name.split('.')[0]
    print(nameWOutTXT)
    #print(currentText[:1000])
    currentOutput = open("./Wk 3/"+nameWOutTXT+".csv","w")
    currentText = currentText.replace('\n','&&&&&\n')
    currentText = currentText.replace(';',':')
    currentText = currentText.replace(',',';')
    currentText = currentText.replace('&',',')
    currentOutput.write("Text,Existentail 'it' and 'dey',No copula 'is/are',Absence of 3rd person singular '-s', <your choice here>\n")
    currentOutput.write(currentText)
    currentOutput.close()
    currentFile.close()


# In[ ]:




