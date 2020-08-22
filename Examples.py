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

