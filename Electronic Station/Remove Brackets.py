import itertools


def is_balanced(a):
    while True:
        if '()' in a:
            a = a.replace('()', '')
        elif '[]' in a:
            a = a.replace('[]', '')
        elif '{}' in a:
            a = a.replace('{}', '')
        else:
            return not a


def remove_brackets(a):
    for i in range(len(a)+1):
        for c in itertools.combinations(range(len(a)), i):
            s = ''.join(v for j, v in enumerate(a) if j not in c)
            if is_balanced(s):
                return s
remove_brackets("(()()((")