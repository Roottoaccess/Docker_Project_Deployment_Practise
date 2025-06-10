# Applying the linear searching using the python script....

# Creating an Empty list and taking the imput from the user and apply it in the empty list

arr = [] # Empty list
limit = int(input("Enter the limit of the list: ")) # Limit of the list

for i in range(limit):
    val = int(input("Value: "))
    arr.append(val) # Appending the value and inserting into the list

print(f'Current List: {arr}') # Printing the list to the user
# Taking the input of the key from the user....
key = int(input("Enter the key to search: "))
count = 0
for i in arr:
    count += 1
    if i == key:
        print(f"Value found in {count} position")
        break