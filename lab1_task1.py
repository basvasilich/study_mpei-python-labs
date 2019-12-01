from lab1_module import *

vector_a = [];
vector_b = [];
vector_c = [];
vector_a_str = input('Input Vector A (1,2,3): ');
vector_b_str = input('Input Vector B (1,2,3): ');
vector_c_str = input('Input Vector C (1,2,3): ');

for i in vector_a_str[0::2]:
    vector_a.append(float(i));

for i in vector_b_str[0::2]:
    vector_b.append(float(i));

for i in vector_c_str[0::2]:
    vector_c.append(float(i));

result_str = "Result: " + str(lab1_task1(vector_a, vector_b, vector_c));

f = open('output.txt', 'w');
f.write(result_str);
print(result_str);
