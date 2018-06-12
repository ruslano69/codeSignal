def groupDating(male, female):
    return [[m for f,m in zip(female,male) if m!=f],[f for m,f in zip(male,female) if m!=f]]
