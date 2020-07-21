def equi(m):
    a, b = 0, 1
    while(a<m):
        a,b = b,b+1
        c=int(m)-a*1+1
        print(" "*c+"@ "*a)
equi(6)