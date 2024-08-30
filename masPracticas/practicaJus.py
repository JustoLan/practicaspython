numbers1 = [1, 0, 3, 8, 6, 0, 2, 9, 7, 4, 5, 0, 3, 6, 2, 0, 8, 1, 9, 7]
numbers2 = [4, 0, 5, 9, 1, 0, 6, 7, 3, 2, 8, 0, 5, 1, 4, 0, 9, 2, 6, 3]
numbers3 = [7, 0, 2, 5, 4, 0, 9, 6, 1, 3, 8, 0, 2, 7, 5, 0, 4, 6, 9, 1]

lists = [numbers1, numbers2, numbers3]

for num_list in lists:
    numbers0end = []

    for num in num_list:
        if num == 0:
            numbers0end.append(num)
        else:
            numbers0end.insert(len(numbers0end) - numbers0end.count(0), num)
    print(numbers0end) y