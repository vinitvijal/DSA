# For any number n, write a program to list all the solutions of the equation x1 + x2 + x3 + ...+ xn = C, where C is a constant (C<=10) and x1, x2,x3,...,xn are nonnegative integers, using brute force strategy.

c = int(input("Enter constant: "))
n = int(input("Enter number of variables: "))
l = []
for i in range(n):
    l.append(0)
while True:
    sum = 0
    for i in range(n):
        sum += l[i]
    if sum == c:
        print(l)
    l[n-1] += 1
    for i in range(n-1,0,-1):
        if l[i] == c+1:
            l[i] = 0
            l[i-1] += 1
    if l[0] == c+1:
        break


