"""finding mode"""


def mode_finder(lst):
    y = {}
    for a in lst:
        if not a in y:
            y[a] = 1
        else:
            y[a] += 1
    return [g for g,l in y.items() if l==max(y.values())]

print(mode_finder([22, 23, 24, 22, 21, 25, 22, 23]))
