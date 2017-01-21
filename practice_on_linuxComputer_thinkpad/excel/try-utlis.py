# -*- coding: utf-8 -*-
import xlwt
import xlrd
from xlrd import open_workbook
from xlutils.copy import copy

while 1:
    e=float(input('输入学号:'))
    data = xlrd.open_workbook('/home/gates/practice/excel/xw.xlsx')
    table = data.sheets()[0]       
    sid=table.col_values(0)
    name=table.col_values(1)
    try:
        
        p=sid.index(e)
    except ValueError:
        print '名单里没有这个学号，请核对后再输：'
        continue
    print name[p]
    if input('Y or N:')==0 :
        
        rb=open_workbook('/home/gates/practice/excel/xw.xlsx')
        wb=copy(rb)
        ws=wb.get_sheet(0)
        ws.write(p,6,10)
        wb.save('/home/gates/practice/excel/xw.xlsx')
        print '干的漂亮！'
    else:
        print '我输错了，重新再来一次吧'
        continue
