@echo off
cd /d "%~dp0"
echo Installing dependencies...
py -3 -m pip install pandas numpy openpyxl matplotlib Pillow --quiet 2>nul || python -m pip install pandas numpy openpyxl matplotlib Pillow --quiet
echo.
echo Running pipeline with --regen flag (force fresh data from 25 June 2025)...
py -3 generate_pipeline.py --regen 2>nul || python generate_pipeline.py --regen
echo.
echo Done. Press any key to exit.
pause
