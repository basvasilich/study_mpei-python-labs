from lab1_module import *

vectors = {'A': [], 'B': [], 'C': []}

for vector in vectors:
    vector_str = input('Input Vector {0} (1,2,3): '.format(vector))
    vectors[vector] = list(map(lambda i: int(i), vector_str.split(',')))

result_str = "Result: " + str(lab1_task1(vectors['A'], vectors['B'], vectors['C']))

f = open('output.txt', 'w')
f.write(result_str)
print(result_str)
