import re

def parse(model):
    m = model.replace(' ','')
    m = m.split('~')
    add = re.split('\+',m[1])
    mlt = [re.split('\*',a) for a in add]

    # p = [[re.split('\**',j) for j in re.split('\*',i)] for i in f]
    return mlt


x = parse('y ~ x**2 + 4*x')
print(x)