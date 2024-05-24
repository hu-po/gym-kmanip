import os
import pprint

import h5py
import gymnasium as gym
import numpy as np

import gym_kmanip as k

# choose your environment
# ENV_NAME: str = "KManipSoloArm"
# ENV_NAME: str = "KManipSoloArmQPos"
ENV_NAME: str = "KManipSoloArmVision"
# ENV_NAME: str = "KManipDualArm"
# ENV_NAME: str = "KManipDualArmQPos"
# ENV_NAME: str = "KManipDualArmVision"
# ENV_NAME: str = "KManipTorso"
# ENV_NAME: str = "KManipTorsoVision"
env = gym.make(
    ENV_NAME,
    log_h5py=True,
    log_rerun=True,
    log_prefix="sim_synth",
)
# env.reset()

NUM_EPISODES: int = 100
for _ in range(NUM_EPISODES):
    env.reset()
    for _ in range(k.MAX_EPISODE_STEPS):
        action  = env.action_space.sample()
        # heuristic action moving towards cube
        cube_pos = env.unwrapped.env.physics.data.qpos[-7:-4].copy()
        eer_pos = env.unwrapped.env.physics.data.site("eer_site_pos").xpos.copy()
        raw_action = cube_pos - eer_pos
        raw_action /= np.linalg.norm(raw_action)
        print(f"raw_action: {raw_action}")
        action["eer_pos"] = raw_action
        _, _, terminated, truncated, _ = env.step(action)
        if terminated or truncated:
            break

env.close()

log_path = os.path.join(env.unwrapped.log_dir, "episode_1.hdf5")
print(f"Opening hdf5 file at \n\t{log_path}")
f = h5py.File(log_path, "r")
print("\nroot level keys:\n")
print(f.keys())
print("\nmetadata:\n")
pprint.pprint(dict(f['metadata'].attrs.items()))
print("\ndata:\n")
print(f['observations/qpos'][0])
print(f['observations/qvel'][0])