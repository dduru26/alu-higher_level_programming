#@/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            # Use str.format() to print the integers, followed by a space
            print("{}".format(row[i]), end="")
            if i < len(row) - 1:
                print(" ", end="")  # Print a space between numbers
        print()  # Print a new line after each row
