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
ans=''
s=raw_input()
ans+=s[0].upper()
for i in range(1,len(s)):
    ans+=s[i].lower()
print ans
ans=chk=0
#end = time.clock()
#print end - start
