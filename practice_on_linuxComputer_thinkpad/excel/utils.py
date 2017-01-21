import xlwt
import xlrd
from xlrd import open_workbook
from xlutils.copy import copy



while 1:
    e=float(input('enter:'))
    data = xlrd.open_workbook('/home/gates/practice/excel/xmw.xls')
    table = data.sheets()[0]       
    sid=table.col_values(0)
    name=table.col_values(1)
    p=sid.index(e)
    print name[p]
    if input('Y or N:')==1 :
        
        rb=open_workbook('/home/gates/practice/excel/xmw.xls')
        wb=copy(rb)
        ws=wb.get_sheet(0)
        ws.write(p,9,'100')
        wb.save('/home/gates/practice/excel/xmw.xls')
        print 'well done'
    else:
        print 're enter'
        continue


    
