---
layout: default
title: Status
---

# Project Summary
Descent is an agent specialized in climbing down hazardous structures. We have designed it to traverse downwards towards the goal state while minimizing the amount of damage it takes. As the agent successfully completes stages, the structures it will have to descend will become larger and more complex.

Stages:
  - Stage 1 3x3 Basic Hill
  - Stage 2 5x5 Basic Hill

# Video Summary

# Approach
Descent is trained with deep Q-learning to recognize the best option for every state of its climb down. The agent is able to perceive adjacent blocks, but its decision making is reliant on the following algorithm: 
(code snippet of main algorithm)
The code above is based on this Q-learning reward function:
(screenshot of equation)
The algorithm is dependent on these factors 
(explanation of variables in code & equation)
We fit this deep Q-learning method to Descent's goal by setting the following reward and penalty values.
(Rewards and penalties)
The agent is trained on a basic structure. Once training is complete, it (should) be able to apply the policy it has learned to similar structures of any size.

# Evaluation

# Remaining Goals

# Resources Used
We used the following python libraries in implementing the deep Q-learning algorithm: 
  -keras
  -tensorflow 
  -numpy
  
The following articles were the basis of our design: 
  - https://keon.io/deep-q-learning/?fbclid=IwAR2WyQjJg7nFgQeF_p72_Bt8FSkGCc4ZhJqcRipT2cmnb6MtbYu-mA7bTT0
