#tính toán ở đây nhá các bạn

from copy import deepcopy
import Det_matrix_module #tính Det của ma trận
import Matrix_nghich_module #tìm ma trận nghịch đảo

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


print(Matrix_nghich_module.matrix_dao(nhap_matrix()))
