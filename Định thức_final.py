from copy import deepcopy

def nhap_matrix():
    n = int(input("Nhập cỡ ma trận: "))
    ma = []
    for i in range(n):
        row = []
        for j in range(n):
            x = int(input(f"Nhập phần tử thứ a[{i+1}][{j+1}]: "))
            row.append(x)
        ma.append(row)
        print(ma)
        print("----------")
    return ma

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

def phu_dai_so_C(a):
    a1 = deepcopy(a)
    a2 = deepcopy(a)
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            a2[i][j] = det_matrix(slice_matrix(a1,i,j)) * (-1)**(i+j)
    return a2

def matrix_chuyen_vi(a):
    a1 = deepcopy(a)
    for i in range(len(a)):
        for j in range(len(a)):
            a1[i][j] = a[j][i]
    return a1

def matrix_dao(a):
    a1 = deepcopy(a)
    a2 = matrix_chuyen_vi(phu_dai_so_C(a))
    for i in range(len(a)):
        for j in range(len(a)):
            a1[i][j] = a2[i][j] / det_matrix(a)
    return a1

print(matrix_dao((nhap_matrix)))
