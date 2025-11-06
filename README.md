# Eldendle API - Miniprojeto Fatec

**Eldendle** é um miniprojeto desenvolvido para a disciplina de Programação de Scripts da Fatec Rio Claro. O tema do trabalho é *Consumo de APIs* e o resultado é um jogo no estilo "Wordle" focado no universo de **Elden Ring**: um servidor com uma API que fornece dados de bosses e um cliente em console que consome essa API para permitir palpites e partidas locais.

---

## ✨ Visão Geral

O repositório está organizado em duas partes principais:

* `server/` — API (backend) construída com **FastAPI** em Python.
* `client/` — Cliente de terminal (frontend) em Python que consome a API usando a biblioteca `requests`.

O objetivo é oferecer um microprojeto completo para demonstrar consumo de APIs, sessões de jogo, e comunicação cliente-servidor em um contexto didático.

---

## ✨ Funcionalidades

### Backend (Servidor)

* Servidor FastAPI com um banco de dados (simples) contendo dezenas de bosses do universo Elden Ring.
* Endpoints para iniciar sessões de jogo, listar bosses, consultar detalhes e registrar palpites.
* Randomização do boss alvo a cada novo jogo.
* Lógica que retorna dicas por campo (por exemplo: `correct`, `partial`, `higher`, `lower`).
* Documentação automática via Swagger (disponível em `/docs` quando o servidor estiver rodando).

### Frontend (Cliente)

* Jogo executável no terminal.
* Verifica se o servidor está online antes de iniciar.
* Menu interativo com opções para: jogar, listar bosses e sair.
* Envia palpites ao servidor e exibe as dicas formatadas para o usuário.
* Detecta condição de vitória quando todos os campos estão corretos.

---

## 💻 Tecnologias

* **Servidor (Backend):** Python 3.x, FastAPI, Uvicorn
* **Cliente (Frontend):** Python 3.x, requests

---

## 📁 Estrutura do Projeto

```
eldendle_api/
├── .venv/                      (Ambiente virtual)
├── client/
│   ├── procura_boss.py
│   └── requirements.txt
├── server/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── database.py
│   │   └── models.py
│   └── requirements.txt
├── .gitignore
├── iniciar_servidor.bat        (Script para iniciar em rede)
├── iniciar_servidor_local.bat  (Script para iniciar em localhost)
└── README.md
```

---

## 🚀 Como Rodar (Guia Rápido)

### Pré-requisitos

* Python 3.10+
* Git

### 1) Clonar o repositório

```bash
git clone https://github.com/nathanscremin/eldendle_api.git
cd eldendle_api
```

### 2) Criar e ativar ambiente virtual

**No Windows (PowerShell/CMD):**

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

(Em Linux/macOS adapte o comando de ativação do venv.)

### 3) Instalar dependências

```bash
# Backend
pip install -r server/requirements.txt

# Frontend
pip install -r client/requirements.txt
```

### 4) Iniciar servidor

Existem scripts preparados ou você pode iniciar manualmente:

**Opção (arquivo):**

* Dar dois cliques em `iniciar_servidor_local.bat` para rodar em localhost.
* Dar dois cliques em `iniciar_servidor.bat` para rodar em rede (lembre de liberar no firewall).

**Opção (manual):**

```bash
cd server
uvicorn app.main:app --reload
# Para aceitar conexões externas:
# uvicorn app.main:app --reload --host 0.0.0.0
```

> O servidor deve ficar rodando em seu próprio terminal.

### 5) Rodar o cliente

1. Abra um novo terminal (mantendo o servidor rodando).
2. Ative o mesmo ambiente virtual:

```bash
cd eldendle_api
.\.venv\Scripts\activate
```

3. Vá para a pasta do cliente e execute:

```bash
cd client
python procura_boss.py
```

Siga as instruções no terminal para jogar.

---

## 📚 Endpoints (Referência)

Base URL (padrão durante desenvolvimento): `http://127.0.0.1:8000`

* **POST** `/api/game/start` — Cria uma nova sessão de jogo. Retorna um `game_id` único.

  ```json
  { "game_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890" }
  ```

* **GET** `/api/bosses/names` — Retorna a lista de nomes dos bosses (array de strings).

  ```json
  [ "Godrick the Grafted", "Rennala, Queen of the Full Moon", "..." ]
  ```

* **GET** `/api/boss/details/{boss_name}` — Retorna os dados completos de um boss.

  ```json
  {
    "nome": "Godrick the Grafted",
    "regiao": "Limgrave",
    "fase": 2,
    "tipo": "Demigod",
    "raca": "Humanoid",
    "localizacao_especifica": "Stormveil Castle",
    "drop_principal": "Godrick's Great Rune",
    "obrigatorio": true,
    "runes": 20000,
    "imagem_url": "https://..."
  }
  ```

* **POST** `/api/guess/{game_id}/{guess_name}` — Envia um palpite para a sessão indicada. Retorna um objeto com dicas por campo:

  ```json
  {
    "nome": "incorrect",
    "regiao": "partial",
    "fase": "higher",
    "tipo": "correct",
    "raca": "incorrect",
    "localizacao_especifica": "incorrect",
    "drop_principal": "incorrect",
    "obrigatorio": "correct",
    "runes": "lower"
  }
  ```

---

## 🧾 Licença & Créditos

Projeto desenvolvido como entrega acadêmica para a disciplina de Programação de Scripts da Fatec Rio Claro.
