testlist1 = [1, 5, 7, 99]
testlist2 = [8102839012, 78956891649, 1298301830, 172390712894671894,
             179759795, 1729379817917490570]
testlist3 = [99, 7895792, 123, 2121, 7797]
testlist4 = [9, 8, 7, 6, 5, 4, 3, 2, 1]


def min(list):
    # python sort method here uses Timsort
    # timsort is an adaptive and stable mergesort variant
    # worst case o(nlogn)
    # best case o(n)
    # average case o(nlogn)
    list.sort()
    return (list[0])


def max(list):
    list.sort()
    return (list[len(list) - 1])


def kmin(list, k):
    list.sort()
    return (list[0 + k])


def kmax(list, k):
    list.sort()
    return (list[len(list) - k])


def range(list, low, high):
    rangelist = []
    for i in list:
        if (low < i) and (i < high):
            rangelist.append(i)
    return rangelist


def ceiling(list, key):
    list.sort()
    ceilinglist = []
    for i in list:
        if (i >= key):
            ceilinglist.append(i)

    if (len(ceilinglist) <= 0):
        print("No qualifying value")
    else:
        print ceilinglist[0]


def floor(list, key):
    list.sort()
    floorlist = []
    for i in list:
        if (i <= key):
            floorlist.append(i)

    if (len(floorlist) <= 0):
        print("No qualifying value")
    else:
        print max(floorlist)


if __name__ == '__main__':
    floor(testlist1, 6)
