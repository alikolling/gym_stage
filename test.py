import gym
import gym_stage
import rospy

rospy.init_node('aa')
env = gym.make('Stage-v0', env_stage=1, continuous=True, goal_list=None)

env.reset()

while True:
    a = [1,1]
    s = env.step(a)
    print(s)    
    
