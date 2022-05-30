file = open("file.txt", 'r')
lines = file.readlines()
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
print("amount of elements in the list :", len(tab_for_all))

print("\n")
final_tab_for_all = []

# for i in range(len(tab_for_all) / 4):
for i in range(124):
    small = min(tab_for_all)
    index_of_small = tab_for_all.index(small)
    if index_of_small != 0:
        pre_small = tab_for_all[index_of_small - 1]
    else:
        pre_small = tab_for_all[len(tab_for_all) - 1]

    # print("small :", small)
    # print("pre small :", pre_small)

    # print("\n")

    big = max(tab_for_all)
    index_of_big = tab_for_all.index(big)
    if index_of_big != 0:
        pre_big = tab_for_all[index_of_big - 1]
    else:
        pre_big = tab_for_all[len(tab_for_all) - 1]
    # print("big :", big)
    # print("pre big :", pre_big)

    final_tab_for_all.append(small)
    final_tab_for_all.append(big)
    final_tab_for_all.append(pre_small)
    final_tab_for_all.append(pre_big)

    # print("\n")

    tab_for_all.remove(small)
    tab_for_all.remove(big)
    tab_for_all.remove(pre_small)
    tab_for_all.remove(pre_big)

    print("final_tab_for_all :", final_tab_for_all)
    print("amount of elements left in the list:", len(tab_for_all))

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


file.close()
