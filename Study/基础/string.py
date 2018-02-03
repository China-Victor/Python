"""
 Created by Victor Wu on 2017/12/22.
 字符串操作 
 切片 ： [起始:结束:步长]
"""
name = "Victor Wu"

print(name[0])  # 取角标0的字符

print(name[2])  # 取角标2的字符

print(name[0:2])  # 切片，包含头不包含尾


print(name[0:10:1])  # 设置步长1
# 不写结束角标，默认取到最后一个， 等效上面方式
print(name[0::1])

# 取倒数第一个字符
print(name[-1])
# 重倒数第2 到 倒数第1（不包含）
print(name[-2:-1])

# 这样取到结果是“”，因为这里步长默认是 1（正方向数）
print(name[-1: -3])
# 当想反方向取时，步长要设置成负数
print(name[-1:-3:-1])

# 整串倒序
print(name[-1::-1])



