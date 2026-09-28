import numpy as np

def main():
    # --- Method 1: Standard Python List ---
    print("=== Addition using Python List ===")
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    
    # Initialize result matrix with zeros, then add elements
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            C[i][j] = A[i][j] + B[i][j]
            
    print("A:", A, "\nB:", B, "\nResult C:", C)

    # --- Method 2: Using NumPy ---
    print("\n=== Addition using NumPy ===")
    A_np = np.array(A)
    B_np = np.array(B)
    
    print("Result C:\n", A_np + B_np)

if __name__ == "__main__":
    main()
