#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import sys
import io
import re
import math
import itertools
#sys.stdin=file('input.txt')
#sys.stdout=file('output.txt','w')
#10**9+7
mod=1000000007
#start = time.clock()
n=int(raw_input())
x=int(raw_input())
print min(abs(n-x),min(n,x)-max(n,x)+10)
#end = time.clock()
#print end - start
