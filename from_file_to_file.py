file_1 = open("file.txt", 'r')
lines = file_1.readlines()
# print("lines :", lines)

str_tab = []

for line in lines:
    smaller_tab = line.split("\t")
    if smaller_tab[-1][-1] == '\n':
        smaller_tab[-1] = smaller_tab[-1][:-1]
    str_tab.append(smaller_tab)

# print("str tab :", str_tab)

int_tab = []
new_smaller_tab = []

for line in str_tab:
    for number in line:
        new_smaller_tab.append(int(number))
    int_tab.append(new_smaller_tab)
    new_smaller_tab = []

# print("int tab :", int_tab)
tab_for_all = []

for tab in int_tab:
    for x in tab:
        tab_for_all.append(x)

# print(tab_for_all.count(99963))


print("tab_for_all :", tab_for_all)
print("amount of elements :", len(tab_for_all))

small = min(tab_for_all)
index_of_small = tab_for_all.index(small)
print("small :", small)
print("index_of_small :", index_of_small)

big = max(tab_for_all)
index_of_big = tab_for_all.index(big)
print("big :", big)
print("index_of_big :", index_of_big)

pre_small = tab_for_all[index_of_small - 1]
pre_big = tab_for_all[index_of_big - 1]


final_tab_for_all = []

final_tab_for_all.append(small)
final_tab_for_all.append(big)
final_tab_for_all.append(tab_for_all[index_of_small - 1])
final_tab_for_all.append(tab_for_all[index_of_big - 1])

print("\n")

print(tab_for_all.remove(small))
print(tab_for_all.remove(big))
print(tab_for_all.remove(index_of_small - 1))
print(tab_for_all.remove(index_of_big - 1))

print(final_tab_for_all)
# print(len(tab_for_all))

# for i in int_tab:
#     i.sort()
#
# print("int sorted tab :", int_tab)
#
# new_int_tab = []
#
# bigger_half_of_int_tab = []
# smaller_half_of_int_tab = []
#
# for tab in int_tab:
#     for i in range(8):
#         smaller_half_of_int_tab.append(tab[i])
#     for i in range(8):
#         bigger_half_of_int_tab.append(tab[8 + i])
#
#     bigger_half_of_int_tab.reverse()
#
#     new_int_tab.append([smaller_half_of_int_tab, bigger_half_of_int_tab])
#
#     bigger_half_of_int_tab = []
#     smaller_half_of_int_tab = []
#
# print("new int tab :", new_int_tab)
#
# final_tab = []
#
#
# for tab in new_int_tab:
#     smaller_tab = []
#     for i in range(8):
#         smaller_tab.append(tab[0][i])
#         smaller_tab.append(tab[1][i])
#     final_tab.append(smaller_tab)
#     smaller_tab = []
#
# print("final_tab :", final_tab)


file_1.close()
