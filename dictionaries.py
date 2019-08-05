# Write a script that performs the following tasks serially:
# 
# Create an empty Dictionary, 'd1' using the 'dict' function.
d1 = dict()
# Print 'd1'.
print(d1)
# Create a Dictionary 'd2' with key values p-play , t-talk.
d2 = {'p-play': 0, 't-talk' : 1}
# Print 'd2'.
print(d2)
# Add two new key values: v-vibe, d-docs.
d2['v-vibe'] = 2
d2['d-docs'] = 3
# Print 'd2'.
print(d2)
# Remove the key value pair, 'v' - vibe, from 'd2'
d2.pop('v-vibe')
# print 'd2'
print(d2)