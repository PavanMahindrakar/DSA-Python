# Recursion example to print "Hello World" n times
# Time Complexity: O(n)

def PrintN_times(i,n):
    if i > n:
        return
    print("Hello World")
    PrintN_times(i + 1, n)

n = int(input("Number of times to print : "))
PrintN_times(1, n)
