import math
f=[0 for i in range(24)]
f[1]=f[2]=1
for i in range(3,22):
    f[i]=f[i-1]+f[i-2]
for i in range(int(input())):
    a=int(input())
  #  print(int(((math.sqrt(5)+1)/2)**a/math.sqrt(5)-((-math.sqrt(5)+1)/2)**a/math.sqrt(5)))
    print(f[a])