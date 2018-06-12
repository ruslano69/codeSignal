class Prizes(object):
    def __init__(self, purchases, n, d):
        self.purchases = purchases
        self.n = n
        self.d = d
        self.cnt = n - 1
        
    def __iter__(self):
        return self
        
    def __next__(self):
        while self.cnt < len(self.purchases):
            self.cnt += self.n
            if self.purchases[self.cnt -self.n] % self.d == 0:
                return self.cnt - self.n + 1
        else:
            raise StopIteration

def superPrize(purchases, n, d):
    return list(Prizes(purchases, n, d))

