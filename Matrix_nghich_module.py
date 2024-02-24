from copy import deepcopy
import Det_matrix_module

def phu_dai_so_C(a):
    a1 = deepcopy(a)
    a2 = deepcopy(a)
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            a2[i][j] = Det_matrix_module.det_matrix(Det_matrix_module.slice_matrix(a1,i,j)) * (-1)**(i+j)
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
    if Det_matrix_module.det_matrix(a)== 0:
        return "Ma trận không nghịch đảo"
    else:
        for i in range(len(a)):
            for j in range(len(a)):
                a1[i][j] = a2[i][j] / Det_matrix_module.det_matrix(a)
        return a1

