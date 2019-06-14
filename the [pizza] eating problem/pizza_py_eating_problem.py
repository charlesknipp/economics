import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt


# define our parameters and specify two different values for B in order to account for both sets of parameters
B1 = (.95)
B2 = (.70)
x = []
x.append(20)
T = 20
a = 0


# define a function that calculates the proceeding pizza consumption given the initial and a guess for the first period
def adjustedx1(min1, max1, initial):
  newx1 = [initial]
  newx1.append((max1+min1)/2)
  for t in range(2, T+1):
    newx1.append((1+B1) * newx1[t-1] - B1 * newx1[t-2])
  return newx1


# define a second function that does the exact same operation with respect to the second set of parameters
def adjustedx2(min2, max2, initial):
  newx2 = [initial]
  newx2.append((max2+min2)/2)
  for t in range(2, T+1):
    newx2.append((1+B2) * newx2[t-1] - B2 * newx2[t-2])
  return newx2


# define the boundaries for initial pizza consumption
max1 = x[0]
min1 = 0

max2 = x[0]
min2 = 0


# recall the defied funcions and define them as a list for both sets which simplifies the following conditionals
x1 = adjustedx1(min1, max1, x[0])
x2 = adjustedx2(min2, max2, x[0])


# create a conditional loop such that we redefine upper and lower boundaries until we have no more pizza at the end of the final period
while True:
  if x1[T] > 0.00001:
    max1 = x1[1]
  elif x1[T] < -0.00001:
    min1 = x1[1]
  else:
    break
  x1 = adjustedx1(min1, max1, x[0])


# since our upper and lower bounds are computed with a different set of parameters, we define different boundaries for that set
while True:
  if x2[T] > 0.00001:
    max2 = x2[1]
  elif x2[T] < -0.00001:
    min2 = x2[1]
  else:
    break
  x2 = adjustedx2(min2, max2, x[0])


# this value should be close to 0 if we properly condition our statements, and it certainly is
print('the pizza left over at a rate of .95: ',abs(round(x1[T],4)))
print('the pizza left over at a rate of .70: ',abs(round(x2[T],4)))


# define some value of consumption given x[] and discount factors for both sets
c1 = []
c2 = []

for i in range(0, T):
  c1.append(x1[i] - x1[i+1] - a)
  c2.append(x2[i] - x2[i+1] - a)


# create a variable to represent the period and set it equal to the elements in x so matplotlib doesn't act up like usual
time = []
for n in range(0,T+1):
  time.append(n+1)


# plotting investment for case 1
fig1 = plt.figure(1)
plt.plot(time, x1)
plt.title('investment ('+r'$x_{t+1}$'+') over time discounted at '+r'$\beta$ '+'= .95')
plt.xlabel('time', fontsize = 16)
plt.ylabel(r'$x_{t+1}$', fontsize = 16)
# in order for it to work in repl you have to save it to your library
fig1.savefig('Investment_1.png')

# plotting investment for case 2
fig2 = plt.figure(2)
plt.plot(time, x2)
plt.title('investment ('+r'$x_{t+1}$'+') over time discounted at '+r'$\beta$ '+'= .70')
plt.xlabel('time', fontsize = 16)
plt.ylabel(r'$x_{t+1}$', fontsize = 16)
# in order for it to work in repl you have to save it to your library
fig2.savefig('Investment_2.png')


# deleting a value of time that we needed to add in order to correspond to the legnth of x[t+1]
del time[0]
# plotting consumption for case 1
fig3 = plt.figure(3)
plt.plot(time, c1)
plt.title('consumption ('+r'$\hat c_t$'+') over time discounted at '+r'$\beta$ '+'= .95')
plt.xlabel('time', fontsize = 16)
plt.ylabel(r'$\hat c_t$', fontsize = 16)
# in order for it to work in repl you have to save it to your library
fig3.savefig('Consumption_1.png')

# plotting consumption for case 2
fig4 = plt.figure(4)
plt.plot(time, c2)
plt.title('consumption ('+r'$\hat c_t$'+') over time discounted at '+r'$\beta$ '+'= .70')
plt.xlabel('time', fontsize = 16)
plt.ylabel(r'$\hat c_t$', fontsize = 16)
# in order for it to work in repl you have to save it to your library
fig4.savefig('Consumption_2.png')
# this following command forces repl to display the graphs once they are saved to your library
plt.show()
