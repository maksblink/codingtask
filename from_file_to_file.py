file = open("file.txt", 'r')
lines = file.readlines()
print("lines :", lines)

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

print("int tab :", int_tab)
tab_for_all = []

for tab in int_tab:
    for x in tab:
        tab_for_all.append(x)

print("tab_for_all :", tab_for_all)
print("amount of elements in the list :", len(tab_for_all))

print("\n")
final_tab_for_all = []

if len(tab_for_all) % 4 == 0:
    what_to_do = 'nothing'

elif len(tab_for_all) % 4 == 1:
    what_to_do = "new small"

elif len(tab_for_all) % 4 == 2:
    what_to_do = "new small, new big"

elif len(tab_for_all) % 4 == 3:
    what_to_do = "new small, new big, new pre small"

for i in range(int(len(tab_for_all) / 4)):
    small = min(tab_for_all)
    index_of_small = tab_for_all.index(small)

    final_tab_for_all.append(small)

    big = max(tab_for_all)
    index_of_big = tab_for_all.index(big)

    final_tab_for_all.append(big)

    tab_for_all.remove(small)
    tab_for_all.remove(big)

    if index_of_small != 0:
        if index_of_small < index_of_big:
            index_of_pre_small = index_of_small - 1
            pre_small = tab_for_all[index_of_pre_small]
        else:
            index_of_pre_small = index_of_small - 2
            pre_small = tab_for_all[index_of_pre_small]
    else:
        index_of_pre_small = len(tab_for_all) - 1
        pre_small = tab_for_all[index_of_pre_small]

    final_tab_for_all.append(pre_small)
    tab_for_all.remove(pre_small)

    if index_of_big != 0:
        if index_of_big < index_of_small:
            if index_of_big < index_of_pre_small:
                index_of_pre_big = index_of_big - 1
                pre_big = tab_for_all[index_of_pre_big]
            else:
                index_of_pre_big = index_of_big - 2
                pre_big = tab_for_all[index_of_pre_big]
        else:
            if index_of_big < index_of_pre_small:
                index_of_pre_big = index_of_big - 2
                pre_big = tab_for_all[index_of_pre_big]
            else:
                index_of_pre_big = index_of_big - 3
                pre_big = tab_for_all[index_of_pre_big]
    else:
        index_of_pre_big = len(tab_for_all) - 1
        pre_big = tab_for_all[index_of_pre_big]

    final_tab_for_all.append(pre_big)

    tab_for_all.remove(pre_big)

    # print("final_tab_for_all :", final_tab_for_all)
    # print("amount of elements left in the list:", len(tab_for_all))

if what_to_do == 'nothing':
    pass

elif what_to_do == 'new small':
    small = min(tab_for_all)
    final_tab_for_all.append(small)

elif what_to_do == 'new small, new big':
    small = min(tab_for_all)
    final_tab_for_all.append(small)
    big = max(tab_for_all)
    final_tab_for_all.append(big)

elif what_to_do == 'new small, new big, new pre small':
    small = min(tab_for_all)
    final_tab_for_all.append(small)
    big = max(tab_for_all)
    final_tab_for_all.append(big)
    tab_for_all.remove(small)
    tab_for_all.remove(big)
    final_tab_for_all.append(tab_for_all[0])

print("final_tab_for_all :", final_tab_for_all)
print("final_tab_for_all :", tab_for_all)
print("final_tab_for_all :", len(final_tab_for_all))

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
