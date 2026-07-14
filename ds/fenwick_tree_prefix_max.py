class FenwickMax:
    def __init__(self, n):
        self.n = n
        self.bit = [float("-inf")] * (n + 1)

    def update(self, i, x):
        i += 1

        while i <= self.n:
            self.bit[i] = max(self.bit[i], x)
            i += i & -i

    def prefix_max(self, r):
        """
        Returns the maximum value in the half-open interval [0, r).
        """
        result = float("-inf")

        while r > 0:
            result = max(result, self.bit[r])
            r -= r & -r

        return result


if __name__ == "__main__":
    a = [5, 2, 7, 4]

    fw = FenwickMax(len(a))

    for i, x in enumerate(a):
        fw.update(i, x)

    print(fw.prefix_max(3))  # max(a[0:3]) = max(5, 2, 7) = 7
    print(fw.prefix_max(2))  # max(a[0:2]) = max(5, 2) = 5
