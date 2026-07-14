class FenwickXor:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, x):
        i += 1

        while i <= self.n:
            self.bit[i] ^= x
            i += i & -i

    def prefix_xor(self, r):
        result = 0

        while r > 0:
            result ^= self.bit[r]
            r -= r & -r

        return result

    def range_xor(self, l, r):
        return self.prefix_xor(r) ^ self.prefix_xor(l)


if __name__ == "__main__":
    a = [3, 1, 4, 1, 5]

    fw = FenwickXor(len(a))

    for i, x in enumerate(a):
        fw.add(i, x)

    print(fw.prefix_xor(3))
    # a[0:3] = 3 ^ 1 ^ 4

    print(fw.range_xor(1, 4))
    # a[1:4] = 1 ^ 4 ^ 1
