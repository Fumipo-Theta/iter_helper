from functools import reduce


class Subset:

    def __init__(self, array, ignore_empty=True, drop=True):
        self.origin = array
        self.bit_length = len(self.origin)
        self.drop = drop
        self.max = int(reduce(lambda acc, e: acc + e,
                              map(lambda _: "1", self.origin), "0b"), 0)
        self.count = 1 if ignore_empty else 0

    def format_bit(self, num):
        return format(num, f'0{self.bit_length}b')

    def get_combination(self, mask):
        if self.drop:
            return list(map(lambda t: t[0], filter(lambda t: t[1] == "1", zip(self.origin, mask))))
        else:
            return list(map(lambda t: t[0] if t[1] == "1" else None, zip(self.origin, mask)))

    def get_origin(self):
        return self.origin

    def __iter__(self):
        return self

    def __len__(self):
        return self.max

    def __next__(self):
        if self.count > self.max:
            raise StopIteration()

        mask = self.format_bit(self.count)
        self.count += 1
        return self.get_combination(mask)
