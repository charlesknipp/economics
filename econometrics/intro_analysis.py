import statsmodels.formula.api as smf
import pandas as pd


demo = {
    'a': ['a1','a1','a2','a2','a1','a1','a2','a2'],
    'b': ['b1','b2','b1','b2','b1','b2','b1','b2'],
    'x1': [1.764,0.400,0.978,2.240,1.867,-0.977,0.950,-0.151],
    'x2': [-0.103,0.410,0.144,1.454,0.761,0.121,0.443,0.333],
    'y': [1.494,-0.205,0.313,-0.854,-2.552,0.653,0.864,-0.742]
}

df = pd.DataFrame.from_dict(demo)
frmla = 'y ~ x1 + a:b - 1'

# OLS is the most flexible model accepting most dependent variable types
ols_model = smf.ols(
    formula = frmla,
    data = df
).fit()
print(ols_model.summary())


df = df.replace(['a1','a2'], [1,0])
frmla = 'a ~ x1 + b'

# probit requires a binary dependent hence we make a = {'a1':0, 'a2':1}
probit_model = smf.probit(
    formula = frmla,
    data = df
).fit()
print(probit_model.summary())

# logit models are less of a pain, but still require binary dependence
logit_model = smf.logit(
    formula = frmla,
    data = df
).fit()
print(logit_model.summary())