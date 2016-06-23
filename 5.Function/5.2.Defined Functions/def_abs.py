#!/usr/bin/env python
def my_abs(x):
	if x>=0:
		return x
	else:
		return -x
print 'Functon has been defined!'
s=float(raw_input('Please input number:'))
print my_abs(s)