file = open("file.txt", 'r')
lines = file.readlines()

str_tab = []

separator = input("What kind of separator did you use? :")
print("Separator is :", separator)

for line in lines:
    smaller_tab = line.split(separator)
    if smaller_tab[-1][-1] == '\n':
        smaller_tab[-1] = smaller_tab[-1][:-1]
    str_tab.append(smaller_tab)

try:
    horizontally = len(smaller_tab)
    vertically = len(str_tab)

except NameError:
    print("Your matrix may be empty.")

int_tab = []
new_smaller_tab = []

try:
    for line in str_tab:
        for number in line:
            new_smaller_tab.append(int(number))
        int_tab.append(new_smaller_tab)
        new_smaller_tab = []

except ValueError:
    print("Something is wrong with your matrix.")

tab_for_all = []

for tab in int_tab:
    for x in tab:
        tab_for_all.append(x)

print("tab_for_all :", tab_for_all)
print("Amount of elements in the list :", len(tab_for_all))

print("\n")

final_tab_for_all = []

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

if len(tab_for_all) % 4 == 1:
    final_tab_for_all.append(tab_for_all[0])

elif len(tab_for_all) % 4 == 2:
    small = min(tab_for_all)
    final_tab_for_all.append(small)
    big = max(tab_for_all)
    final_tab_for_all.append(big)

elif len(tab_for_all) % 4 == 3:
    small = min(tab_for_all)
    final_tab_for_all.append(small)
    tab_for_all.remove(small)
    big = max(tab_for_all)
    final_tab_for_all.append(big)
    tab_for_all.remove(big)
    final_tab_for_all.append(tab_for_all[0])

print("final_tab_for_all :", final_tab_for_all)
print("Amount of elements in final_tab_for_all :", len(final_tab_for_all))

file.close()

new_file = open("new_file.txt", 'w')

final_str = ""

counter = 0

try:
    for i in range(vertically):
        for j in range(horizontally):
            final_str += str(final_tab_for_all[counter])
            if j - horizontally != -1:
                final_str += '\t'
            counter += 1
        if i - vertically != -1:
            final_str += '\n'

except NameError:
    print("Your matrix may be empty.")

except IndexError:
    print("Something is wrong with your matrix.")

new_file.write(final_str)

new_file.close()
