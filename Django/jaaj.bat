setlocal enabledelayedexpansion

set x=7

for /l %%i in (2, 1, %x%) do (
py -m venv minimal%%i
cd minimal%%i
py -m pip install Django
py -m pip install "colorama >= 0.4.6"
cd ..
)

endlocal
