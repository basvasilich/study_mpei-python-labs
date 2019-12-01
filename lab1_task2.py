from lab1_module import *

a: float = float(input('Input A '))
b: float = float(input('Input B '))
n: int = int(input('Input N '))

step: float = (b - a) / (n - 1)
x = a

result_str1 = make_header(name1='F1')
result_str2 = make_header(name1='F2')
result_str3 = make_header(name1='F1', name2='F2')

for i in range(1, n + 1):
    result_str1 += make_row(x, f1=func1)
    result_str2 += make_row(x, f1=func2)
    result_str3 += make_row(x, f1=func1, f2=func2)
    x += step

result = result_str1 + "\n" + result_str2 + "\n" + result_str3
f = open('output.txt', 'w')
f.write(result)
print(result)
