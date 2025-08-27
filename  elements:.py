n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

# Find max
largest = arr[0]
for num in arr:
    if num > largest:
        largest = num

print("Largest element:", largest)