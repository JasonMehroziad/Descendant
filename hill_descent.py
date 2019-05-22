try:
    from malmo import MalmoPython
except:
    import MalmoPython
import os
import sys
import time
import json
import random
import numpy as np
import math
import scipy.stats
# import matplotlib.pyplot as plt
from dqn_agent import DQNAgent

grid_length, grid_width = 3, 3
grid_height = 25
directions = ['movenorth 1', 'moveeast 1', 'movesouth 1', 'movewest 1']

state_size = 9
action_size = 4
learning_rate = 0.001
discount_rate = 0.95
epsilon = 1.0
epsilon_decay = 0.995
epsilon_min = 0.01
episodes = 10000

def generate_hill_with_valleys(size, freq, oct, exp):
	pass

def generate_hill(size, scale):
	x, y = np.mgrid[0:size:1, 0:size:1]
	pos = np.empty(x.shape + (2,))
	pos[:,:,0] = x
	pos[:,:,1] = y
	rv = scipy.stats.multivariate_normal([size // 2, size // 2], cov = [[size * scale, 0], [0, size * scale]])
	# plt.contour(x, y, rv.pdf(pos))
	# plt.show()
	scale = size / max([max(row) for row in rv.pdf(pos)])
	return [int(scale * e) for row in rv.pdf(pos) for e in row]

def generate_spiral(height):
	grid_size = int(math.ceil(math.sqrt(height)))
	grid = [[0 for i in range(grid_size)] for i in range(grid_size)]
	adjustment = 1 if grid_size % 2 == 0 else 0
	center = ((grid_size // 2 - adjustment), (grid_size // 2 - adjustment))
	current_position = center
	for h in range(height, 0, -1):
		x, y = current_position
		grid[x][y] = h
		possible = []
		if x > 0 and grid[x - 1][y] == 0:
			possible.append((x - 1, y))
		if y > 0 and grid[x][y - 1] == 0:
			possible.append((x, y - 1))
		if x < grid_size - 1 and grid[x + 1][y] == 0:
			possible.append((x + 1, y))
		if y < grid_size - 1 and grid[x][y + 1] == 0:
			possible.append((x, y + 1))
		if len(possible) == 0:
			break
		current_position = sorted(possible, key = lambda x: math.hypot(center[0] - x[0], center[1] - x[1]))[0]
	return [i for row in grid for i in row]

def xml_hill(size):
    xml = ""
    index = 1000 * size
    # height_input = generate_hill(size, 4)
    height_input = generate_spiral(size * size)
    print(height_input)
    for height in height_input:
        if height < 0:
            xml += '<DrawCuboid x1="' + str(index % size) + \
                   '" y1="200" z1="'+ str(int(index / size)) + \
                   '" x2="' + str(index % size)  + '" y2="-40" z2="' + \
                   str(int(index / size))+ '" type="air" />'
        else:
            xml += '<DrawCuboid x1="' + str(index % size) + \
                   '" y1="' + str(height + 1) +'" z1="'+ str(int(index / size)) + \
                   '" x2="' + str(index % size)  + '" y2="0" z2="' + \
                   str(int(index / size))+ '" type="grass" />'
        index += 1
    return xml

def get_current_block(data):
	return data['feet'][0]

def get_state(data):
	results = [-grid_height] * (grid_length * grid_width)
	for i in range(len(data['sight']))[::-1]:
		if results[i % (grid_length * grid_width)] == -grid_height and data['sight'][i] == 'grass':
			results[i % (grid_length * grid_width)] = i // (grid_length * grid_width) - grid_height
	return results # face negative-z/north direction

def wait_world_state(agent_host):
	world_state = agent_host.peekWorldState()
	obvsText = world_state.observations[-1].text
	data = json.loads(obvsText)
	while world_state.is_mission_running and get_current_block(data) == 'air':
		time.sleep(0.1)
		world_state = agent_host.peekWorldState()
		if len(world_state.observations) == 0:
			break
		data = json.loads(world_state.observations[-1].text)
	time.sleep(0.1)
	return agent_host.getWorldState()

def main():
	my_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
	<Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	  <About>
	    <Summary>Hill Descent.</Summary>
	  </About>
	  <ServerSection>
	    <ServerInitialConditions>
	        <Time><StartTime>1</StartTime></Time>
	    </ServerInitialConditions>
	    <ServerHandlers>
	      <FlatWorldGenerator generatorString="3;1*minecraft:cobblestone;2"/>
	      <DrawingDecorator>{}</DrawingDecorator>
	      <ServerQuitFromTimeUp timeLimitMs="100000"/>
	      <ServerQuitWhenAnyAgentFinishes/>
	    </ServerHandlers>
	  </ServerSection>
	  <AgentSection mode="Survival">
	    <Name>Bob</Name>
	    <AgentStart>
	      <Placement x="2.5" y="27" z="1002.5" pitch="30" yaw="0"/>
	    </AgentStart>
	    <AgentHandlers>
	      <DiscreteMovementCommands/>
	      <ObservationFromFullStats/>
	      <ObservationFromGrid>
	          <Grid name="sight">
	              <min x="{}" y="{}" z="{}"/>
	              <max x="{}" y="{}" z="{}"/>
	          </Grid>
	          <Grid name="feet">
	              <min x="0" y="-1" z="0"/>
	              <max x="0" y="-1" z="0"/>
	          </Grid>
    	  </ObservationsationFromGrid>
	      <RewardForTouchingBlockType>
	        <Block reward="-100.0" type="lava" behaviour="onceOnly"/>
	        <Block reward="100.0" type="lapis_block" behaviour="onceOnly"/>
	      </RewardForTouchingBlockType>
	      <RewardForSendingCommand reward="-1" />
	      <AgentQuitFromTouchingBlockType>
	          <Block type="cobblestone" />
	      </AgentQuitFromTouchingBlockType>
	    </AgentHandlers>
	  </AgentSection>
	</Mission>
	'''.format(xml_hill(5), -(grid_length - 1) // 2, -grid_height, -(grid_width - 1) // 2,
		(grid_length - 1) // 2, grid_height, (grid_width - 1) // 2)

	agent = DQNAgent(state_size, action_size, learning_rate, discount_rate, epsilon, epsilon_min, epsilon_decay)

	my_client_pool = MalmoPython.ClientPool()
	my_client_pool.add(MalmoPython.ClientInfo("127.0.0.1", 10001))
	agent_host = MalmoPython.AgentHost()

	for e in range(episodes):
		my_mission = MalmoPython.MissionSpec(my_xml, True)

		my_mission_record = MalmoPython.MissionRecordSpec()
		
		my_mission.requestVideo(800, 500)
		my_mission.setViewpoint(1)
		print("Waiting for the mission to start", end=' ')
		agent_host.startMission(  my_mission, my_mission_record, )
		world_state = agent_host.getWorldState()
		while not world_state.has_mission_begun:
		    print(".", end="")
		    time.sleep(0.1)
		    world_state = agent_host.getWorldState()
		    for error in world_state.errors:
		        print("Error:",error.text)
		print()
		done = False
		batch_size = 32
		while world_state.is_mission_running:
			world_state = agent_host.getWorldState()
			if world_state.number_of_observations_since_last_state > 0:
				obvsText = world_state.observations[-1].text
				data = json.loads(obvsText)
				state = get_state(data)
				prev_y = data.get(u'YPos', 0)
				prev_damage = data['DamageTaken']
				action = agent.act(state)
				agent_host.sendCommand(directions[action])
				time.sleep(0.2)
				world_state = wait_world_state(agent_host)
				obvsText = world_state.observations[-1].text
				data = json.loads(obvsText)
				current_y = data.get(u'YPos', 0)
				current_damage = data['DamageTaken']
				next_state = get_state(data)
				reward = (prev_y - current_y) - 20 * (prev_damage - current_damage)
				done = True if get_current_block(data) == 'cobblestone' or not world_state.is_mission_running else False
				agent.remember(state, action, reward, next_state, done)
				print('episode {}/{}, action: {}, reward: {}, e: {:.2}, done: {}'.format(e, episodes, directions[action], reward, agent.epsilon, done))

				if len(agent.memory) > batch_size:
					agent.replay(batch_size)
		time.sleep(1)

if __name__ == '__main__':
	main()