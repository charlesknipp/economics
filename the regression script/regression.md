## Regression tutorial

Now that I have your attention, chances are you don't know how to use this kind of script. That's gonna change...I hope

**You need to have Python 3 installed locally on your machine**

Once you have your api key from [FRED](https://research.stlouisfed.org/docs/api/api_key.html) you will be prompted to enter it when you run the script so have it ready in a separate document. The chain of inputs should look like this:

```
>> new script, who dis?
>> u have a FRED api key?
>> enter ur FRED api key:
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

Now in order to run the damn thing, punch in the file path into cmd and hit enter. If that doesn't work then you're :shit: out of luck @nayod78

### To do list:

- [x] Automate heteroskedasticity corrected standard errors
- [ ] Allow users to input FRED data sets in the console (and work properly)
- [ ] Call from a server of existing users and store their queries
