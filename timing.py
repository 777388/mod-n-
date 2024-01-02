import sys
import os
for i in range(int(sys.argv[1])):
    for b in range(int(sys.argv[2])):
        f = os.popen("python3 modn.py "+str(i+1)+" "+str(b+1)+" "+sys.argv[3]).read()
        print(f)