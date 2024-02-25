from copy import deepcopy

def slice_matrix(a,m,n): #Cắt ma trận thành các ma trận con Mij
    a1 = deepcopy(a)
    a1.pop(m-1)
    for i in range(0,len(a1)):
        del a1[i][n-1]
    return a1

def det_matrix(a): #Tính Det ma trận
    det = 0
    if len(a) == 3:
        b = deepcopy(a)
        tong = 0
        hieu = 0
        for k in range(0,len(a)):
            b[k] += a[k][0: (len(a)-1)]
        for j in range(0,len(a)):
            tich1 = 1
            tich2 = 1
            for i in range(0,len(a)):
                tich1 = tich1* b[i][i+j]
                tich2 = tich2 *b[len(a)-1-i][i+j]
            tong += tich1
            hieu -= tich2
        return tong+hieu
    elif len(a) == 1:
        return a[0][0]
    else:
        for x in range(0,len(a)):
            det += det_matrix(slice_matrix(a,1,x+1))* ((-1)**x) * a[0][x] 
        return det