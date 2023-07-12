# Write a Program to evaluate a polynomial function. (For example store f(x) = 4n2 + 2n + 9 in an array and for a given value of n, say n = 5, compute the value of f(n)).

equ = list(map(int,input("Enter coefficients of polynomial: ").split()))
n = int(input("Enter value of n: "))
sum = 0
for i in range(len(equ)-1,-1,-1):
    sum += equ[i]*n**i
print("Value of polynomial: ",sum)
