def compose(f, g):
    return lambda a: f(g(a))

def simpleComposition(f, g, x):
    return compose(eval(f), eval(g))(x)
