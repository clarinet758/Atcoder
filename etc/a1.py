#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

n,k=map(int,input().split())
print("YES" if k==1 or (n+1)//2>=k else "NO")
