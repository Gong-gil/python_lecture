def root_ex(a,b,c):
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 *a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 *a)
    return '해는',r1, '또는' ,r2

print(root_ex(2,-1,-6))