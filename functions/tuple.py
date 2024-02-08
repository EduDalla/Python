my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3 # (1, 10, 100, 1, 10, 100, 1, 10, 100) because it's multiplying "THE LIST", not the numbers inside it

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

# a tuple cannot be changed by append or insert
# but can be changed by modification

tup = (1, 2, 4, 8)
tup = tup[1:-1]
tup = tup[0]
print(tup)
