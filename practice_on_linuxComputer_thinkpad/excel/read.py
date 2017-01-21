# -*- coding: utf-8 -*- 
import  xdrlib ,sys
import xlrd

data = xlrd.open_workbook('/home/gates/practice/excel/xmw.xls')
table = data.sheets()[0]       
sid=table.col_values(0)
name=table.col_values(1)
p=sid.index(141210027)




