import re

# OLS regression algorithm using matrix manipulation and a custom function parser

def matrixProd(X,Y):
    '''
    Calculate the product of two matrices, order matters
    '''

    return [[sum(a*b for a,b in zip(x,y)) for y in zip(*Y)] for x in X]


def parse(model,data):
    '''
    Parses regression equations into a matrix.
    
    To add a constant terms, use '+1'; to add exponents, use 'x^3'; for 
    multiplication, use '4*x'.
    '''

    m = model.replace(' ','')
    m = m.split('~')
    M = []

    ind_list = []
    key = []

    for k,v in data.items():
        if k == m[0]:
            dep = v
        elif k in m[1]:
            ind_list.append(v)
            key.append(k)

    try:
        add = re.split(r'\+',m[1])
    except TypeError:
        add = m[1]

    if re.search(r'(\+1$)|(^1\+)',m[1]) != None:
        M.append([1 for i in dep])
        m[1] = re.sub(r'(\+1$)|(^1\+)','',m[1])

    for ind in range(len(ind_list)):
        pwr = []
        for trm in add:
            try:
                pwr.append(int(re.search(key[ind]+r'(\^)(\d)',trm).group(2)))
            except AttributeError:
                pass

            if trm == key:
                M.append([i for i in ind_list[ind]])
    
        if pwr:
            for i in pwr:
                M.append([j**i for j in ind_list[ind]])

        
    y = [[i] for i in dep]
    M = [*map(list,[*zip(*M)])]

    return M,y


def rref(M):
    '''
    Gauss Jordan Row Reduction of any given matrix M
    '''
    
    c = 0

    for r in range(len(M)):
        if c >= len(M[0]):
            break
        i = r

        while M[i][c] == 0:
            i += 1
            if i == len(M):
                i = r
                c += 1
                if len(M[0]) == c:
                    break

        M[i],M[r] = M[r],M[i]
        lv = M[r][c]
        M[r] = [v/float(lv) for v in M[r]]

        for i in range(len(M)):
            if i != r:
                l = M[i][c]
                M[i] = [v-l*u for u,v in zip(M[r],M[i])]

        c += 1
    
    return M


def ols(formula,data):
    '''
    Least squares regression algorithm using matrix manipulation
    '''

    X,y = parse(formula,data)

    for i in range(len(X)):
        if len(X[i]) != len(X[i-1]):
            raise IndexError('Inconsistent row length in X')
        else:
            continue
    
    if len(X) != len(y):
        raise IndexError('Expected %d arguments in y, received %d' % (len(X),len(y)))

    else:
        Xt = [list(i) for i in zip(*X)]
        XtX = matrixProd(Xt,X)
        Xty = matrixProd(Xt,y)

        for i in range(len(XtX)): XtX[i].extend(Xty[i])
        S = rref(XtX)
        B = [m[-1] for m in S]
        return B


obs = {
    'x': [0,1,2,3],
    'y': [9,3,19,17]
}

model = ols(
    formula = 'y ~ x + x^2 + 1',
    data = obs
)

print(model)