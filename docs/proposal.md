---
layout: default
title: Proposal
---

## Summary
Our project will be a downhill navigation AI for Minecraft. Our scenario will begin with the agent at the top of a tall structure. The goal will be to navigate down the structure to the bottom successfully, with taking minimal fall damage. The agent will be trained on a variety of structures, and develop a policy to best navigate down any descent. 

## AI/ML Algorithms
Deep Q-learning and navigation with some perception, the agent will begin by taking random actions then eventually learn a effective policy to follow. Over time the chance of it taking a random action will decrease and eventually it will follow this policy. Taking fall damage will constitute a minor failure, dying will be considered a major failure, and progressing farther than previous records will be considered a success. The agent will be able to view some of the blocks around it, and follow a learnt policy to sucessfully navigate any environment.

## Evaluation Plan
A successful project will be able to safely climb down the entire sturcture taking minimum damage. The metrics for success will be, in order of priority: Survival, then taking minimal fall damage. We will visualize the algorithm with a grid based map of the structure with a gradient representation of depth, and the AIs progress down it. If time permits, we would like to train the agent to find the fastest route down the structure while taking minimal damage, and possibly add additional obstacles to the structures, such slight ascents requiring upward movement

## Appointment
Our appointment is on Friday, April 26 at 10:30 am.
