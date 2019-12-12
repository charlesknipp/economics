## Regression tutorial

Chances are you don't know how to use this kind of script. That's gonna change...I hope

**You need to have Python 3 installed locally on your machine**

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

Now in order to run the damn thing, punch in the file path into cmd and hit enter. If that doesn't work then you're :shit: out of luck @nayod78

Once you have your api key from [FRED](https://research.stlouisfed.org/docs/api/api_key.html) you will be prompted to enter it when you run the script so have it ready in a separate document. The chain of inputs should look like this:

```
>> new script, who dis?
>> u have a FRED api key?
>> enter ur FRED api key:
```

When you enter the desired data sets try to separate each list item with a comma and a space as to not confuse the parser. I think it should work either way, but just to be safe it should look like this:

```
>> which FRED datasets u want? GDP, SP500, CPIAUCSL, FEDFUNDS
```

The script is designed to be flexible with inputs so you shouldn't have to worry about uppercase inputs; however try to stay consistent with your inputs since this is a very basic parser.

### To do list:

- [x] Automate heteroskedasticity corrected standard errors
- [x] Allow users to input FRED data sets in the console (and work properly)
- [ ] Add more tests like stationarity and ARIMA models
- [ ] Correct for disparities in inputted FRED data (likely using ARIMA)
