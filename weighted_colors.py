# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 14:44:30 2013

@author: Pete
"""
import itertools as itr
from random import choice

N=3
M=3


Preferences = []

for i in range(M):
    Preferences.append('o%s'%i)

permutations = list(itr.permutations(Preferences,len(Preferences)))

print(choice(permutations))


