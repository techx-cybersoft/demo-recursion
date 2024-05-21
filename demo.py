def tinhTong(n):
    if n == 0:
        return 0
    
    return n + tinhTong(n - 1)

print(tinhTong(3))
