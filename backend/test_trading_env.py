from trading_env import TradingEnv

# Créer l'environnement
env = TradingEnv()

# Réinitialiser l'environnement
obs, info = env.reset()

print("État initial :", obs)

# Tester l'environnement sur 10 étapes
for i in range(10):
    action = env.action_space.sample()  # Choisir une action aléatoire
    obs, reward, done, _, _ = env.step(action)
    print(f"Étape {i + 1} - Action: {action}, Récompense: {reward}, État: {obs}")

    if done:
        print("Fin de l'épisode, réinitialisation de l'environnement.\n")
        obs, info = env.reset()
