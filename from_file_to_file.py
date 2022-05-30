file_1 = open("file.txt", 'r')
lines = file_1.readlines()
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

for i in int_tab:
    i.sort()

print("int sorted tab :", int_tab)

new_int_tab = []

bigger_half_of_int_tab = []
smaller_half_of_int_tab = []

for tab in int_tab:
    for i in range(8):
        smaller_half_of_int_tab.append(tab[i])
    for i in range(8):
        bigger_half_of_int_tab.append(tab[8 + i])

    bigger_half_of_int_tab.reverse()

    new_int_tab.append([smaller_half_of_int_tab, bigger_half_of_int_tab])

    bigger_half_of_int_tab = []
    smaller_half_of_int_tab = []

print("new int tab :", new_int_tab)

final_tab = []

counter = 0

for tab in new_int_tab:
    smaller_tab = []
    for i in range(8):
        smaller_tab.append(tab[0][i])
        smaller_tab.append(tab[1][i])
    final_tab.append(smaller_tab)
    smaller_tab = []

print("final_tab :", final_tab)

file_1.close()
