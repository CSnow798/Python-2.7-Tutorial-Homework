#!/usr/bin/env python 
age=raw_input('Please input your age:')
age=int(age)

if age>=18:
	print 'adult' #'Your age is ', age,'. You are adult.'
elif age>=6:
	print 'teenager' #'Your age is ', age, '. You are kid.'
else:
	print 'kid' #'Your age is ', age, '. You are teenager.'

