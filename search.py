# -*- coding: utf-8 -*-

import math

def binary_search_rec(A,v,left,right):
    if (right >= left):
        mid = left + (right - left)//2 # using `(right + left)//2` can lead to an integer overflow
        if (v == A[mid]):
            return mid
        elif (v < A[mid]):
            return binary_search_rec(A,v,left,mid-1)
        else:
            return binary_search_rec(A,v,mid+1,right)
    
    return -1
        
## Q1 ##
def binary_search(A,v):
    pass

def cost_binary_search(n):
    pass
    
## Q2 ##
def ternary_search(A,v):
    pass

def cost_ternary_search(n):
    pass
    
def cost_binary_search_value(A,v):
    # if len(A) == 0: return 1
    left = 0
    right = len(A) - 1

    cost = 1
    while (right >= left):
        mid = left + (right - left)//2
        cost += 1 
        if (v == A[mid]):
            return cost
        else: # decomposed elif into else if, then inserted "cost += 1" before the if
            cost += 1
            if (v < A[mid]):
                right = mid - 1
            else:
                left = mid + 1
        cost += 1

    return cost

def cost_ternary_search_value(A,v):
    pass

## Q3 ##
def exponential_search(A,v):
    pass

def cost_exponential_search(v):
    pass

## Q4 ##
def interpolation_search(A,v):
    pass

## Q6 ##
def findFirstOccurrence(A, v):
    pass

def findLastOccurrence(A, v):
    pass

## Q7 ##
def findKClosestElements(A, v, k):
    pass

## Q8 ##
def findFrequency(A):
    pass
