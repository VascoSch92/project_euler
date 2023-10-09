from utils.functions import pentagonal_number


class Problem76:
    TITLE = 'Counting Summations'
    DESCRIPTION = 'https://projecteuler.net/problem=76'

    def compute_partitions(self, goal):
        partitions = [1]
        for n in range(1, goal + 1):
            partition_value = 0
            for k in range(1, n + 1):
                coefficient = (-1) ** (k + 1)
                for t in [pentagonal_number(k), pentagonal_number(-k)]:
                    if (n - t) >= 0:
                        partition_value += coefficient * partitions[n - t]
            partitions.append(partition_value)
        return partitions

    def answer(self) -> int:
        partition_sequence = self.compute_partitions(goal=100)
        return partition_sequence[-1] - 1
