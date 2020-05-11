import re

obs = {
    'x': [0,1,2,3],
    'y': [9,3,19,17]
}

def parse(model,data):
    '''
    Parses regression equations into a matrix.
    
    To add a constant terms, use '+1'; to add exponents, use 'x^3'; for 
    multiplication, use '4*x'.
    '''

    m = model.replace(' ','')
    m = m.split('~')
    M = []

    for k,v in data.items():
        if k == m[0]:
            dep = v
        elif k in m[1]:
            ind = v
            key = k

    try:
        add = re.split(r'\+',m[1])
    except TypeError:
        add = m[1]

    if re.search(r'(\+1$)|(^1\+)',m[1]) != None:
        M.append([1 for i in ind])
        m[1] = re.sub(r'(\+1$)|(^1\+)','',m[1])
        
    mlt = []
    pwr = []

    for trm in add:
        try:
            mlt.append(int(re.search(r'(\d)(\*)',trm).group(1)))
        except AttributeError:
            pass

        try:
            pwr.append(int(re.search(r'(\^)(\d)',trm).group(2)))
        except AttributeError:
            pass

        if trm == key:
            M.append([i for i in ind])

    if mlt:
        for i in mlt:
            M.append([i*j for j in ind])
    
    if pwr:
        for i in pwr:
            M.append([j**i for j in ind])

        
    y = [[i] for i in dep]
    M = [*map(list,[*zip(*M)])]

    return M,y


x = parse('y ~ x + x^2 + 1',obs)
print(x)