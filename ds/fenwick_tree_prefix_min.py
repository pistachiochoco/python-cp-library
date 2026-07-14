class FenwickMin:
    def __init__(self, n):
        self.n = n
        self.bit = [float("inf")] * (n + 1)

    def update(self, i, x):
        i += 1

        while i <= self.n:
            self.bit[i] = min(self.bit[i], x)
            i += i & -i

    def prefix_min(self, r):
        """
        Returns the minimum value in the half-open interval [0, r).
        """
        result = float("inf")

        while r > 0:
            result = min(result, self.bit[r])
            r -= r & -r

        return result


if __name__ == "__main__":
    a = [5, 2, 7, 4]

    fw = FenwickMin(len(a))

    for i, x in enumerate(a):
        fw.update(i, x)

    print(fw.prefix_min(3))  # min(a[0:3]) = min(5, 2, 7) = 2
    print(fw.prefix_min(4))  # min(a[0:4]) = 2
