n = int(input("Enter the number of elements you want in your list: "))
arr = []
for i in range(n):
 arr.append(input(f"Enter element {i + 1}: "))
# Ensure the list is sorted
arr.sort()
print("Sorted list:", *arr ,sep=" , ")
value = input("Enter the element you want to find: ")
low = 0
high = len(arr) - 1
found = False
while low <= high:
 mid = (low + high) // 2
 if arr[mid] == value:
  print(f"The element '{value}' is found at index {mid}")
  found = True
  break
 elif arr[mid] < value:
  low = mid + 1
else:
 high = mid - 1
if not found:
 print("Element cannot be found in the list")