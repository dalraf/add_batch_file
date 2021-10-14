import os

conteudo = '''
@echo off
ipconfig | find /i "IPv4"
pause
'''

filename = 'mostarip.bat'
dir = 'c:\\Users\\Public\\Desktop'
file_path = os.path.join(dir, filename)

with open(file_path, 'w') as file:
    file.write(conteudo)