from collections import namedtuple

def get_puzzle(day, part=1):
    path = f"in/{day:02}_{part}.txt"
    with open(path, "r") as f:
        out = f.read().strip()
        
    return out

class P(namedtuple('P', ('x', 'y'))):
    def __add__(self, o):
        return P(self.x + o[0], self.y+o[1])
    def __sub__(self, o):
        return P(self.x - o[0], self.y-o[1])
    def __mul__(self, o):
        return P(self.x * o, self.y * o)
    def __truediv__(self, o):
        return P(self.x / o, self.y / o)
    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5