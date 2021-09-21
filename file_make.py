import os

conteudo = '''
@echo off
ipconfig | find /i "IPv4"
pause
'''

filename = 'mostarip.bat'
file_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', filename)

with open(file_path, 'w') as file:
    file.write(conteudo)