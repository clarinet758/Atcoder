#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

a,b,c,d=map(int,input().split())
print("Yes" if (a<=c<=b or a<=d<=b or c<=a<=d or c<=b<=d) else "No")
