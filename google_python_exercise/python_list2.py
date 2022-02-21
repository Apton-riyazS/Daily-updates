#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
#
# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
#
# Additional basic list exercises
#
# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove(l):
   # l=list(input('enter another one to sort').split())
    l =list(sorted(set(l)))
    print(str(l)) 
#l=list(input('enter another one to sort').split())
#remove(l)
# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def merge(l, r):
  # printing original lists 
  print ("The original list 1 is : " + str(l))
  print ("The original list 2 is : " + str(r))
  res = sorted(l + r)
  res =list(sorted(set(res)))
  print(str(res)) 
##################################################
##########################################1
 #####################################
l=list(input('enter  one list of number to sort and remove its adjecent').split())
remove(l)
########################################
l=list(input('enter list to sort ').split())
r=list(input('enter another one to sort').split())
merge(l,r)
############################
