import numpy as np

# -------------------------------------------------------
#                   UI DISPLAY HELPERS
# -------------------------------------------------------

def print_header():
    print("\n📌 MATRIX OPERATIONS TOOL\n")

def print_menu():
    print("Choose an operation:")
    print("  1️⃣  Matrix Addition")
    print("  2️⃣  Matrix Subtraction")
    print("  3️⃣  Matrix Multiplication")
    print("  4️⃣  Matrix Transpose")
    print("  5️⃣  Matrix Determinant")
    print("  6️⃣  Exit")

def print_section(title):
    print(f"\n🔹 {title}")

def print_matrix(label, matrix):
    print(f"\n📘 {label}:")
    print(matrix)


# -------------------------------------------------------
#               MATRIX INPUT FUNCTION
# -------------------------------------------------------

def input_matrix(name):
    try:
        print_section(f"Enter details for {name}")
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        print("\nEnter elements row-wise (space-separated):")
        nums = list(map(float, input("➤ ").split()))

        if len(nums) != rows * cols:
            print("\n❌ ERROR: Provided elements do not match matrix size.")
            return None

        matrix = np.array(nums).reshape(rows, cols)
        print_matrix(name, matrix)
        return matrix

    except:
        print("\n❌ ERROR: Invalid input. Please enter numeric values only.")
        return None


# -------------------------------------------------------
#               OPERATION FUNCTIONS
# -------------------------------------------------------

def add_matrices():
    print_section("Matrix Addition")
    A = input_matrix("Matrix A")
    B = input_matrix("Matrix B")
    if A is None or B is None:
        return
    if A.shape != B.shape:
        print("\n❌ ERROR: Matrices must have the same dimensions for addition.")
        return
    print_matrix("Result (A + B)", A + B)


def subtract_matrices():
    print_section("Matrix Subtraction")
    A = input_matrix("Matrix A")
    B = input_matrix("Matrix Matrix B")
    if A is None or B is None:
        return
    if A.shape != B.shape:
        print("\n❌ ERROR: Matrices must have the same dimensions for subtraction.")
        return
    print_matrix("Result (A - B)", A - B)


def multiply_matrices():
    print_section("Matrix Multiplication")
    A = input_matrix("Matrix A")
    B = input_matrix("Matrix B")
    if A is None or B is None:
        return
    if A.shape[1] != B.shape[0]:
        print("\n❌ ERROR: Columns of A must equal rows of B.")
        return
    print_matrix("Result (A × B)", np.dot(A, B))


def transpose_matrix():
    print_section("Matrix Transpose")
    A = input_matrix("Matrix")
    if A is None:
        return
    print_matrix("Transpose", A.T)


def determinant_matrix():
    print_section("Matrix Determinant")
    A = input_matrix("Matrix")
    if A is None:
        return
    if A.shape[0] != A.shape[1]:
        print("\n❌ ERROR: Only square matrices have determinants.")
        return
    det = np.linalg.det(A)
    print(f"\n🔹 Determinant: {round(float(det), 4)}")


# -------------------------------------------------------
#                   MAIN PROGRAM LOOP
# -------------------------------------------------------

def main():
    print_header()

    while True:
        print_menu()
        choice = input("\nEnter your choice: ").strip()

        operations = {
            "1": add_matrices,
            "2": subtract_matrices,
            "3": multiply_matrices,
            "4": transpose_matrix,
            "5": determinant_matrix
        }

        if choice == "6":
            print("\n✨ Exiting Matrix Operations Tool. Goodbye 👋\n")
            break

        operation = operations.get(choice)
        if operation:
            operation()
        else:
            print("\n❌ Invalid choice. Please select a valid option.")

        print()  # clean spacing


# Run Program
if __name__ == "__main__":
    main()
