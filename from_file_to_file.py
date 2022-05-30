file_1 = open("file.txt", 'r')
lines = file_1.readlines()
# print(lines)

tab = []

for line in lines:
    smaller_tab = line.split("\t")
    if smaller_tab[-1][-1] == '\n':
        smaller_tab[-1] = smaller_tab[-1][:-1]
    tab.append(smaller_tab)

print(tab)

new_tab = []
new_smaller_tab = []

for line in tab:
    for number in line:
        new_smaller_tab.append(int(number))
    new_tab.append(new_smaller_tab)
    new_smaller_tab = []


print(new_tab)

# counter_line = 0
# counter_number = 0
#
#
# for line in tab:
#     for number in line:
#         tab[counter_line][counter_number] = int(number)
#     counter_number = 0
#
# print(tab)

# for i in tab:
#     i.sort()

# print(tab)
# tab_sort =


# add_some_zeros(tab)
# print(tab)

# for i in tab:
#     print(len(i))
#
#
# # file.close()
