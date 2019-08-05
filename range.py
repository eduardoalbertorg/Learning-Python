# Write a script to generate the following list of numbers using range:

# Generate a list 'k1' having five continuous numbers starting from 0.
k1 = list(range(4))
# Print 'k1'.
print(k1)
# Generate a list 'k2' having five continuous numbers starting from 10.
k2 = list(range(10, 15))
# Print 'k2'.
print(k2)
# Generate a list 'k3' having even numbers between 10 and 20 (include 10 and 20).
k3 = list(range(10, 21, 2))
# Print 'k3'.
print(k3)
# Generate a list 'k4' having numbers from 100 to 1 in decreasing order, 
k4 = list()
for index in range(100, 1, -1):
    if(index % 25 == 0):
        k4.append(index)
# which are also multiples of 25.
# Print 'k4'.
print(k4)