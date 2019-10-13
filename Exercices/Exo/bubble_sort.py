def bubble_sort(list_to_sort):
    for i in range(len(list_to_sort)):
        for j in range(len(list_to_sort) - 1):
            if list_to_sort[j] > list_to_sort[j + 1]:
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
    print(list_to_sort)


test = [10, 5, 2, 3, 6, 9, 20, 60, 21]
print(test)
bubble_sort(test)

