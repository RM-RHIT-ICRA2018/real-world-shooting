from gym.envs.registration import register

register(
        id='shooting',
        entry_point='real_world_shooting.envs:ShootingEnv',
)
