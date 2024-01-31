import numpy as np
import random
from matplotlib import pyplot as plt
from matplotlib.pyplot import cm

def coinThrow(a, b, p):
    return (a+1, b-1) if (1-p < np.random.uniform()) else (a-1, b+1)  

number_of_games = 3
p_o_s = [0.2, 0.3, 0.5, 0.8]
games = [(a) for a in range(0, number_of_games)]
probability = dict.fromkeys(p_o_s)
trajectories = dict.fromkeys(games)

for p in p_o_s:
    probability[p] = []
    for i in games:
      trajectories[i] = []
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
        trajectories[i].append((number_of_throws, win_games))
      probability[p].append(trajectories[i])

colors_dict = {0 : 'r', 1 : 'g', 2 : 'b'}

figure, axis = plt.subplots(4,1)

pr_list = sorted(probability.items())
X, Y = zip(*pr_list)
for i in range(len(p_o_s)):
  iter = 0
  for x in Y[i]:
    a, b = zip(*x)
    c = str(colors_dict[iter])
    axis[i].plot(a, b, color=c)
    axis[i].set(xlabel="Number of thorws", ylabel="Wins of A")
    axis[i].title.set_text('p = {}'.format(p_o_s[i]))
    iter+=1

plt.tight_layout()
plt.show()
