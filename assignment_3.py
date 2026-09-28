def is_right_angled(a, b, c):
    sides = sorted([a, b, c])
    return (sides[0]**2 + sides[1]**2) == sides[2]**2

def main():
    print("=== Assignment 3: Right Angled Triangle Check ===\n")
    a = int(input("Enter side 1: "))
    b = int(input("Enter side 2: "))
    c = int(input("Enter side 3: "))

    if is_right_angled(a, b, c):
        print(f"\nTriangle with sides {a},{b},{c} IS a Right Angled Triangle.")
    else:
        print(f"\nTriangle with sides {a},{b},{c} is NOT a Right Angled Triangle.")

if __name__ == "__main__":
    main()
