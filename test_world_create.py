try:
    from malmo import MalmoPython
except:
    import MalmoPython

import os
import sys
import time
import json
from math import inf
from priority_dict import priorityDictionary as PQ
heights = [30, 24, 16, 14, 14, 12, 28, 4, -1, 15, 13, 10, 26, 23, 21, 18, -1, \
           8, 25, 20, 14, 11, 10, 6, 21, 17, 11, 8, 5, 5, 18, 16, 10, 4, 2, 0]
           
def xml_hill(height_input):
    xml = ""
    index = 6000
    for height in height_input:
        if height < 0:
            xml += '<DrawCuboid x1="' + str(index % 6) + \
                   '" y1="200" z1="'+ str(int(index / 6)) + \
                   '" x2="' + str(index % 6)  + '" y2="-40" z2="' + \
                   str(int(index / 6))+ '" type="air" />'
        else:
            xml += '<DrawCuboid x1="' + str(index % 6) + \
                   '" y1="' + str(height + 1) +'" z1="'+ str(int(index / 6)) + \
                   '" x2="' + str(index % 6)  + '" y2="0" z2="' + \
                   str(int(index / 6))+ '" type="cobblestone" />'
        index += 1
    return xml

print(xml_hill(heights))
my_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
<Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

  <About>
    <Summary>Cliff walking mission based on Sutton and Barto.</Summary>
  </About>

  <ServerSection>
    <ServerInitialConditions>
        <Time><StartTime>1</StartTime></Time>
    </ServerInitialConditions>
    <ServerHandlers>
      <FlatWorldGenerator generatorString="3;2;1;village"/>
      <DrawingDecorator>
        <!-- coordinates for cuboid are inclusive -->''' + \
       xml_hill(heights) + '''        
      </DrawingDecorator>
      <ServerQuitFromTimeUp timeLimitMs="20000"/>
      <ServerQuitWhenAnyAgentFinishes/>
    </ServerHandlers>
  </ServerSection>

  <AgentSection mode="Survival">
    <Name>Bob</Name>
    <AgentStart>
      <Placement x="0" y="32" z="1000" pitch="30" yaw="0"/>
    </AgentStart>
    <AgentHandlers>
      <DiscreteMovementCommands/>
      <ObservationFromFullStats/>
      <RewardForTouchingBlockType>
        <Block reward="-100.0" type="lava" behaviour="onceOnly"/>
        <Block reward="100.0" type="lapis_block" behaviour="onceOnly"/>
      </RewardForTouchingBlockType>
      <RewardForSendingCommand reward="-1" />
      <AgentQuitFromTouchingBlockType>
          <Block type="lava" />
          <Block type="lapis_block" />
      </AgentQuitFromTouchingBlockType>
    </AgentHandlers>
  </AgentSection>

</Mission>
'''
my_mission = MalmoPython.MissionSpec(my_xml, True)

my_mission_record = MalmoPython.MissionRecordSpec()
agent_host = MalmoPython.AgentHost()
my_mission.requestVideo(800, 500)
my_mission.setViewpoint(1)
print("Waiting for the mission to start", end=' ')
my_client_pool = MalmoPython.ClientPool()
#my_client_pool.add(MalmoPython.ClientInfo("127.0.0.1", 10001))
agent_host.startMission(  my_mission, my_mission_record, )
world_state = agent_host.getWorldState()
while not world_state.has_mission_begun:
    print(".", end="")
    time.sleep(0.1)
    world_state = agent_host.getWorldState()
    for error in world_state.errors:
        print("Error:",error.text)
while world_state.is_mission_running:
    world_state = agent_host.getWorldState()
    if world_state.number_of_observations_since_last_state > 0:
        obvsText = world_state.observations[-1].text
        data = json.loads(obvsText) # observation comes in as a JSON string...
        print(data)
        current_x = data.get(u'XPos', 0)
        current_y = data.get(u'YPos', 0)
        current_z = data.get(u'ZPos', 0)
        #print(current_x, current_y, current_z)
current_y = data.get(u'YPos', 0)


