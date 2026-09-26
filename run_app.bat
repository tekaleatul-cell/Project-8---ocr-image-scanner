@echo off
if not exist ".venv\Scripts\streamlit.exe" (
    echo The application environment is missing.
    echo Run the first-time setup commands in README.md first.
    pause
    exit /b 1
)
call ".venv\Scripts\streamlit.exe" run app.py
