def sortCodefighters(codefighters):
    res = [CodeFighter(*codefighter) for codefighter in codefighters]
    res.sort(reverse=True)
    return list(map(str, res))

class CodeFighter:
    def __init__(self, name, _id, score):
        self.name = name
        self.id = int(_id)
        self.score = int(score)
    
    def __str__(self):
        return self.name
    
    def __lt__(self, o):
        return (self.score, o.id) < (o.score, self.id)
