file_1 = open("file.txt", 'r')
lines = file_1.readlines()
print("lines: ", lines)

str_tab = []

for line in lines:
    smaller_tab = line.split("\t")
    if smaller_tab[-1][-1] == '\n':
        smaller_tab[-1] = smaller_tab[-1][:-1]
    str_tab.append(smaller_tab)

print("str tab :", str_tab)

int_tab = []
new_smaller_tab = []

for line in str_tab:
    for number in line:
        new_smaller_tab.append(int(number))
    int_tab.append(new_smaller_tab)
    new_smaller_tab = []

print("new tab :", int_tab)

for i in int_tab:
    i.sort()

print("new sorted tab :", int_tab)

smaller_half_of_new_tab = []
bigger_half_of_new_tab = []

new_new_tab = []

counter = 1

for tab in int_tab:
    new_new_tab.append([])

    counter += 1

i = 1

# while i <= 8:
#     print(i)
#     i += 1

###
###
###
###

file_1.close()
