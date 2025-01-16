import math

n=int(input())
cube=[i**3 for i in range(105)]
for a in range(2,n+1):
    for b in range(2,a):
        for c in range(b,a):
            for d in range(c,a):
                if cube[a]==cube[b]+cube[c]+cube[d]:
                    print(f'Cube = {a}, Triple = ({b},{c},{d})')
                    break


