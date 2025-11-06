@echo off
echo ===========================================
echo 1. ATIVANDO AMBIENTE VIRTUAL (.venv)
echo ===========================================
call .\.venv\Scripts\activate

echo.
echo ===========================================
echo 2. NAVEGANDO PARA A PASTA DO SERVIDOR
echo ===========================================
cd server

echo.
echo ===========================================
echo 3. INICIANDO SERVIDOR FASTAPI (em localhost)
echo Pressione CTRL+C para parar o servidor
echo ===========================================
rem O Uvicorn usa localhost (127.0.0.1) por padrao
uvicorn app.main:app --reload

echo.
echo Servidor foi finalizado.
pause