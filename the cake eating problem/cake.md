## The cake eating problem

The nature of the problem is as follows. An agent lives in periods 0, 1, ..., T, where T is a large number. The agent has preferences over the consumption of cake. In each period t the utility the agent receives from consuming c[t] units of cake is ln(c[t] + α). Utility in future periods is discounted by a factor β ∈ (0, 1). At date t = 0, the agent has a total amount x[0] > 0 cake.

In any period in which the agent starts with a total amount of x[t] units of cake and decides to consume c[t] units of cake, the agent is leaving for the next period an amount of x[t+1] units of cake, according to the equation:

```
x[t+1] = x[t] − c
```

The problem the agent faces is how much cake to consume in each period and how much cake to leave for future periods in order to maximize lifetime utility. Constraints are as follows:

```
x[t+1] = x[t] − c[t]
x[0] > 0 given
c[t] ≥ 0
x[t+1] ≥ 0
```

From now on we will set α = 0.

This is a well behaved maximization problem. In this case (α = 0), the optimal consumption are all positive. Note that necessary and sufficient condition for optimum are:

```
(1 + β)x[t+1] − βx[t] = x[t+2] ∀ t ∈ {0, 1, ..., T − 1}
x[T+1] = 0
x[t+1] = x[t] − c[t] ∀ t
```

Use the program to find optimum {c[0], x[t+1]} for the following values:

```
Set 1 = {α = 0, β = 0.95, T = 20, x[0] = 20}
Set 2 = {α = 0, β = 0.7, T = 20, x[0] = 20}
```
