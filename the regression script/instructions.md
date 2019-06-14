## makeup tutorial ft. James Charles

Now that I have your attention, chances are you don't know how to use this kind of script. That's gonna change...I hope

**You need to have Python 3 installed locally in your machine**

Once you have your api key from [FRED](https://research.stlouisfed.org/docs/api/api_key.html) complete the following code in the script such that you replace ... with the api key and # with one plus the previous user's value for x:

```
elif user == 'name':
    fred = Fred(api_key='...')
    x = #
```

Before you can run the script, you have to install the required packages. To do this without royally fucking up, input the following commands in cmd:

```
pip install scipy==1.2.1
pip install pandas
pip install numpy
pip install statsmodels
pip install matplotlib
pip install fredapi
```

*Side note: we need to downgrade scipy to version 1.2.1 because statsmodels is not updated to comply with scipy's newly defined factorials (unless you get it straight from the git repository)*

Now in order to run the damn thing, punch in the file path into cmd and hit enter. If that doesn't work then you're :POOP: out of luck @noah_deitrick
