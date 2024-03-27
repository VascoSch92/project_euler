class Problem26:
    TITLE = "Reciprocal cycles"
    DESCRIPTION = "https://projecteuler.net/problem=26"

    def answer(self) -> int:
        max_recurring_cycle_length = float("-inf")
        max_denominator = None

        for denominator in range(3, 1_000, 2):
            length_recurring_cycle = self.length_recurring_cycle(
                numerator=1, denominator=denominator
            )
            if length_recurring_cycle > max_recurring_cycle_length:
                max_recurring_cycle_length = length_recurring_cycle
                max_denominator = denominator

        return max_denominator

    def length_recurring_cycle(self, numerator: int, denominator: int) -> int:
        reminders = []
        rems = None
        while rems not in reminders:
            reminders.append(rems)
            numerator *= 10
            rems = numerator % denominator

        reminders.pop(0)
        return len(reminders)
