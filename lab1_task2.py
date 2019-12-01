from lab1_module import *


def make_row(x, f1, f2=False):
    if (f2):
        return "{1} {0:6.4}{1:6.4}{2:6.4}\n".format(str(x), str(f1(x)), str(f2(x)))
    return "{0:6.4}{1:6.4}\n".format(str(x), str(f1(x)))


def make_header(name1, name2=False):
    if (name2):
        return """
 X     {0}    {1}
-------------------
""".format(name1, name2);
    return """
 X     {0}
-----------
""".format(name1);


a = float(input('Input A '));
b = float(input('Input B '));
n = int(input('Input N '));

step = (b - a) / (n - 1);
x = a;

result_str1 = make_header(name1='F1');
result_str2 = make_header(name1='F2');
result_str3 = make_header(name1='F1', name2='F2');

for i in range(1, n + 1):
    result_str1 += make_row(x, f1=func1);
    result_str2 += make_row(x, f1=func2);
    result_str3 += make_row(x, f1=func1, f2=func2);
    x += step;

result = result_str1 + "\n" + result_str2 + "\n" + result_str3;
f = open('output.txt', 'w');
f.write(result);
print(result);
