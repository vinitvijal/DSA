# Write a Program that generates all the permutations of a given set of digits, with or without repetition.


def permutation(s):
    if len(s) == 0:
        return []
    if len(s) == 1:
        return [s]
    l = []
    for i in range(len(s)):
        m = s[i]
        rem = s[:i] + s[i+1:]
        for p in permutation(rem):
            l.append([m] + p)
    return l


s = list(map(int,input("Enter elements of set: ").split()))
print("Permutations of Set: ", permutation(s))
