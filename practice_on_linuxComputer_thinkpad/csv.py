import csv
with open('egg.csv','wb') as f:
    wt=csv.writer(f,dialect='excel')

    wt.writerowrow(['a','v','n'])
    wt.writerowrow(['3','5','9'])
    wt.writerowrow(['1','3','6'])
