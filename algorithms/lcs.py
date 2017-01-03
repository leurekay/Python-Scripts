import numpy as np
x="bada"
y="adbad"
x_len=len(x)
y_len=len(y)
x_new="0"+x
y_new="0"+y
M=np.zeros((x_len+1,y_len+1),"int")
for i in range(1,x_len+1):
    for j in range(1,y_len+1):
        if x_new[i]==y_new[j]:
            M[i][j]=M[i-1][j-1]+1
        else:
            M[i][j]=max(M[i][j-1],M[i-1][j])
max_num=M[x_len][y_len]

