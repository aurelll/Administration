@echo off
setlocal
cd /d C:\.Scripts\Administration
python -m venv env
call env\Scripts\activate

echo Environnement virtuel activé. Vous pouvez maintenant lancer main.py.
cmd /k
