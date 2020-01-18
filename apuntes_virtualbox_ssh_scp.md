# Virtual box

## Red

Crear Archivo / Administrador de red anfitrion
Maquinas virtuales:
    adaptador 1 : nat
    adaptador 2 : anfitrion

## Servidor Linux

### Pon IP estática al servidor
```bash
$ ifconfig -a
...
enp0s8: flags=4098<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        ether 08:00:27:e5:78:0f  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
 ...

$ cat /etc/network/interfaces
auto lo
iface lo inet loopback

auto enp0s8
iface enp0s8 inet static
address 192.168.56.100

```
### Poner nombre del host
```bash
$ cat /etc/hostname 
apihub

```

## Lista de hosts accesibles
```
cat /etc/hosts
127.0.0.1	localhost
127.0.1.1	MateBook

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

192.168.56.100	apihub
192.168.56.101	app1
192.168.56.102	app2
192.168.56.110	central1

```


## Autentificación SSH Key

### Genera clave privada/publica en cliente
```bash
ssh-keygen -t rsa -b 4096
```

### Sube la clave publica al servidor

#### modo facil
```bash
$ ssh-copy-id janrax@servidor 
```

#### modo dificil
```bash
# desde cliente
$ scp /home/janrax/.ssh/id_rsa.pub janrax@server:/home/janrax/.ssh/uploaded_key.pub
# en servidor
$ cat /home/janrax/.ssh/uploaded_key.pub >> /home/janrax/.ssh/authorized_keys
$ chmod 700 /home/janrax/.ssh
$ chmod 600 /home/janrax/.ssh/*
```

### Que ssh solo permita conexión con clave publica/privada
```
$ cat vi /etc/ssh/sshd_config 
...
PasswordAuthentication no
...

$ sudo service ssh restart
```
