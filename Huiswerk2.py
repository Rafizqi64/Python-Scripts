# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 20:45:12 2020

@author: rafizqi64
"""

import matplotlib

inf = open('seqhw2-1.txt', 'r')

s = inf.read().upper()
n = s.split()[2 : : 3]                                           #slice out everything but the sequences
print(n)                                                         #sequences

fragment = [['CG'], []]                                          #experimentation with arrays
mx = 0
for line in range(0,len(n)):                                     
        fragment[1].append(n[line].count(fragment[0][0]))        #make a list out of the 2nd array
        matplotlib.pyplot.plot(line+1, fragment[1][line], 'bo')  #draw graph
        matplotlib.pyplot.xlabel('Sequence number')
        matplotlib.pyplot.ylabel('numbers of CGs in sequence')
        print("Sequence", line+1, "has", fragment[1][line],"C")  #for checking the graph
        if fragment[1][line] > mx:                               #establish max CGs in 1 line 
            mx = fragment[1][line]

for value in range(mx):
    if fragment[1].count(value) == 1:
        print("there is", fragment[1].count(value), "sequence with", value, "CGs")
    else:
         print("there are", fragment[1].count(value), "sequences with", value, "CGs")

    
inf.close()
