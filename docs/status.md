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

<iframe width="560" height="315" src="https://www.youtube.com/embed/grTlyizTJ4M" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# Approach
Descendant is trained with deep Q-learning to recognize the best option for every state of its climb down. The agent begins by following an epsilon greedy policy, randomly choosing moves independent of success or failure. During this greedy policy period, the agent is rewarded by the following function for each move it takes: 

<img src ="https://github.com/JasonMehroziad/Descendant/blob/master/docs/images/status_reward_code.PNG">
This reward function penalizes the agent for taking damage and rewards them for the more downhill movement made without taking damage.

The reward for each episode is used to train a neural network model to develop a Markov Decision Process (MDP), which can predict the agent's reward for taking a specific action. Over time, the chance the agent takes a random action, the variable ε, decays, and the agent starts acting by taking the best rewarded action according to the MDP. The neural network is trained by the following loss function:

<img src = "https://github.com/JasonMehroziad/Descendant/blob/master/docs/images/formula.PNG">

The variables of this function are as follows:
 - r is the return of the reward function mentioned previously
 - γ is the discount factor, which tells the MDP how much to value new information it learns
 - Q is the value of the state being updated within the neural network

# Evaluation

**Qualitatively**, Descendant is able to climb down stage 1 successfully after around 500 trials. The agent, once fully trained, can make its way to the bottom of the structure in a short amount of time without taking damage or becoming trapped. This satisfies the basic criteria for the project's success on a basic 3x3 stage. The agent also learned to take shortcuts, prioritizing moves that will bring it to the bottom faster. Due to this, the agent does not get trapped on walls or climb back up. The episodes shown in the status video show the agent's progress in throughout training and its eventual successful results. Based on the viewable evidence the agent is success for descending basic structures.

**Quantitatively**, Descendant's training to minimize damage can also be seen by its reward output. The following display Descendant's rewards for its actions, along with whether they were random or calculated by the MDP neural network. 

Initially:
<img src = "https://github.com/JasonMehroziad/Descendant/blob/master/docs/images/model_inital.png">

Descendent is starts with an epsilon greedy policy (ε = 1.0), acting completely at random. 

After 100 episodes:
<img src = "https://github.com/JasonMehroziad/Descendant/blob/master/docs/images/model_100.png">

Descendent makes mostly random decisions, but has been trained enough to make good decisions when they are calculated using its MDP. ε = 0.8 at this point.

After 500 episodes:
<img src = "https://github.com/JasonMehroziad/Descendant/blob/master/docs/images/model_500.png">

Descendent is fully trained, and can make its way down the hill safely and efficiently by taking the highest reward action predicted by its MDP. ε = 0.01, and by this point it is acting entirely on the policy built by its training. Because of the consistently good rewards received, we can consider the agent a success for descending basic structures.

# Remaining Goals

Currently the Descendent is only successful at descending small basic structures. In the coming weeks, we hope to increase the scale of the structures the agent can climb down. Eventually the agent should be able to reach the bottom of a 10x10 massive structure taking minimum damage in efficient time. It should also be noted that the initial stages (1&2), were designed with a spiraling optimal path. The final agent should be able to descend any sort of hill, not just those with spiraling paths, and will be tested accordingly. 

Another way of increasing Descendant’s skill would be to add additional hazards to the structures, such as lava, death pits, and slight inclines. Adding inclines to the structures would be the final stretch goal, as training the agent to consider moving upwards as an optimal move will require advanced updates to the agent's reward function. This ties into another stretch goal, which is to make the agent less shortsighted. This could allow the agent to also consider the optimal path down in terms of total distance in addition to damage taken, optimizing it on multiple factors in the ideal case.

# Resources Used
We used the following python libraries in implementing the deep Q-learning algorithm: 
  - keras
  - tensorflow 
  - numpy
  
The following articles assisted in our design: 
  - [Deep Q-learning Reference](https://keon.io/deep-q-learning/?fbclid=IwAR2WyQjJg7nFgQeF_p72_Bt8FSkGCc4ZhJqcRipT2cmnb6MtbYu-mA7bTT0)
  - [Malmo's Documentation](http://microsoft.github.io/malmo/0.30.0/Documentation/index.html)
