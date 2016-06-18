#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
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
def gcd(a,b): return a if b==0 else gcd(b,a%b)
def lcm(a,b): return a*b/gcd(a,b)
def euclid_dis(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2)**0.5
def choco(xa,ya,xb,yb,xc,yc,xd,yd): return 1 if abs((yb-ya)*(yd-yc)+(xb-xa)*(xd-xc))<1.e-10 else 0

n=int(raw_input())
#n,k=map(int,raw_input().split())
l=map(int,raw_input().split())
l.append(l[-1])
ans=t=0
chk=[IS]*(n+1)
chk[0]=0
while t<n:
    chk[t+1]=min(chk[t+1],chk[t]+abs(l[t+1]-l[t]))
    if t<n-1:
        chk[t+2]=min(chk[t+2],chk[t]+abs(l[t+2]-l[t]))
    t+=1
print chk[-1]
#end = time.clock()
#print end - start
