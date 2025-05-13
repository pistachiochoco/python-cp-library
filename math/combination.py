"""
combination.py

Compute nCk(combination), nPk(permutation) module a prime 'mod' using precomputed factorials and inverse factorials.
"""

MOD = 998244353

class Combination:
    """
    Usage:
        comb_mod = Combination(n)
        res_comb = comb_mod.nCk(n, k)
        res_perm = comb_mod.nPk(n, k)
    """
    def __init__(self, n, mod=MOD):
        self.n = n
        self.mod = mod
        self.fact = [1] * (1 + n)
        self.fact_inv = [1] * (1 + n)

        for i in range(1, n + 1):
            self.fact[i] = self.fact[i - 1] * i % mod

        self.fact_inv[n] = pow(self.fact[n], mod - 2, mod)
        for i in range(n - 1, -1, -1):
            self.fact_inv[i] = self.fact_inv[i+1] * (i + 1) % mod
    
    def nCk(self, n, k):
        if k < 0 or k > n or n > self.n:
            return 0
        return self.fact[n] * self.fact_inv[n - k] % self.mod * self.fact_inv[k] % self.mod

    def nPk(self, n, k):
        if k < 0 or k > n or n > self.n:
            return 0
        return self.fact[n] * self.fact_inv[n - k] % self.mod