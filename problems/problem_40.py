class Problem40:
    TITLE = 'Champernowne s constant'
    DESCRIPTION = "An irrational decimal fraction is created by concatenating the positive integers:\n " \
                  "0.123456789101112131415161718192021... \n " \
                  "It can be seen that the 12th digit of the fractional part is 1. If d_n represents the nth \n " \
                  " digit of the fractional part, find the value of the following expression:\n" \
                  "d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000"

    def answer(self):
        d = self.get_champernowne_constant(number=500_000)

        return (
                int(d[1]) * int(d[10]) * int(d[100]) * int(d[1_000]) * int(d[10_000]) * int(d[100_000]) * int(
            d[1_000_000])
        )

    @staticmethod
    def get_champernowne_constant(number: int) -> str:
        return ''.join([str(num) for num in range(number)])
