class Problem5:
    TITLE = 'Smallest multiple'
    DESCRIPTION = "2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any "\
                  "remainder. \n What is the smallest positive number that is evenly divisible by all of the "\
                  "numbers from 1 to 20?"

    def answer(self):
        return 1*(2**4)*(3**2)*5*7*11*13*17*19
