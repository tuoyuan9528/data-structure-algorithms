def bubble_sort(alist):
     n = len(alist)
     for j in range(0, n - 1):
        count = 0
        for i in range(0, n - j - 1):
                if alist[i] > alist[i + 1]:
                    alist[i], alist[i + 1] = alist[i + 1], alist[i]
                    count += 1
        if count == 0:
             return

if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("Original list:", li)
    bubble_sort(li)
    print("Sorted list:", li)