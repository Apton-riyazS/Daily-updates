#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
#
# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
#
# Basic list exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in list2.py.
#
# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
#
def match_ends(a):
  count = 0
  dict={}
  for i in a:
    if len(a) >= 2 and a[0] == [-1]:
      dict[i] = dict.get[i,0]+1
  print('number of strings is: ',count)
#
# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def sort(s):
    for i in s:
        if i[0] == 'x':
            xlist.append(i)
            s.remove(i)
    print((sorted(xlist))+(sorted(s)))
    del xlist[:]
#
# Extract the last element from a tuple -- used for custom sorting below.
#last element based sorting
def last(a):  
    lst = len(a)  
    for i in range(0, lst):  
          for j in range(0, lst-i-1):  
            if (a[j][-1] > a[j + 1][-1]):  
                b = a[j]  
                a[j]= a[j + 1]  
                a[j + 1]= b  
    print(a)  
#################################################################
# ####################################################
# ###############3output secssion#################    
a=list(input('enter a list of strings to count,last chars of the string are the same  ').split())
print(a)
match_ends(a)
###########################################
s=list(input('enter a list of strings for sorted by  start with x first : ').split())
xlist=[]
sort(s)
################################
a=list(input('enter a list to sort last element from a tuple in a sorted manner: ').split())
last(a)
#########################################
