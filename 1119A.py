# 1119A - Ilya and a Colorful Walk



n = int(input()) 
y = input().split(" ")

j = n - 1

while y[0] == y[n - j - 1] == y[j]:
    j -= 1
    
print(j)
