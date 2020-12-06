#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 23:12:38 2020

@author: rafi
"""

def get_fasta_from_file(filename):
    """ Read a fasta file (filename) from disk and return
    its full contents as a string"""
    inf = open(filename)
    data = inf.read()
    inf.close()
    return data

def table_print(sequence_list):
    print('|' + '-'*44 + '|')
    headerstr = '|{0:^14s}|{1:^14s}|{2:^14s}|' # Define table format strings
    tablestr = '|{0:^14s}|{1:^14.2f}|{2:^14s}|'
    print(headerstr.format('Block', 'CG Ratio', 'PolyA',))
    print(('|'+'-'*14)*3+'|')
    x_aft = 0
    for i in range(0, len(sequence_list)):
        
        CG_total = 0
        mxA = 0
        A = 0
        for x in sequence_list[i]:
            if x in 'CG':
                CG_total += 1
            if x in 'A' and A >= 0:
                A += 1
                if A > mxA:
                    mxA = A
            else:
                A = 0
        CG_Ratio = (CG_total/len(sequence_list[i])) 
 
        x_pre = x_aft + 1
        x_aft = x_aft + len(sequence_list[i])
        
        print(tablestr.format(str(x_pre) + ' - ' + str(x_aft), CG_Ratio, str(mxA)))
    print('|' + '-'*44 + '|')
    
full_list = get_fasta_from_file('example.fasta')
sequencename = full_list.split('\n')[0]
n = ''.join(full_list.split('\n')[1:])

x = 100 
split_list = [n[y-x:y] for y in range(x, len(n)+x, x)]

print()
print(sequencename)
print()
table_print(split_list) 


# url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=110645916&rettype=fasta"
# rf = urllib.request.urlopen(url)
# data = rf.read()
# rf.close()
# data = data.decode()
