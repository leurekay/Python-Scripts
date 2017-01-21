import xlwt
f=xlwt.Workbook()
table=f.add_sheet('001')
table.write(0,0,'heh')
f.save('excel1.xls')
