
l=[]
    n=int(input())
    for _ in range(n):
        l.append([input(),float(input())])
    s=set([l[i][1] for i in range(n)])
    s=list(s)
    s.sort()
    l=[l[i][0] for i in range(n) if l[i][1]== s[1]]
    l.sort()
    for i in l:
        print(i)
