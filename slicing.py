# Consider the list 'k' with seven numbers [3, 4, 5, 6, 7, 8, 9].
# Perform the following tasks, and print the outputs in separate lines:

# Print the list of alternative numbers, using the slicing option, starting from '3'.
# Print the list of alternative numbers obtained from the first 4 elements only.
# Print the list of odd indexed elements of list 'k'.
# Since indexing starts at zero, odd indices would be 1,3, and so on.

k = [3, 4, 5, 6, 7, 8, 9]
print(k[0::2])
print(k[0:4:2])
print(k[1::2])