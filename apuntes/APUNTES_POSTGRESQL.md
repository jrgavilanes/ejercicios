# Apuntes Postgres SQL

## Fuentes

https://medium.com/coding-blocks/creating-user-database-and-adding-access-on-postgresql-8bfcd2f4a91e
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04


## Instalar en Linux

```
$ sudo apt update
$ sudo apt install postgresql postgresql-contrib
```

## Acceder como usuario administrador ( postgres )

```
$ sudo -i -u postgres
$ psql
```

## Salir del prompt

```
postgres=# \q
```

## COMBO: Crear BD, Usuario y asignar Usuario a Bd
```
$ sudo -u postgres psql
postgres=# create database mydb;
postgres=# create user myuser with encrypted password 'mypass';
postgres=# grant all privileges on database mydb to myuser;
```
