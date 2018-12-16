#!/usr/bin/python3
import sys

def match_paren(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(': 
            stack.append(i)
        elif s[i] == ')':
            if len(stack) == 0: 
                return i
            else: 
                stack.pop()
    if len(stack) != 0:
        return stack.pop(0)
    return False

if __name__ == '__main__':
    i = 1
    for line in sys.stdin:
        col = match_paren(line)
        if (col):
            print("There is a unbalanced parenthesis on line " + \
                   "{} at column {}".format(i, col))
        i += 1


