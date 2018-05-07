import gym
from gym import error, spaces, utils
from gym.utils import seeding

class ShootingEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.action_dim=2 #the angle accleration of the turret
        self.obs_dim=1+2+2  #the current distance, the current velocity (in the turret coordination), 
                            #the current pixel distance between the center of the camera and the target 
        bounds=[[0,0],[1,1]] #the bound on the accerlation of the turret
        low = bounds[:, 0]
        high = bounds[:, 1]
        self.action_space = spaces.Box(low=low, high=high)

        high = np.inf*np.ones(self.obs_dim)
        low = -high
        self.observation_space = spaces.Box(low, high)

    def step(self, action): #apply action to the robot

    
    def reset(self):
        
    #def render(self):
    
