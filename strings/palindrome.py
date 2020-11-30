# -*- coding: utf-8 -*-
"""
Palindrome Question: Check if the string is a palindrome or not.
"""

"""
Algorithm

naman <- n = n, a = a, m = m done
AAAA <- A = A, A = A done
Best <- B != t done
"""

word = "naman"

length_word = len(word)


i=0
j= length_word-1

is_palindrome = True

while(j >= length_word/2):
    if(word[i]!=word[j]):
        print("Not a palindrome")
        is_palindrome = False
        break

    i=+1
    j=-1

if(is_palindrome):
    print("Is a palindrome")
