import statsmodels.formula.api as smf
from patsy import demo_data
import pandas as pd
import numpy as np

'''
Using the package statsmodels.formula.api, we can treat statistical analysis
like we're used to in stata and r.

Formulas require a left hand side LHS and a right hand side RHS. Below is a list
of possible formulas and some syntax to get started:

    C(a)    defines a categorical variable using a dummy treatment by default
    - 1     eliminates an intercept term (there by default)
    a:b     constructs interaction terms based on the variables used
    a ~ b   separates the LHS from the RHS

Read the patsy documentation for more information; statsmodels.formula.api is
written based on patsy and the syntax is fairly similar.
'''


demo = {
    'a': ['a1','a1','a2','a2','a1','a1','a2','a2'],
    'b': ['b1','b2','b1','b2','b1','b2','b1','b2'],
    'x1': [1.764,0.400,0.978,2.240,1.867,-0.977,0.950,-0.151],
    'x2': [-0.103,0.410,0.144,1.454,0.761,0.121,0.443,0.333],
    'y': [1.494,-0.205,0.313,-0.854,-2.552,0.653,0.864,-0.742]
}

demo = pd.DataFrame.from_dict(demo)
demo = demo.replace(['a1','a2'],[1,0])

frmla1 = 'y ~ x1 + a'
frmla2 = 'a ~ x1'

'''
The following regressions are just a few functions supported by statsmodels,
but there are some key things that need to be done in order to use them. For
example, the probit and logit models require the dependent variable to be
binary; hence why I had to change a to predict the likeliness of a1 in line
33 where I replace it with a bool.

Also use smf.___ to call the regression model as defined in the preamble
'''

ols_model = smf.ols(
    formula = frmla1,
    data = demo
).fit()

print(ols_model.summary())

probit_model = smf.probit(
    formula = frmla2,
    data = demo
).fit()

print(probit_model.summary())


logit_model = smf.logit(
    formula = frmla2,
    data = demo
).fit()

print(logit_model.summary())