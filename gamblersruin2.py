import numpy as np
from matplotlib import pyplot as plt

def analytic_formula(a, b, p):
    z = a + b
    if (p == 1/2):
        return b/z
    q = 1-p
    return (1-(p/q)**b) / (1-(p/q)**z)

def coinThrow(a, b, p):
    return (a+1, b-1) if (1-p < np.random.uniform()) else (a-1, b+1)

def game(a, b, p):
    while (a > 0 and b > 0):
        a, b = coinThrow(a, b, p)
    return (a, b)

number_of_games = 200
probability_of_success = 0.5
coinConfigurations = [(a, 100-a) for a in range(1, 100)]
coins = [(a) for a in range(1, 100)]
probabilityOfFailure = dict.fromkeys(coins)

for a, b in coinConfigurations:
  lost_games = 0
  for _ in range(number_of_games):
     a_temp, b_temp = game(a, b, probability_of_success)
     if (a_temp == 0):
          lost_games += 1
  probabilityOfFailure[a] = lost_games/number_of_games

figure, axis = plt.subplots(1, 2)

pr_list = sorted(probabilityOfFailure.items())
x, y = zip(*pr_list)

axis[0].plot(x, y, color='r')
axis[0].set(xlabel="Number of coins", ylabel="Probability of ruin of gambler A")
axis[0].set_title("Numeric solution")

analytic_arr = np.zeros(len(coins))
index = 0
for a in coins:
  analytic_arr[index] = analytic_formula(a, 100-a, probability_of_success)
  index = index + 1
axis[1].plot(coins, analytic_arr, color='g')
axis[1].set(xlabel="Number of coins", ylabel="Probability of ruin of gambler A")
axis[1].set_title("Analytic solution")

plt.tight_layout()
plt.show()
