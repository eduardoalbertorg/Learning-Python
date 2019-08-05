# Consider the string 's' contains the value 'tata consultancy services limited'.

# Determine the no. of vowels present in it, using the "while" loop.
# Store the number in the variable 'count', and print it.

index = 0
count = 0
s = 'tata consultancy services limited'
string_length = len(s) - 1
while(index < string_length):
    if('a' in s[index]
    or 'e' in s[index]
    or 'i' in s[index]
    or 'o' in s[index]
    or 'u' in s[index]):
        count = count + 1
    index = index + 1
print(count)