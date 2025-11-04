from pydantic import BaseModel
from typing import Literal

# Status de feedback para o jogo
FeedbackStatus = Literal["correct", "incorrect", "partial", "higher", "lower"]

class Boss(BaseModel):
    # Define a estrutura de um Boss.
    nome: str
    regiao: str
    fase: int
    tipo: str
    raca: str
    localizacao_especifica: str
    drop_principal: str
    obrigatorio: bool
    imagem_url: str
    runes: int
    
class GuessFeedback(BaseModel):
    # Define as respostas de feedback para o cliente.
    nome: FeedbackStatus
    regiao: FeedbackStatus
    fase: FeedbackStatus
    tipo: FeedbackStatus
    raca: FeedbackStatus
    localizacao_especifica: FeedbackStatus
    drop_principal: FeedbackStatus
    obrigatorio: FeedbackStatus
    runes: FeedbackStatus
    