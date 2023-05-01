class Problem63:
    TITLE = 'Powerful digit counts'
    DESCRIPTION = "The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit number,\n" \
                  " 134217728=8**9, is a ninth power. How many n-digit positive integers exist which are \n" \
                  " also an nth power?"

    def answer(self) -> int:
        count = 0

        for base in range(1, 11):
            for power in range(1, 23):
                if len(str(base ** power)) == power:
                    count += 1
        return count
