from copy import deepcopy

def slice_matrix(a,m,n):
    a1 = deepcopy(a)
    a1.pop(m)
    for i in range(0,len(a1)):
        del a1[i][n]
    return a1

def det_matrix(a):
    det = 0
    if len(a) == 1:
        return a[0][0]
    else:
        for x in range(0,len(a)):
            det += det_matrix(slice_matrix(a,0,x))* ((-1)**x) * a[0][x] 
        return det