import gymnasium as gym

# Test d'un environnement simple (CartPole)
env = gym.make("CartPole-v1", render_mode="human")
obs, info = env.reset()

print("État initial :", obs)

for _ in range(10):  # Joue 10 itérations
    action = env.action_space.sample()  # Choisit une action aléatoire
    obs, reward, terminated, truncated, info = env.step(action)
    print(f"Action: {action}, Récompense: {reward}, État: {obs}")

    if terminated or truncated:
        obs, info = env.reset()

env.close()
