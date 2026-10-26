# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 17:08:16 2026

@author: darij
"""

# for i in range(10):
#     if i % 2 == 0:
#         print(i)
        
# s = "demo loops - fruit loops"
# for index in range(len(s)):
#     if s[index] =="i" or s[index] == "u":
#         print("There is an i or u")

# for char in s:
#     if char == "i" or char =="u":
#         print("There is an i or u")

# for char in s:
#     if char in 'iu':
#         print("There is an i or u")

an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))

for w in word:
    if w in an_letters:
        #print(f'Give me an {c} : {c}') # with f-strings
        print("Give me an " + w + ": " + w)
    else:
        #print(f'Give me a {c} : {c}') # with f-strings
        print("Give me a " + w + ": " + w)
print("What does that spell? ")
for i in range(times):
    print(word, "!!!")
