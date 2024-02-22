from copy import deepcopy
a = [[1,2,3,4,0],
     [0,2,4,1,0],
     [0,0,1,2,0],
     [0,0,0,3,0],
     [0,0,0,0,4]]
def slice_matrix(a,n):
    a1 = deepcopy(a)
    a1.pop(0)
    for i in range(0,len(a1)):
        del a1[i][n]
    return a1

def det2(a):
    det = 0
    if len(a) == 3:
        tong = 0
        hieu = 0
        b = deepcopy(a)
        for k in range(0,len(b)):
            b[k] += b[k][0: (len(b)-1)]

        for j in range(0,len(b)):
            tich1 = 1
            tich2 = 1
            for i in range(0,len(b)):
                tich1 = tich1* b[i][i+j]
                tich2 = tich2 *b[len(b)-1-i][i+j]
            tong += tich1
            hieu -= tich2
        return tong + hieu
    elif len(a) == 1:
        return a[0][0]
    else:
        for x in range(0,len(a)):
            det += det2(slice_matrix(a,x))* ((-1)**x) * a[0][x] 
        return det
    
print(det2(a))