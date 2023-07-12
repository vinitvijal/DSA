# Create a class RELATION, use Matrix notation to represent a relation. Include member functions to check if the relation is Reflexive, Symmetric, Anti-symmetric, Transitive. Using these functions check whether the given relation is: Equivalence or Partial Order relation or None

class Relation:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def is_reflexive(self):
        for i in range(len(self.matrix)):
            if self.matrix[i][i] != 1:
                return False
        return True
    
    def is_symmetric(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True
    
    def is_anti_symmetric(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j] == 1 and self.matrix[j][i] == 1 and i != j:
                    return False
        return True
    
    def is_transitive(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j] == 1:
                    for k in range(len(self.matrix)):
                        if self.matrix[j][k] == 1 and self.matrix[i][k] != 1:
                            return False
        return True
    
    def is_equivalence(self):
        if self.is_reflexive() and self.is_symmetric() and self.is_transitive():
            return True
        return False
    
    def is_partial_order(self):
        if self.is_reflexive() and self.is_anti_symmetric() and self.is_transitive():
            return True
        return False
    
    def is_none(self):
        if self.is_reflexive() == False and self.is_symmetric() == False and self.is_anti_symmetric() == False and self.is_transitive() == False:
            return True
        return False
    
    def display(self):
        print("Matrix Representation of Relation: ")
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                print(self.matrix[i][j], end = " ")
            print()
    
    def display_result(self):
        print("Reflexive: ",self.is_reflexive())
        print("Symmetric: ",self.is_symmetric())
        print("Anti Symmetric: ",self.is_anti_symmetric())
        print("Transitive: ",self.is_transitive())
        print("Equivalence: ",self.is_equivalence())
        print("Partial Order: ",self.is_partial_order())
        print("None: ",self.is_none())

matrix = []
n = int(input("Enter number of rows and column: "))
print("Enter matrix elements: ")
for i in range(n):
    matrix.append(list(map(int,input().split())))  

print(matrix)
# r = Relation(matrix)
