my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new = my_list[0:]

for i in my_list:
    if i in new: # preste atenção no uso do "in"
        del my_list[i]

print("A lista com os elementos exclusivos aqui")
print(my_list)

