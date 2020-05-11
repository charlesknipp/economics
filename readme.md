# Economics

A repository of all the code I use as an undergraduate economics/math student.

### The cake eating problem

`cake_eating_problem.py` spooked everyone in Dr. Prescott's class... clearly, except for me. The problem requires students to maximize aggregate utility over time by optimizing consumption; constraints include a discount rate, a time period, and a budget.

### The FRED script

`regression.py` is an ongoing project that pulls from FRED data sets and regresses the joined data frames; it automatically accounts for heteroskedasticity and if there is only one regressor, it tells you to reject. You do need an api key from [FRED](https://research.stlouisfed.org/docs/api/api_key.html) in order to run the script.

### The least squares algorithm

`ols_algorithm.py` is a basic least squares regression algorithm that uses the matrix representation of least squares. The script also includes a function parser that interprets very similarly to r style formulas; something like `y ~ x + x^2 + 1` where `+1` represents a constant term.

### The econometrics script

`intro_analysis.py` is a demo of the `statsmodels` module in Python using `patsy` to interpret r style formulation; this is just a demo to show off the formulation considering the shortcomings of `statsmodels` own documentation. 

### The rest

*"You can't derive smallest"* -[ancient chinese proverb](https://wpcarey.asu.edu/people/profile/1636136)

email: cknipp@asu.edu
