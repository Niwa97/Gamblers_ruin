import numpy as np
from matplotlib import pyplot as plt

def coinThrow(a, b, p):
    return (a+1, b-1) if (1-p < np.random.uniform()) else (a-1, b+1)

p_o_s = [0.2, 0.3, 0.5, 0.8]
probability = dict.fromkeys(p_o_s)

for p in p_o_s:
    probability[p] = []
    win_games = 0
    number_of_throws = 0;
    a_curr = a_prev = 10
    b_curr = b_prev = 10
    while(a_curr > 0 and b_curr > 0):
      a_curr, b_curr = coinThrow(a_curr, b_curr, p)
      number_of_throws += 1
      if(a_curr > a_prev):
        win_games += 1
      a_prev, b_prev = a_curr, b_curr
      probability[p].append((number_of_throws, win_games))

figure, axis = plt.subplots(4,1)

pr_list = sorted(probability.items())
X, Y = zip(*pr_list)
for i in range(len(p_o_s)):
  x, y = zip(*Y[i])
  axis[i].plot(x, y, color='b')
  axis[i].set(xlabel="Number of thorws", ylabel="Wins of A")

plt.tight_layout()
plt.show()
