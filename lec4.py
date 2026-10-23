# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 17:08:16 2026

@author: darij
"""

# for i in range(10):
#     if i % 2 == 0:
#         print(i)
        
s = "demo loops - fruit loops"
# for index in range(len(s)):
#     if s[index] =="i" or s[index] == "u":
#         print("There is an i or u")

# for char in s:
#     if char == "i" or char =="u":
#         print("There is an i or u")

for char in s:
    if char in 'iu':
        print("There is an i or u")