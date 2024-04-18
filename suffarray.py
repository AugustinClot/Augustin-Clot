# -*- coding: utf-8 -*-

def str_compare(a, b):
    N = min(len(a),len(b))
    for i in range(N):
        if a[i] < b[i]:
            return -1
        elif a[i] > b[i]:
            return 1

    return len(a)-len(b)

def str_compare_m(a,b, m):
    if len(a) >= m and len(b) >= m:
        # len(a) >= m and len(b) >= m
        return str_compare(a[:m], b[:m])
    else:
        # len(a) < m or len(b) > m
        return str_compare(a,b)

def longest_common_prefix(a, b):
    N = min(len(a),len(b))
    for i in range(N):
        if a[i] != b[i]:
            return i
    return N


class suffix_array:

    # Question 1
    def __init__(self, t):

    # Question 2
    def suffix(self, i):
        pass

    # Question 3
    def findL(self, S):
        pass

    def findR(self,S):
        pass

    # Question 4
    def findLR(self,S):
        return (self.findL(S),self.findR(S))

# Question 5
def KWIC(sa, S, c = 15):
    pass

# Question 6
def longest_repeated_substring(sa):
    pass
