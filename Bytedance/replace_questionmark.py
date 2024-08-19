# encoding: utf-8

"""
题目：
给定一个由 4 种字符 012? 组成的数组，其中 ? 可以被任意替换成 012 中的一个，问这个数组所有问号被替换后能形成多少种可能性，使得任意相邻两个字符不同。

例子
input= 00?1?
output= 0

input= 012
output= 1

input= 0??1?
output= 6

有6种可能性
01010
01210
02010
01212
01012
02012

input= 0??????2??201???
output= 688

"""

import sys

def get_possibilities(s) -> int:
    result = 1
    for i in range(0, len(s)):
        if s[i] == '?':
            for j in ['0', '1', '2']:
                if i > 0 and s[i-1] == j:
                    continue
                temp = j + s[i+1:]
                result += get_possibilities(temp)
            break
        elif i > 0 and s[i] == s[i-1]:
            print("mismatch", s[i-1], s[i])
            return 0
    if result > 1:
        return result-1
    return result

print(get_possibilities(sys.stdin.readline()))
