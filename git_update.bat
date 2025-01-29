@echo off
setlocal enabledelayedexpansion

:: Aller dans le dossier du projet 
:: cd /d "C:\chemin\vers\projet"

:: Demander un message de commit à l'utilisateur
set /p commit_msg=Entrez le message du commit : 

:: Fichiers modifiés
git add .

:: Valider les modifications avec le message entré
git commit -m "!commit_msg!"

:: Envoyer sur GitHub
git push origin main

echo.
echo ✅ Mise à jour envoyée sur GitHub avec succès !
pause