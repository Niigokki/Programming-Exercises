#Author - Jacob Smith
#trying to gain more python experience
#problem taken from https://www.hackerrank.com/challenges/compress-the-string/problem
from itertools import groupby
test = input()
for x, y in groupby(test):
    print((len(list(y)), int(x)))
