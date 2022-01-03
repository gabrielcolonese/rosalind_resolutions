# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 00:34:43 2021

@author: Gabriel
"""
import math

def comb(n, k):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    

k = 15 #homozygous dominant
m = 25 #heterozygous
n = 18 #homozygous recessive

pop = k+m+n

total_comb = comb(pop, 2) * 4

full_ht = comb(m, 2) * 1 
full_hr = comb(n, 2) * 4
ht_hr = m*n * 2

# up = full_ht + full_hr + ht_hr
# den = pop
# print(up)
# print(pop)
prob = 1-(full_ht + full_hr + ht_hr)/total_comb
print (full_ht)
print (full_hr)
print (ht_hr)
print (total_comb)
print(prob)