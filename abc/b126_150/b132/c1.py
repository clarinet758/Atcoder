#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n=int(input())
d=[int(i) for i in input().split()]
d.sort()
print(d[n//2]-d[n//2-1])
