from fastapi import FastAPI, HTTPException
from typing import List

from .database import BOSS_DATABASE
from .models import Boss, GuessFeedback, FeedbackStatus

# Inicialização do FastAPI
app = FastAPI()

# Valor fixo, alterar
BOSS_DO_DIA_NOME = "Malenia"
BOSS_DO_DIA_DADOS = Boss(**BOSS_DATABASE[BOSS_DO_DIA_NOME])

@app.get("/")
def read_root():
    return{"Projeto" : "Eldendle API"}

@app.get("/api/bosses/names", response_model=List[str])
def get_all_boss_names():
    # Endpoint para os palpites.
    return list(BOSS_DATABASE.keys())

@app.get("/api/boss/details/{boss_name}", response_model=Boss)
def get_boss_details(boss_name: str):
    # Endpoint para o cliente pegar os dados do boss
    if boss_name not in BOSS_DATABASE:
        raise HTTPException(status_code=404, detail="Boss não encontrado.")
    return BOSS_DATABASE[boss_name]
    
@app.post("/api/guess/{guess_name}", response_model=GuessFeedback)
def process_guess(guess_name: str):
    # Endpoint principal, o cliente envia o nome e o servidor compara com o BOSS_DO_DIA
    if guess_name not in BOSS_DATABASE:
        raise HTTPException(status_code=404, detail="Boss não encontrado.")
    
    guess_data = Boss(**BOSS_DATABASE[guess_name])
    
    feedback = {
        "nome": "correct" if guess_data.nome == BOSS_DO_DIA_DADOS.nome else "incorrect",
        "regiao": "correct" if guess_data.regiao == BOSS_DO_DIA_DADOS.regiao else "incorrect",
        "fase": "correct" if guess_data.fase == BOSS_DO_DIA_DADOS.fase else "incorrect",
        "tipo": "correct" if guess_data.tipo == BOSS_DO_DIA_DADOS.tipo else "incorrect",
        "raca": "correct" if guess_data.raca == BOSS_DO_DIA_DADOS.raca else "incorrect",
        "localizacao_especifica": "correct" if guess_data.localizacao_especifica == BOSS_DO_DIA_DADOS.localizacao_especifica else "incorrect",
        "drop_principal": "correct" if guess_data.drop_principal == BOSS_DO_DIA_DADOS.drop_principal else "incorrect",
        "obrigatorio": "correct" if guess_data.obrigatorio == BOSS_DO_DIA_DADOS.obrigatorio else "incorrect",
    }
    
    # Adicionar logica "partial" pra algumas coisas,
    
    return GuessFeedback(**feedback)