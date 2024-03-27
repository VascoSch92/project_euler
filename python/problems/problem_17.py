class Problem17:
    TITLE = "Number Letter Counts"
    DESCRIPTION = "https://projecteuler.net/problem=17"

    def answer(self) -> int:
        digits = [
            "",
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
        ]
        decimal = [
            "ten",
            "eleven",
            "twelve",
            "thirteen",
            "fourteen",
            "fifteen",
            "sixteen",
            "seventeen",
            "eighteen",
            "nineteen",
        ]
        decine = [
            "twenty",
            "thirty",
            "forty",
            "fifty",
            "sixty",
            "seventy",
            "eighty",
            "ninety",
        ]

        letters_count = 0

        # From 1 to 9
        for a in digits:
            letters_count += len(a)

        # From 10 to 19
        for b in decimal:
            letters_count += len(b)

        # From 20 to 99
        for a in decine:
            for b in digits:
                letters_count += len(a + b)

        # Just x00
        for a in digits[1::]:
            letters_count += len(a + "hundred")

        # From x01 to x09
        for a in digits[1::]:
            for b in digits[1::]:
                letters_count += len(a + "hundredand" + b)

        # From x10 to x19
        for a in digits[1::]:
            for b in decimal:
                letters_count += len(a + "hundredand" + b)

        # From x20 to x99
        for d in digits[1::]:
            for a in decine:
                for b in digits:
                    letters_count += len(d + "hundredand" + a + b)

        # Add length of 1_000
        letters_count += len("onethousand")

        return letters_count
