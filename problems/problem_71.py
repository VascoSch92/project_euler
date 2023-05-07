from math import gcd


class Problem71:
    TITLE = 'Ordered fractions'
    DESCRIPTION = "Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is \n" \
                  " called a reduced proper fraction. If we list the set of reduced proper fractions for d ≤ 8 in \n" \
                  " ascending order of size, we get: 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7,\n " \
                  " 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8 It can be seen that 2/5 is the fraction \n " \
                  "immediately to the left of 3/7. By listing the set of reduced proper fractions for \n " \
                  "d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately\n " \
                  " to the left of 3/7."

    def answer(self) -> int:
        for denominator in range(1_000_000, 2, -1):
            if denominator % 7 == 0:
                return 3 * (denominator // 7) - 1
