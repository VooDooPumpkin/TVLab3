import math
# combinatoric formuls
class combinatorics():

    # factorial
    def fac(r, l=1):
        if (r == 0):
            return 1
        if (l == r):
            return l
        mid = (r + l) // 2
        return combinatorics.fac(mid, l) * combinatorics.fac(r, mid + 1)

    # combinations without repetition
    def combiNoRep(n, m):
        return combinatorics.fac(n) // (combinatorics.fac(m) * combinatorics.fac(n - m))

    # combinations with repetition
    def combiRep(n, m):
        return combinatorics.combiNoRep(n + m - 1, m)

    # accommodation without repetition
    def accomNoRep(n, m):
        return combinatorics.fac(n) // combinatorics.fac(n - m)

    # accommodation with repetition
    def accomRep(n, m):
        return n ** m

    # permutation with repetition
    def permWithRep(n, arrayM):
        res = 1
        for it in arrayM:
            res *= combinatorics.fac(int(it))
        return combinatorics.fac(n) // res

    # sum of array
    def sumArray(array):
        res = 0
        for it in array:
            res += int(it)
        return res