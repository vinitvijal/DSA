# Write a Program to check if a given graph is a complete graph. Represent the graph using the Adjacency Matrix representation.

class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def is_complete(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if i != j and self.matrix[i][j] != 1:
                    return False
        return True
    
    def display(self):
        print("Adjacency Matrix Representation of Graph: ")
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                print(self.matrix[i][j], end = " ")
            print()
    
    def display_result(self):
        print("Complete: ",self.is_complete())

matrix = []
n = int(input("Enter number of vertices: "))
print("Enter Adjacency Matrix: ")
for i in range(n):
    matrix.append(list(map(int,input().split())))
g = Graph(matrix)
g.display()
g.display_result()
