n = int(input("Enter number of sides: "))

# First row
for i in range(1, n+1):
    print(i, end="")
print()

# Middle rows
for i in range(2, n):
    print(i, end="")
    for j in range(n-2):
        print(" ", end="")
    print(n - i + 1)

# Last row
for i in range(n, 0, -1):
    print(i, end="")
