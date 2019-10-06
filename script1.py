import timeit


def generator1():
    for i in range(10):
        yield i


setup = '''def fib_recurse(n, cnt=[0]):
    #cnt[0] += 1
    #print(cnt)
    if n in (1, 2):
        return 1

    return fib_recurse(n-1) + fib_recurse(n-2)'''

stmt = 'fib_recurse(10)'


def fib_cache(n, cache={1: 1, 2: 1}, cnt=[0]):
    cnt[0] += 1
    print(cnt)
    if n not in cache:
        cache[n] = fib_cache(n-1) + fib_cache(n-2)
    return cache[n]


def fib2(n):
    a, b = 1, 1
    if n in (1, 2):
        return a

    for i in range(2, n):
        a, b = b, a + b

    return b


if __name__ == '__main__':
    print(timeit.timeit(setup=setup, stmt=stmt, number=100))
    # print(fib_recurse(10))
    # print(fib_cache(10))