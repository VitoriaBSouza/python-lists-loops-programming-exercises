# Your code here
def matrix_builder(int):
    aux = []
    
    for i in range(int):
        row = []
        for x in range(int):
            row.append(1)
        aux.append(row)
        
    return aux

print(matrix_builder(3))