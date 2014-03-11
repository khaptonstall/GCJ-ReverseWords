import sys


f = open("B-small-practice.in", 'r')


T = int(f.readline().strip())


array = []

for i in range(T):
    array.append(f.readline().strip().split(' '))
    

for ar in array:
    print ' '.join(ar[::-1])
    
    
f.close()
