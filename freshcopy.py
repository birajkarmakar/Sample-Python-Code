#!/bin/usr/env python
import os
import sys
a=[]
b=[]

def find_key(dic, val):
	return [k for k, v in dic.iteritems() if v == val][0]
def listdir_fullpath(m):
    return [os.path.join(m, f) for f in os.listdir(m)]
p=listdir_fullpath(sys.argv[1])
for i in p:
        b.append(i)
	a.append(os.path.getsize(i))

d=dict(zip(a,b))
keys=d.keys()
keys.sort()
vals=map(d.get,keys)
l=1
for i in vals:
	o=find_key(d, i)
    	o = float(o)
    	if o >= 1099511627776:
        	terabytes = o / 1099511627776
        	size = '%.2fT' % terabytes
    	elif o >= 1073741824:
        	gigabytes = o / 1073741824
        	size = '%.2fG' % gigabytes
    	elif o >= 1048576:
        	megabytes = o / 1048576
        	size = '%.2fM' % megabytes
    	elif o >= 1024:
        	kilobytes = o / 1024
        	size = '%.2fK' % kilobytes
    	else:
        	size = '%.2fb' % o
    	print l, i , "!! Size " ,size
	l=l+1 
