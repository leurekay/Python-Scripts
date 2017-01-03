# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 12:22:48 2016

@author: aa
"""
pathread="ceshi.txt"
pathwrite="out.txt"
fr = open(pathread, 'r')
fw=open(pathwrite,"a")
raw=fr.readlines()
count=0
for strList in raw:
    s=strList.split()
    s[0]=int(s[0])
    for i in [3,4,5,6,7,8,9]:
        s[i]=float(s[i])           
    fw.writelines("%5d%-5s%5s%5d%8.3f%8.3f%8.3f%8.4f%8.4f%8.4f"%(s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8],s[9])+"\n")
    count=count+1
    print count
fr.close()
fw.close()
    
