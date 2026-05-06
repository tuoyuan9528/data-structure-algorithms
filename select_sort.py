# alist = [54, 226, 93, 17, 77, 31, 44, 55, 20]
# alist = [17, 226, 93, 54, 77, 31, 44, 55, 20]
# alist = [17, 20, 93, 54, 77, 31, 44, 55, 226]

# min = 0
# min = 3
# alist[0], alist[3] = alist[3], alist[0]
# min = 8
# alist[1], alist[8] = alist[8], alist[1]
# min = 5
# alist[2], alist[5] = alist[5], alist[2]

def select_sort(alist):
    n = len(alist)
    for j in range(0, n - 1):
        min_index = j
        for i in range(j + 1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]


if __name__ == "__main__":
    li = [54, 226, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    select_sort(li)
    print(li)
