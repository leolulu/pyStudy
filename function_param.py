def print_max(a,b):
    if a>b:
          print(a, 'is maximum')
    elif a==b:
        print(a, 'is equal to', b)
    else:
           print(b, 'is maximum')

print_max(3, 4)

x = '*'
y = '/'

# 以参数的形式传递变量
print_max(x, y)
