m = list()
for n in range(1, 10):
    if n % 3 == 0 or n % 5 == 0:
        m.append(n)
print(sum(m))


class Summable_List(list):
    def sum(self):
        s = 0
        for v in self:
            s += v
        return s


# The sum of a sequence has a simple, recursive definition
def sumr(seq):
    if len(seq) == 0: return 0
    return seq[0] + sumr(seq[1:])


def until(n, filter_func, v):
    if v == n: return []
    if filter_func(v):
        return [v] + until(n, filter_func, v + 1)
    else:
        return until(n, filter_func, v + 1)


mult_3_5 = lambda x: x % 3 == 0 or x % 5 == 0


def next_(n, x):
    return (x + n / x) / 2


def repeat(f, a):
    yield a
    for v in repeat(f, f(a)):
        yield v

def within(ε, iterable):
 def head_tail(ε, a, iterable):
 b = next(iterable)
 if abs(a-b) <= ε: return b
 return head_tail(ε, b, iterable)
 return head_tail(ε, next(iterable), iterable)
