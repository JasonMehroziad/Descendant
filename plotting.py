import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import scipy.interpolate as ip

# todo (discuss with group):
#
#   - reward per episode (messy, dashed line for optimum)
#   - average reward per episode (messy)
#   - moves per episode (dashed line for optimum)
#   - error for reward (messy)
#   - error for moves
#   - successes over time (determine what a success is: no damage taken or positive reward)
#
#   - maybe epsilon over time?
#   - maybe benchmark graphs with random agent?
#
# todo (test):
#
#   - test jumping
#   - test csv writing/data collection
#   - test plotting

def plot_from_file(fname):
    data = pd.read_csv(fname, sep=',')

    # reward per episode
    optimum_reward = 0
    plt.plot(data['episode'].values, data['reward'].values, 
        marker_style = 'None', line_style = '-', color = 'b')
    plt.axhline(y = optimum_reward, color = 'r', line_style = '--')
    plt.xlabel('episode')
    plt.ylabel('reward')
    plt.title('Reward Per Episode')
    plt.savefig('./plots/reward_per_episode.png', dpi = 500)
    plt.close()

    # average reward per episode
    plt.plot(data['episode'].values, np.divide(data['reward'].values, data['moves'].values), 
        marker_style = 'None', line_style = '-', color = 'b')
    plt.xlabel('episode')
    plt.ylabel('average reward')
    plt.title('Average Reward Per Episode')
    plt.savefig('./plots/average_reward_per_episode.png', dpi = 500)
    plt.close()

    # moves per episode
    optimum_moves = 0
    plt.plot(data['episode'].values, data['moves'].values, 
        marker_style = 'None', line_style = '-', color = 'b')
    plt.axhline(y = optimum_moves, color = 'r', line_style = '--')
    plt.xlabel('episode')
    plt.ylabel('moves')
    plt.title('Number of Moves Per Episode')
    plt.savefig('./plots/moves_per_episode.png', dpi = 500)
    plt.close()

    # success over time
    plt.plot(data['episode'].values, np.cumsum(data['success'].values), 
        marker_style = 'None', line_style = '-', color = 'b')
    plt.xlabel('episode')
    plt.ylabel('cumulative successes')
    plt.title('Cumulative Successes over Time')
    plt.savefig('./plots/cumulative_successes.png', dpi = 500)
    plt.close()

if __name__ == '__main__':
	plot_from_file('./data/results.csv')

