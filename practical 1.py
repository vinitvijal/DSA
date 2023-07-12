# Create a class SET. Create member functions to perform the following SET operations:
# 1) ismember: check whether an element belongs to the set or not and return value as true/false.
# 2) powerset: list all the elements of the power set of a set .
# 3) subset: Check whether one set is a subset of the other or not.
# 4) union and Intersection of two Sets.
# 5) complement: Assume Universal Set as per the input elements from the user.
# 6) set Difference and Symmetric Difference between two sets.
# 7) cartesian Product of Sets

class Set:
    def __init__(self, set1):
        self.set1 = set1

    def ismember(self, element):
        if element in self.set1:
            return True
        else:
            return False

    def powerset(self):
        power_set = [[]]
        for i in self.set1:
            for j in power_set:
                power_set = power_set + [list(j) + [i]]
        return power_set

    def subset(self, set2):
        for i in set2:
            if i not in self.set1:
                return False
        return True


    def union(self, set2):
        return self.set1.union(set2)
    
    def intersection(self, set2):
        return self.set1.intersection(set2)
    
    def complement(self, universal_set):
        return universal_set.difference(self.set1)
    
    def set_difference(self, set2):
        return self.set1.difference(set2)
    
    def symmetric_difference(self, set2):
        return self.set1.symmetric_difference(set2)
    
    def cartesian_product(self, set2):
        cartesian_product = []
        for i in self.set1:
            for j in set2:
                cartesian_product.append((i,j))
        return cartesian_product
    

set1 = set(map(int,input("Enter elements of set1: ").split()))
s = Set(set1)
num = int(input("Enter element to check: "))
print('Element Exist in Set :',s.ismember(num))


powerset = s.powerset()
print("Power Set of Set: ", powerset)

set2 = set(map(int,input("Enter elements of set2: ").split()))
print("Set2 is subset of Set1: ", s.subset(set2))

print("Union of Set1 and Set2: ", s.union(set2))
print("Intersection of Set1 and Set2: ", s.intersection(set2))

universal_set = set1 = set(map(int,input("Enter elements of universal set: ").split()))
print("Complement of Set1: ", s.complement(universal_set))

print("Set Difference of Set1 and Set2: ", s.set_difference(set2))
print("Symmetric Difference of Set1 and Set2: ", s.symmetric_difference(set2))

print("Cartesian Product of Set1 and Set2: ", s.cartesian_product(set2))