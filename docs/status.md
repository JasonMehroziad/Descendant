---
layout: default
title: Status
---

# Project Summary
Descendant is an agent specialized in climbing down hazardous structures. We have designed it to traverse downwards towards the goal state while minimizing the amount of damage it takes. As the agent successfully completes stages, the structures it will have to descend will become larger and more complex. The following is a list of stages developed so far.

Stages:
  - Stage 1: 3x3 Basic Hill
  - Stage 2: 5x5 Basic Hill

# Video Summary

# Approach
Descendant is trained with deep Q-learning to recognize the best option for every state of its climb down. The agent begins by following a epsilon greedy policy, randomly choosing moves independent of success or failure. During this greedy policy period, the agent is rewarded by the following function for each move it takes: 

![image not found](https://github.com/JasonMehroziad/Descendant/blob/master/docs/images/status_reward_code.PNG)
This reward function penalizes the agent for taking damage and rewards them for the more downhill movement made without taking damage.

The reward for each episode is used to train a neural network model to develop a Markov Decision Process (MDP), which can predict the agent's reward for taking a specific action. Over time, the chance the agent takes a random action, the variable ε, decays, and the agent starts acting by taking the best rewarded action according to the MDP. The neural network is trained by the following loss function:

![image not found](https://github.com/JasonMehroziad/Descendant/blob/master/docs/images/formula.PNG)

The variables of this function are as follows:
 - r is the return of the reward function mentioned previously
 - γ is the discount factor, which tells the MDP how much to value new information it learns
 - Q is the value of the state being updated within the neural network

# Evaluation




# Remaining Goals


# Resources Used
We used the following python libraries in implementing the deep Q-learning algorithm: 
  - keras
  - tensorflow 
  - numpy
  
The following articles assisted in our design: 
  - [Deep Q-learning Reference](https://keon.io/deep-q-learning/?fbclid=IwAR2WyQjJg7nFgQeF_p72_Bt8FSkGCc4ZhJqcRipT2cmnb6MtbYu-mA7bTT0)
  - [Malmo's Documentation](http://microsoft.github.io/malmo/0.30.0/Documentation/index.html)
