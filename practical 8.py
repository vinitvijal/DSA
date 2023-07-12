# Write a Program to accept a directed graph G and compute the in-degree and out-degree of each vertex.

class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def in_degree(self):
        in_degree = []
        for i in range(len(self.matrix)):
            count = 0
            for j in range(len(self.matrix)):
                if self.matrix[j][i] == 1:
                    count += 1
            in_degree.append(count)
        return in_degree
    
    def out_degree(self):
        out_degree = []
        for i in range(len(self.matrix)):
            count = 0
            for j in range(len(self.matrix)):
                if self.matrix[i][j] == 1:
                    count += 1
            out_degree.append(count)
        return out_degree
    
    def display(self):
        print("Adjacency Matrix Representation of Graph: ")
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                print(self.matrix[i][j], end = " ")
            print()

matrix = []
n = int(input("Enter number of vertices: "))
print("Enter Adjacency Matrix: ")
for i in range(n):
    matrix.append(list(map(int,input().split())))
g = Graph(matrix)
g.display()
print("In Degree: ",g.in_degree())
print("Out Degree: ",g.out_degree())
