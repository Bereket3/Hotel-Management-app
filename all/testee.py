def sorter(*a):
    sorted_arrey = []
    for j in range(len(a) - 1):
        if a[j] > a[j + 1]:
            sorted_arrey.append(a[j])
    return sorted_arrey


print(sorter(1, 3, 5, 6, 9, 10, -20))