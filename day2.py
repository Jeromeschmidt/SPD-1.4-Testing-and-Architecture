

def find_unique(l1):
    set1 = set()
    unique = None
    for elm in l1:
        if elm not in set1:
            unique = elm
        set1.add(elm)
    return unique

# print(find_unique([1,1,1,1,2,1,1,1,1,]))



def find_duplicate(l1):
    set1 = set()
    for elm in l1:
        if elm in set1:
            return elm
        set1.add(elm)
    return None

# print(find_duplicate([1,2,3,4,5,6,4]))


def check_equal_len(l1, l2):
    i = 0
    count = 0
    while True:
        try:
            l1[i]
        except:
            count += 1
        try:
            l2[i]
        except:
            count += 1
        if count == 1:
            return False
        if count == 2:
            return True
        i += 1
        count = 0
    return True

# print(check_equal_len([1,2,3], [4,5,6]))
# print(check_equal_len([1,2,3], [4,5,6,7]))

def find_most_common_word(l1):
    hist = dict()
    for i in range(len(l1)):
        if l1[i] in hist:
            hist[l1[i]] += 1
        else:
            hist[l1[i]] = 1
    max = (None, 0)
    for key, value in hist.items():
        if value > max[1]:
            max = (key, value)
    return max[0]

# print(find_most_common_word(["one", "two", "three", "one"]))

def find_first_last_occurance():
    pass

def two_sum(l1, t):
    set1 = set()

    for i in range(len(l1)):
        diff = t - l1[i]

        if diff in set1:
            return(diff, l1[i])

        set1.add(l1[i])

    return None

# print(two_sum([1,2,3,4,5,6], 7))
