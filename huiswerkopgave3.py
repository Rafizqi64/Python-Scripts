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
    headerstr = '{0:^14s} | {1:^12s} | {2:^14s}' # Define table format strings
    tablestr = '{0:^14s} | {1:^14f} | {2:^14f}'
    print(headerstr.format('Block', 'CG Ratio', 'PolyA',))
    print(('|'+'-'*14)*3+'|')
    
    for i in range(0, len(sequence_list)):
             C = sequence_list[i].count('C')
             G = sequence_list[i].count('G')
             CG_total = C+G
             CG_Ratio = (CG_total/len(sequence_list[i]))
#        for x in range(0, len(sequence_list[i])):
#            mxA = 0
#            if len(sequence_list.find(row[4]*x)) > mxA:
#                mxA = len(sequence_list.find(row[4]*x))
    print(tablestr.format(' ', CG_Ratio, ' '))

full_list = get_fasta_from_file('example.fasta')
sequencename = full_list[0: 105]
list_base_blocks = full_list[105 : ]
print(len(list_base_blocks))
n = list_base_blocks.split()
x=100 
split_list = [list_base_blocks[y-x:y] for y in range(x, len(list_base_blocks)+x, x)]
print(split_list)

print(table_print('n')) 
        
# import urllib
# url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=110645916&rettype=fasta"
# rf = urllib.request.urlopen(url)
# data = rf.read()
# rf.close()
# data = data.decode()