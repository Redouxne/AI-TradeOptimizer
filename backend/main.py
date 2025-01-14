from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 1️⃣ Déclaration de l'application FastAPI
app = FastAPI()

# 2️⃣ Ajout du middleware CORS après la déclaration de l'application
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3️⃣ Définition des routes
@app.get("/")
def home():
    return {"message": "Welcome to AI Trade Optimizer"}

# 4️⃣ Lancer l'API avec Uvicorn si exécuté directement
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
