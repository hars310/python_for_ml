def printFibSeries(length):
    prev, prev2 = 1, 0
    for _ in range(length):
        print(prev, end=" ")
        next_val = prev + prev2
        prev2 = prev
        prev = next_val

# Get input from the user
len = int(input("Length of series: "))
printFibSeries(len)
print("\n")
