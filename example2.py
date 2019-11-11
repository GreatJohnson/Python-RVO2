import rvo2
import numpy as np
import matplotlib.pyplot as plt

sim = rvo2.PyRVOSimulator(1/100., 1, 5, 1.5, 1.5, 0.5, 5)

# Pass either just the position (the other parameters then use
# the default values passed to the PyRVOSimulator constructor),
# or pass all available parameters.
a0 = sim.addAgent((0, 0))
a1 = sim.addAgent((1, 0))
a2 = sim.addAgent((1, 1))
a3 = sim.addAgent((0, 1))

# Obstacles are also supported.
o1 = sim.addObstacle([(0.1, 0.1), (-0.1, 0.1), (-0.1, -0.1),(0.5,0.5),(0.3,0.3),(0.2,0.2),(0.2,0.5)])
sim.processObstacles()

sim.setAgentPrefVelocity(a0, (5, 5))
sim.setAgentPrefVelocity(a1, (-5, 5))
sim.setAgentPrefVelocity(a2, (-5, -5))
sim.setAgentPrefVelocity(a3, (5, -5))

print('Simulation has %i agents and %i obstacle vertices in it.' %
      (sim.getNumAgents(), sim.getNumObstacleVertices()))

print('Running simulation')

for step in range(80):
    sim.doStep()

    positions = ['(%5.3f, %5.3f)' % sim.getAgentPosition(agent_no)
                 for agent_no in (a0, a1, a2, a3)]
    print('step=%2i  t=%.3f  %s' % (step, sim.getGlobalTime(), '  '.join(positions)))
    a00 = sim.getAgentPosition(a0)
    a01 = sim.getAgentPosition(a1)
    a02 = sim.getAgentPosition(a2)
    a03 = sim.getAgentPosition(a3)


    plt.cla()

    plt.title("Multi-Agent")
    plt.grid(True)

    plt.xlim(-2, 2)

    plt.ylim(-2, 2)

    plt.scatter(a00[0],a00[1],s=40)
    plt.scatter(a01[0],a01[1],s=40)
    plt.scatter(a02[0],a02[1],s=40)
    plt.scatter(a03[0],a03[1],s=40)

    plt.scatter(-0.1, -0.1,s=30,c='R')
    plt.scatter(0.1, 1,s=30,c='R')
    plt.scatter(-0.1, 1,s=30,c='R')
    plt.scatter(0.5, 0.5,s=30,c='R')
    plt.scatter(0.3, 0.3,s=30,c='R')
    plt.scatter(0.2, 0.2,s=30,c='R')
    plt.scatter(0.2, 0.5,s=30,c='R')
    plt.pause(0.005)

