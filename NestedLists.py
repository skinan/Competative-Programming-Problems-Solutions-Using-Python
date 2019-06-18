# Practice > PythonBasic > Data Types > Nested Lists
# HackerRank

testlist = [[input(),float(input())] for i in range(int(input()))]

temp = sorted(set(a[1] for a in testlist))

for answer in sorted(a[0] for a in testlist if a[1] == temp[1]):
    print(answer)
