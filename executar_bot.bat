@echo off
cd /d C:\Users\Tera\Documents\bot_utilidade_publica

:: Registra o timestamp de inicio no arquivo de log
echo [%date% %time%] Iniciando rotina meteorologica do terreno... >> auditoria.log

call venv\Scripts\activate

:: Executa o bot e redireciona TODA a saida (sucesso e erro) para o log
python -u main.py >> auditoria.log 2>&1

deactivate

:: Registra o encerramento
echo [%date% %time%] Execucao finalizada. >> auditoria.log
echo -------------------------------------------------- >> auditoria.log
