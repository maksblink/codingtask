file_1 = open("file.txt", 'r')
lines = file_1.readlines()
print(lines)

tab = []

for line in lines:
    smaller_tab = line.split("\t")
    if smaller_tab[-1][-1] == '\n':
        smaller_tab[-1] = smaller_tab[-1][:-1]
    tab.append(smaller_tab)

print(tab)

# def add_some_zeros(tab):
#     max_lenght = max(len(elem) for elem in tab)
#     for t in tab:
#         a = max_lenght - len(t)
#         for i in range(a):
#             t.append(None)
#     return tab


# add_some_zeros(tab)
# print(tab)

# for i in tab:
#     print(len(i))


# file.close()
