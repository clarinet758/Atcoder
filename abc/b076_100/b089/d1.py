#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

def sol():
    h,w,d=map(int,input().split())
    a=[[int(i) for i in input().split()] for i in range(h)]
    t={}
    for i in range(h):
        for j in range(w):
            t[a[i][j]]=(i,j)
    ans=[0]*(h*w+1)
    for i in range(h*w,d,-1):
        o,p=t[i]
        ans[i-d]=ans[i]+abs(o-t[i-d][0])+abs(p-t[i-d][1])
    q=int(input())
    for i in range(q):
        l,r=map(int,input().split())
        print(ans[l]-ans[r])

if __name__=="__main__":
    sol()
