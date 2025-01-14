import gymnasium as gym
from gymnasium import spaces
import numpy as np

class TradingEnv(gym.Env):
    """Environnement de simulation pour le trading"""

    def __init__(self):
        super(TradingEnv, self).__init__()

        # Définition de l'espace d'observation (ex: prix actuel, volume, indicateurs techniques)
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(5,), dtype=np.float32)

        # Définition de l'espace d'action (0 = vendre, 1 = hold, 2 = acheter)
        self.action_space = spaces.Discrete(3)

        # Initialisation de l'état (prix, volume, etc.)
        self.state = np.random.rand(5)
        self.done = False

    def reset(self, seed=None, options=None):
        """Réinitialise l'environnement"""
        self.state = np.random.rand(5)
        self.done = False
        return self.state, {}

    def step(self, action):
        """Applique une action et met à jour l'environnement"""
        reward = np.random.randn()  # Simulation d'un profit ou d'une perte
        self.state = np.random.rand(5)
        self.done = np.random.rand() > 0.95  # L'épisode se termine avec une probabilité de 5%
        
        # ✅ Retourne 5 valeurs (obs, reward, done, truncated, info)
        return self.state, reward, self.done, False, {}
