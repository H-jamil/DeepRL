##
# @author Jamil Hasibul <mdhasibul.jamil@siu.edu>
 #
 #@desc Created on 2021-03-05 9:42:55 pm
 # @copyright
 #
import random

class Environment:
  def __init__(self):
    self.steps_left=10

  def get_observation(self):
    return [0.0, 0.0, 0.0]

  def get_actions(self):
    return [0,1]

  def is_done(self):
    return self.steps_left==0

  def action(self,action):
    if self.is_done():
      raise Exception ("Game is Over")
    self.steps_left-=1
    return random.random()


class Agent:
  def __init__(self):
    self.total_reward =0

  def step(self,env):
    current_obs=env.get_observation()
    action=env.get_actions()
    reward=env.action(random.choices(action))
    self.total_reward += reward


if __name__=="__main__":
  env=Environment()
  agent= Agent()

  while not env.is_done():
    agent.step(env)

  print("Toatl reward got %.4f" %agent.total_reward)
