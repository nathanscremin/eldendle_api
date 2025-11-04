# Bibliotecas
import random
import uuid

from fastapi import FastAPI, HTTPException
from typing import List, Dict
from .database import BOSS_DATABASE
from .models import Boss, GuessFeedback, FeedbackStatus

# Inicialização do FastAPI
app = FastAPI()

# Inicialização do jogo
ACTIVE_GAMES: Dict[str, Boss] = {}

#Função que randomiza o boss
def get_new_random_boss() -> Boss:
    all_boss_names = list(BOSS_DATABASE.keys())
    random_boss_name = random.choice(all_boss_names)
    print(f"--- Novo jogo criado. Resposta: {random_boss_name} ---")
    return Boss(**BOSS_DATABASE[random_boss_name])

@app.get("/")
def read_root():
    return{"Projeto" : "Eldendle API"}

@app.get("/api/bosses/names", response_model=List[str])
def get_all_boss_names():
    return list(BOSS_DATABASE.keys())

@app.get("/api/boss/details/{boss_name}", response_model=Boss)
def get_boss_details(boss_name: str):
    # Endpoint para o cliente pegar os dados do boss
    if boss_name not in BOSS_DATABASE:
        raise HTTPException(status_code=404, detail="Boss não encontrado.")
    return BOSS_DATABASE[boss_name]
    
@app.post("/app/game/start")
def start_new_game():
    # Criar um novo jogo
    game_id = str(uuid.uuid4())
    correct_boss = get_new_random_boss()
    ACTIVE_GAMES[game_id] = correct_boss
    return {"game_id": game_id}

@app.post("/api/guess/{game_id}/{guess_name}", response_model=GuessFeedback)
def process_guess(game_id: str, guess_name: str):
    # Endpoint principal
    correct_boss_data = ACTIVE_GAMES.get(game_id)

    if not correct_boss_data:
        raise HTTPException(status_code=404, detail="Sessão de jogo não encontrada. Inicie um novo jogo.")
    if guess_name not in BOSS_DATABASE:
        raise HTTPException(status_code=404, detail="Boss não encontrado.")
    
    guess_data = Boss(**BOSS_DATABASE[guess_name])
    feedback = {}
    feedback["nome"] = "correct" if guess_data.nome == correct_boss_data.nome else "incorrect"
    feedback["tipo"] = "correct" if guess_data.tipo == correct_boss_data.tipo else "incorrect"
    feedback["raca"] = "correct" if guess_data.raca == correct_boss_data.raca else "incorrect"
    feedback["drop_principal"] = "correct" if guess_data.drop_principal == correct_boss_data.drop_principal else "incorrect"
    feedback["obrigatorio"] = "correct" if guess_data.obrigatorio == correct_boss_data.obrigatorio else "incorrect"

    if guess_data.localizacao_especifica == correct_boss_data.localizacao_especifica:
        feedback["localizacao_especifica"] = "correct"
        feedback["regiao"] = "correct"
    elif guess_data.regiao == correct_boss_data.regiao:
        feedback["localizacao_especifica"] = "incorrect"
        feedback["regiao"] = "partial" 
    else:
        feedback["localizacao_especifica"] = "incorrect"
        feedback["regiao"] = "incorrect"
        
    if guess_data.fase == correct_boss_data.fase:
        feedback["fase"] = "correct"
    elif guess_data.fase < correct_boss_data.fase:
        feedback["fase"] = "higher" 
    else:
        feedback["fase"] = "lower" 

    if guess_data.runes == correct_boss_data.runes:
        feedback["runes"] = "correct"
    elif guess_data.runes < correct_boss_data.runes:
        feedback["runes"] = "higher" 
    else:
        feedback["runes"] = "lower"  
        
    return GuessFeedback(**feedback)