#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
import re
import math
import itertools
import collections
import bisect
#sys.stdin=file('input.txt')
#sys.stdout=file('output.txt','w')
#10**9+7
mod=1000000007
#mod=1777777777
pi=3.141592653589
IS=float('inf')
xy=[(1,0),(-1,0),(0,1),(0,-1)]
bs=[(-1,-1),(-1,1),(1,1),(1,-1)]
def niten(a,b): return abs(a-b) if a>=0 and b>=0 else  a+abs(b) if a>=0 else abs(a)+b if b>=0 else abs(abs(a)-abs(b))
def fib(n): return [(seq.append(seq[i-2] + seq[i-1]), seq[i-2])[1] for seq in [[0, 1]] for i in range(2, n)]
def gcd(a,b): return a if b==0 else gcd(b,a%b)
def lcm(a,b): return a*b/gcd(a,b)
def eucl(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)**0.5
def choco(xa,ya,xb,yb,xc,yc,xd,yd): return 1 if abs((yb-ya)*(yd-yc)+(xb-xa)*(xd-xc))<1.e-10 else 0
def pscl(num,l=[1]):
    for i in range(num):
        l = map(lambda x,y:x+y,[0]+l,l+[0])
    return l

class UnionFind:
    def __init__(self, size):
        self.rank=[0]*size
        self.par =range(size)
        self.grp =size

    def find(self, x):
        if x==self.par[x]: return x

        self.par[x]=self.find(self.par[x])
        return self.par[x]

    def same(self, x, y): #2つの頂点が同じグループであるかを判定する
        return self.find(x)==self.find(y)

    def unite(self, x, y): #辺で接続されている2つの頂点を投げて統合する
        x,y=self.find(x),self.find(y)
        if x==y:
            return

        self.grp-=1
        if self.rank[x]<self.rank[y]:
            self.par[x]=y
        else:
            self.par[y]=x
            if self.rank[x]==self.rank[y]:
                self.rank[x]+=1

    def group_num(self):
        return self.grp
    def ra(self):
        return self.par

n,m=map(int,raw_input().split())
ans=0
uf=UnionFind(n)

d={i:0 for i in range(n)}
for i in range(m):
    a,b=map(int,raw_input().split())
    uf.unite(a-1,b-1)
    d[a-1]+=1
    d[b-1]+=1

for i in range(n):
    uf.find(i)

q1=uf.ra()
chk={}
for a,i in enumerate(q1):
    if i in chk:
        chk[i][0]+=1
        chk[i][1]+=d[a]
    else:
        chk[i]=[1,d[a]]
for i in chk:
    if chk[i][0]==chk[i][1]/2+1:
        ans+=1
print ans
