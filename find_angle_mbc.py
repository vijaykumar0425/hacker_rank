# Enter your code here. Read input from STDIN. Print output to STDOUT

import math 
import sys
AB = int(sys.stdin.readline())
BC = int(sys.stdin.readline()) 
sys.stdout.write(str(int(round(math.degrees(math.atan2(AB,BC)))))+'°')


