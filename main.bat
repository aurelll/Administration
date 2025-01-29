@echo off
setlocal

REM Vérification si le script est lancé avec les privilèges administratifs
openfiles >nul 2>&1
if %errorlevel% neq 0 (
    echo Demande d'élévation des privilèges...
    REM Relancer le script avec élévation de privilèges
    powershell -Command "Start-Process cmd -ArgumentList '/c cd /d %~dp0 && %0' -Verb runAs"
    exit /b
)

REM Si déjà en mode admin, activer l'environnement virtuel
cd /d C:\.Scripts\Administration

REM Vérifier si l'environnement virtuel existe
if not exist "env" (
    echo Environnement virtuel non trouvé, création...
    python -m venv env
)

REM Activer l'environnement virtuel
call env\Scripts\activate

REM Vérification que l'environnement virtuel est bien activé
echo Environnement virtuel activé. Vous pouvez maintenant lancer main.py.

REM Vérifier si 'customtkinter' est installé dans l'environnement
python -m pip show customtkinter >nul 2>&1
if %errorlevel% neq 0 (
    echo Le module 'customtkinter' n'est pas installé. Installation en cours...
    python -m pip install customtkinter
)

REM Lancer main.py
python main.py

REM Garder la fenêtre ouverte après l'exécution
pause
