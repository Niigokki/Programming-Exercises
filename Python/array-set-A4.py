testlist = [x**2 for x in range(10)]


def add(element):
    #   checks if set/list contains element
    #   ensures that it's not a dupe or a null
    #   check if array is full and resize if so
    #   keep in ascending natural order
    if element not in testlist and element is None:
        print "element is null"
        return False
    elif element in testlist and element is not None:
        print "element already present in set"
        return False
    elif element not in testlist and element is not None:
        testlist.append(element)
        testlist.sort()
        print("element added, new set is")
        print(testlist)
        return True


def remove(element):
    try:
        testlist.remove(element)
    except ValueError:
        print("element not in set")


def contains(element):
    try:
        testlist.index(element)
        return True
    except ValueError:
        print("element not in set")
        return False


def size():
    return len(testlist)


def isEmpty():
    if size() > 0:
        print("list isn't empty")
        return False
    else:
        print("list is empty")
        return True


def equals(list):
    # enumerate is very handy - adds index value to our iteration
    for i, element in enumerate(list):
        testval1 = testlist.count(element)
        testval2 = list.count(element)
        if testval1 != testval2:
            print("sets are not equal")
            return False
    print("sets are equivelent")
    return True


def union(list):
    list += testlist
    list.sort()
    print list
    return True


def intersection(list):
    list.sort()
    testlist.sort()
    intersectionlist = []
    for element in list:
        if element in testlist:
            intersectionlist.append(element)
    print intersectionlist
    return True


def complement(list):
    list.sort()
    testlist.sort()
    complementlist = []
    for element in list:
        if element not in testlist:
            complementlist.append(element)
    complementlist.sort()
    print complementlist
    return True


if __name__ == '__main__':
    print testlist
    isEmpty()
    blankList = [x**2 for x in range(10)]
    blankList.reverse()
    print blankList
    intersection(blankList)
    complement(blankList)
