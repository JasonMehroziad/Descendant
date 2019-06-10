# Video

# Summary

# Approaches
### Proposed Approaches
In this project, we thought of many possible approaches to solve our descent problem. The first idea proposed was to just used Dijkstra's with the change in heights being the edge weights. While it would give use the optimal route to take the least amount of damage, that approach would require the knowledge of the entire environment. For our project, we wanted to keep it realistic and limit the sight of the agent to a 5x5 grid around it; regular players cannot see the entire hill at once.

The next idea proposed was to use q-learning to solve our descent problem, but we realized that it would take far too long to train. Recall that in Assignment 2, students ran such a simple problem for thousands of iterations but still did not converge. We believed that such a complicated problem with complicated structures for the agent to climb down, q-learning would not be able to finish within a reasonable amount of time.

### Our Approach
Our final idea, which we used for this project, was deep-q-learning. It uses a neural network in order approximate q-values for each possible action given a state. It is far more effective in larger environments compared to q-learning. 
The agent’s state is an array of the 5x5 grid of heights of the terrain relative to the agent’s height. The agent has 4 different move actions it could take: north, east, south, west. It could also jump in those directions if the terrain in the specific cardinal direction is only 1 block higher than the agent’s current y position but is still encompassed in those 4 actions. 

#### Reward Function
The agent’s reward function is the following:
```
If agent keeps the exact same position:
	Reward = -1000
Otherwise:
	Reward = 2 * change in y position - 50 * damage taken - 1
```
This reward function penalizes the agent for taking damage and rewards them for the more downhill movement made without taking damage. The reward for each episode is used to train a neural network model to develop a Markov Decision Process (MDP), which can predict the agent’s reward for taking a specific action. The neural network is trained by the following loss function:

<img src="images/formula.png" height="100" width="500">

The variables of this function are as follows:
  - r is the return of the reward function mentioned previously
  - γ is the discount factor, which tells the MDP how much to value new information it learns
  - Q is the value of the state being updated within the neural network
  - s is the state
  - a is the action

#### Hyperparameters
The agent had an constant learning rate of 0.1. We didn’t want the learning rate too low or the agent would take too long to train; we didn’t want the learning rate too high or performance may diverge. Also, the agent had a discount rate of 0.95 because we didn’t want our agent to be too short-sighted. Finally, the agent starts off an epsilon, which is the chance the agent takes a random action, of 1.0, but its epsilon gradually decreases multiplicatively by 0.9999. Over time, the chance the agent takes a random action decays, and the agent starts acting by taking the best rewarded action. 

# Evaluation

# References
We used the following python libraries in implementing the deep Q-learning algorithm, in addition to Malmo: 
  - keras
  - tensorflow 
  - numpy
  
The following articles assisted in our design: 
  - [Deep Q-learning Reference](https://keon.io/deep-q-learning/?fbclid=IwAR2WyQjJg7nFgQeF_p72_Bt8FSkGCc4ZhJqcRipT2cmnb6MtbYu-mA7bTT0)
  - [Malmo's Documentation](http://microsoft.github.io/malmo/0.30.0/Documentation/index.html)
