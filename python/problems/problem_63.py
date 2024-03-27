class Problem63:
    TITLE = "Powerful digit counts"
    DESCRIPTION = "https://projecteuler.net/problem=63"

    def answer(self) -> int:
        count = 0

        for base in range(1, 11):
            for power in range(1, 23):
                if len(str(base**power)) == power:
                    count += 1
        return count
