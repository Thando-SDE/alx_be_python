size = int(input("Enter the size of the pattern: "))

row = 1

while row <= size:
    for col in range(1, size + 1):
        print("*", end="")
    print()
    row += 1
    