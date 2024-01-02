import sys
f = []
x = int(sys.argv[1])%int(sys.argv[2])
for i in range(int(sys.argv[3])):
    f.append(i+1)
print(list(map(lambda b: x+int(sys.argv[2])*b, f)))