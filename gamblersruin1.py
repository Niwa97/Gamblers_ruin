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
starting_capital_a = starting_capital_b = 50
p_o_s = [0.1, 0.45, 0.5, 0.55, 0.9]
probability = dict.fromkeys(p_o_s)

for p in p_o_s:
    probability[p] = []
    lost_games = 0
    for i in range(number_of_games):
      a, b = game(starting_capital_a, starting_capital_b, p)
      if (a == 0):
        lost_games += 1
    probability[p].append(lost_games/number_of_games)

figure, axis = plt.subplots(1, 2)

pr_list = sorted(probability.items())
x, y = zip(*pr_list)

axis[0].plot(x, y, color='r')
axis[0].set(xlabel="Probability of single success", ylabel="Probability of ruin of gambler A")
axis[0].set_title("Numeric solution")

analytic_arr = np.zeros(len(p_o_s))
index = 0
for p in p_o_s:
  analytic_arr[index] = analytic_formula(starting_capital_a, starting_capital_b, p)
  index = index + 1
axis[1].plot(p_o_s, analytic_arr, color='g')
axis[1].set(xlabel="Probability of single success", ylabel="Probability of ruin of gambler A")
axis[1].set_title("Analytic solution")

plt.tight_layout()
plt.show()
