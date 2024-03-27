class Problem40:
    TITLE = "Champernowne s constant"
    DESCRIPTION = "https://projecteuler.net/problem=40"

    def answer(self):
        d = self.get_champernowne_constant(number=500_000)

        return (
            int(d[1])
            * int(d[10])
            * int(d[100])
            * int(d[1_000])
            * int(d[10_000])
            * int(d[100_000])
            * int(d[1_000_000])
        )

    @staticmethod
    def get_champernowne_constant(number: int) -> str:
        return "".join([str(num) for num in range(number)])
