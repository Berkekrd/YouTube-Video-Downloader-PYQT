import subprocess
subprocess.run('python -m PyQt5.uic.pyuic -x main.ui -o mainPage.py')
# subprocess.run('python -m PyQt5.pyrcc_main deneme.qrc  -o deneme_rc.py')
# # pyinstaller --onefile --noconsole main.py
