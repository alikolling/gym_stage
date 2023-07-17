import gym
import gym_stage
import rospy
import numpy as np

rospy.init_node('aa')
env = gym.make('Stage-v0', env_stage=1, continuous=True, goal_list=None)

env.reset()

while True:

    a = np.random.rand(2)
    s, r, d ,_ = env.step(a)
    print(s, r)
    if d:
        env.reset()

