#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
a=[int(i) for i in input().split()]
x=0
b=[]
for i in a:
  if i<0: x=x+1
  b.append(abs(i))
b.sort()
print(sum(b)-b[0]*2 if  x%2 else sum(b))
