n=int(input())
arr=map(int,input().split())
l=list(arr)
l.sort()
m=max(l)
ele=l.index(m)
sec=ele-1
print("Runnerup Score:",l[sec])
