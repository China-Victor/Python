"""
 Created by Victor Wu on 2017/12/22.
 
"""

import numpy as np

a = np.array([1, 2, 3])
print(a)
print(a[1:2])

# 等差数组
lo = np.logspace(1, 10, 3)
print(lo)  # [  1.00000000e+01   3.16227766e+05   1.00000000e+10]

# 从字符串得到数组
s = np.fromstring("hello numpy", dtype=np.int8)
print(s)  # [104 101 108 108 111  32 110 117 109 112 121]

b = np.array([[1, 2, 3], [4, 5, 6]])
c = b[1]
print(c)  # [4 5 6]  获取的一个元素
d = b[1:2]
print(d)  # [[4 5 6]]  切片返回得到一个数组， 然后再把子元素装到这个数组里

e = b[1:2][0]
print(e)  # [4 5 6]  相当于从[[4 5 6]] 中获取第一个元素


# 自定义结构体
personal = np.dtype({'names': ['name', 'age'], 'formats': ['S32', 'i']})
print(personal)  # [('name', 'S32'), ('age', '<i4')]

my_personal = np.array([("victor", 18)], dtype=personal)
print(my_personal)  # [(b'victor', 18)]

print(my_personal[0])  # (b'victor', 18)

print(str(my_personal[0][0], encoding="utf-8"))  # victor





