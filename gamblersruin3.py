import numpy as np
from matplotlib import pyplot as plt

def coinThrow(a, b, p):
    return (a+1, b-1) if (1-p < np.random.uniform()) else (a-1, b+1)

def game(a, b, p):
    while (a > 0 and b > 0):
        a, b = coinThrow(a, b, p)
    return (a, b)

def length_of_game(a, b, p):
    number_of_throws = 0
    while (a > 0 and b > 0):
        a, b = coinThrow(a, b, p)
        number_of_throws += 1
    return number_of_throws

p_o_s = [0.2, 0.5, 0.8]
number_of_games = 1000
starting_capital_a = starting_capital_b = 50
number_of_rounds = dict.fromkeys(p_o_s)

for p in p_o_s:
  number_of_rounds[p] = [length_of_game(starting_capital_a, starting_capital_b, p) for _ in range(number_of_games)]

fig, axes = plt.subplots(len(p_o_s), 1)

for p in p_o_s:
  print("Probability of success {} ".format(p) + "Expected length of the game ", sum(number_of_rounds[p])/len(number_of_rounds[p]))

for ax, p in zip(axes, p_o_s):
    ax.set_title("Probability of sucess = {}".format(p))
    ax.hist(number_of_rounds[p], density=True, bins=50)
    ax.xaxis.set_label_text("Number of rounds")
    ax.yaxis.set_label_text("P(Number of rounds)")

plt.tight_layout()
plt.show()
