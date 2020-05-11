import re

# OLS regression algorithm using matrix manipulation and a custom function parser

def matrixProd(X,Y):
    '''
    Calculate the product of two matrices, order matters
    '''

    return [[sum(a*b for a,b in zip(x,y)) for y in zip(*Y)] for x in X]


def parser(model):
    m = model.split('~')
    f = m[1]

    p = [[re.split('**',j) for j in re.split('*',i)] for i in re.split('+',f)]
    return p


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


def ols(X,y):
    '''
    Least squares regression algorithm using matrix manipulation
    '''

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


model = ols(
    X = [[1,1],[1,2],[1,3]],
    y = [[5],[7],[16]]
)

print(model)