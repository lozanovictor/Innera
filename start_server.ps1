# 1 - Definir o diretório atual
Set-Location -Path $PSScriptRoot

# 2 - Executar pip install matplotlib
pip install matplotlib

# 3 - Executar o comando 'python manage.py runserver'
Start-Process "python" "manage.py runserver"

# 4 - Abrir o navegador no endereço 'http://127.0.0.1:8000/'
Start-Process "http://127.0.0.1:8000/"