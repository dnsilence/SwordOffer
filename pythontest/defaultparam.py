def add_end(L=[]):
    L.append('END')
    return L


def add_end_change(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


if __name__ == '__main__':
    print(add_end())
    print(add_end())
    print(add_end_change())
    print(add_end_change())