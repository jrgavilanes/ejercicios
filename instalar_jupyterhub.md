# INSTALACIÓN JUPYTERHUB

Ojo el primer usuario será el administrador, y la clave de acceso que ponga será la que se le asignará.

```

curl https://raw.githubusercontent.com/jupyterhub/the-littlest-jupyterhub/master/bootstrap/bootstrap.py | sudo python3 - --admin janrax

tljh-config set https.enabled true
tljh-config set https.letsencrypt.email janrax@yopmail.com
tljh-config add-item https.letsencrypt.domains python.codekai.es
tljh-config reload proxy
systemctl restart jupyterhub.service

## SWAP FILE GUAPO
```
fallocate -l 2G /swapfile
chmod 600 /swapfile
mkswap /swapfile
swapon /swapfile
sh -c 'echo "/swapfile none swap sw 0 0" >> /etc/fstab'
reboot
```

```


# INSTALAR PAQUETES

Desde el terminal del usuario administrador dentro de jupyterhub( desde la máquina no vale)

ejemplo para instalar numpy
```
sudo -E conda install -c conda-forge numpy
```
