#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


a,b=map(int,input().split())
print(b if a>12 else b//2 if a>5 else 0)
