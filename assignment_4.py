import numpy as np

def main():
    print("Addition using Python List")
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            C[i][j] = A[i][j] + B[i][j]
            
    print("A:", A, "B:", B, "Result C:", C)

    
print("Addition using NumPy")
    A_np = np.array(A)
    B_np = np.array(B)
    
    print("Result C:", A_np + B_np)

    main()
