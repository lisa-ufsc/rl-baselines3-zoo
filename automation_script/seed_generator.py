
import random


class SeedGenerator:

    def generate(self):
        return random.randrange(1, 2**32 - 1)

print([SeedGenerator().generate() for _ in range(10)])

