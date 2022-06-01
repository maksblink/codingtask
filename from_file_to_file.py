file = open("file.txt", 'r')
lines = file.readlines()

str_tab = []

# separator = input("What kind of separator did you use? :")
separator = '\t'
print("Separator is :", separator)

print("\n")

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

sorted_tab = sorted(tab_for_all)

print("sorted_tab :", sorted_tab)

interation = len(sorted_tab)

bigger_half_of_int_tab = []
smaller_half_of_int_tab = []

for i in range(int(interation / 2)):
    smaller_half_of_int_tab.append(sorted_tab[i])
    bigger_half_of_int_tab.append(sorted_tab[interation - 1 - i])

print("smaller_half_of_int_tab :", smaller_half_of_int_tab)
print("bigger_half_of_int_tab :", bigger_half_of_int_tab)
print("len smaller_half_of_int_tab :", len(smaller_half_of_int_tab))
print("len bigger_half_of_int_tab :", len(bigger_half_of_int_tab))

final_tab = []

for i in range(int(interation / 2)):
    final_tab.append(smaller_half_of_int_tab[i])
    final_tab.append(bigger_half_of_int_tab[i])

if len(sorted_tab) % 2 != 0:
    index_of_last_index = int(interation / 2)
    final_tab.append(sorted_tab[index_of_last_index])

print("final_tab :", final_tab)
print(len(final_tab))

file.close()

new_file = open("new_file.txt", 'w')

final_str = ""

counter = 0

try:
    for i in range(vertically):
        for j in range(horizontally):
            final_str += str(final_tab[counter])
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
