# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 19:17:18 2016

@author: aa
"""

import xlwt

Dic={1:"a",2:"b",3:"c",4:"d",5:"e"}
f=xlwt.Workbook()
tableAll=f.add_sheet('jorder')
table=f.add_sheet('001')
for i in range(1,6):
    table.write(0,i,Dic[i])
f.save("a"+'.xls')
for i in range(1,21):
    for j in range(1,6):
        table.write(i,j,str(i)+"*"+str(j)+"="+str(i*j))
for i in range(1,6):
    tableAll.write(0,i,Dic[i])
f.save("a"+'.xls')