def bubble(alist):
    times = 0
    for num in range(len(alist) - 1, 0, -1):
        print('num', num)
        for i in range(num):
            print('i', i)
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
            times += 1
        print('times = %d' % times)


def select(alist):
    times = 0
    for index in range(len(alist) - 1, 0, -1):
        pos = 0
        for i in range(1, index + 1):
            times += 1
            if alist[i] > alist[pos]:
                pos = i
        alist[pos], alist[index] = alist[index], alist[pos]
    print('times = %d' % times)


def insert(alist):
    times = 0
    for index in range(1, len(alist)):
        tmp = alist[index]
        pos = index
        while pos > 0 and alist[pos - 1] > tmp:
            times += 1
            alist[pos] = alist[pos - 1]
            pos -= 1
        alist[pos] = tmp
        # while pos > 0:
        # 	times += 1
        # 	if alist[pos-1] > tmp:
        # 		alist[pos] = alist[pos-1]
        # 	else:
        # 		alist[pos] = tmp
        # 		break
        # pos -= 1

    print('times = %d' % times)


def quick(alist, first, last):
    if first < last:
        pos = findpos(alist, first, last)
        quick(alist, first, pos - 1)
        quick(alist, pos + 1, last)


def findpos(slist, low, high):
    tmp = slist[low]
    while low < high:
        while low < high and slist[high] >= tmp:
            high -= 1
        slist[low] = slist[high]
        while low < high and slist[low] <= tmp:
            low += 1
        slist[high] = slist[low]
    slist[low] = tmp
    return low


alist = [3, 5, 98, 6, 1, 4, 5, 7, 44]
blist = [1, 2, 3, 4, 5]
# bubble(alist)
# select(alist)
quick(alist, 0, len(alist) - 1)
print(alist)


lis = [5, 4, 7, 9, 3, 1, 0, 8, 2, 3]


def fastSort(lis):
    if len(lis) == 1 or len(lis) == 0:
        return lis
    tmp = lis[0]
    left = 0
    right = len(lis) - 1
    while left < right:
        while tmp < lis[right] and left < right:
            right -= 1
        lis[left] = lis[right]
        while tmp >= lis[left] and left < right:
            left += 1
        lis[right] = lis[left]
    lis[left] = tmp
    res = fastSort(lis[:left]) + [lis[left], ] + fastSort(lis[left + 1:])
    return res

res = fastSort(lis)
print(res)


def shellSort(lis):
    gap = len(lis) / 2
    while gap > 0:
        for index in range(gap):
        	# insertSort(lis, index, gap)
            for i in range(index + gap, len(lis), gap):
                tmp = lis[i]
                pos = i
                while pos >= gap and lis[pos - gap] > tmp:
                    lis[pos] = lis[pos - gap]
                    pos -= gap
                lis[pos] = tmp
        gap /= 2


def insertSort(lis, index, gap):
    for i in range(index + gap, len(lis), gap):
        tmp = lis[i]
        pos = i
        while pos >= gap and lis[pos - gap] > tmp:
            lis[pos] = lis[pos - gap]
            pos -= gap
        lis[pos] = tmp

shellSort(lis)
print(lis)
