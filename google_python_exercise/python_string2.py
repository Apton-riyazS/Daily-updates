#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
#
# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
#
# Additional basic string exercises
#
# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
#def verbing(s):
    if len(s) >= 3 :
        if s[-3:] == 'ing' :
            a = s[0:-3]
            print(a+str('ly'))
        else:
            #a = s[0:-3]
            print(s+ str('ing'))
    else:
        print('string is : ',s)
#s=input('enter a string to test verbing func: ')
#verbing(s)
#
# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
#def not_bad(s):
 # # +++your code here+++
  #return
# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a):
    len(a)/ 2
    if len(a)%2 ==0:
            print(a)
    else:
        b=len(a)/2
        c=len(a)/2
        #if len(a)%2==1:
        b=a[-1:]
        c=a[-1:]
            #print(a[0:2]+a[-1:]+a[2:])
        print(a[0:-2]+a[0:-2]+b[-1:]+c[-1:])
###########################
 # print( )
 # print(  'not_bad')
 # test(not_bad('This movie is not so bad'), 'This movie is good')
  #test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  #test(not_bad('This tea is not hot'), 'This tea is not hot')
  #test(not_bad("It's bad yet not"), "It's bad yet not")
#########################
a=input('enter a string ')
front_back(a)
##################################
s=input('enter a string to test verbing func: ')
verbing(s)
###############################
