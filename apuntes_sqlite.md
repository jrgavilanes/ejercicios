# Apuntes SQLite

## Instalación

https://www.sqlite.org/index.html

Instalación en Linux
```
$ sudo apt-get install sqlite3
```

Gestor visual

https://sqlitestudio.pl/index.rvt

## SQL básicos

Comandos básicos
```
$ sqlite3 db.sqlite
sqlite> .header on
sqlite> .mode column
sqlite> select * from pasajeros;
id          nombre      vuelo_id  
----------  ----------  ----------
3           juanra      2         

```

Cerrar
```
sqlite> .quit
```

Ver bases de datos activas
```
sqlite> .databases
main: /home/janrax/Escritorio/db2.sqlite
sqlite> 

```

Ver tablas disponibles
```
sqlite> .tables
usuarios
sqlite> .schema usuarios
CREATE TABLE usuarios (
    id         INTEGER       PRIMARY KEY AUTOINCREMENT,
    nombre     VARCHAR (100) NOT NULL,
    password   VARCHAR (100) NOT NULL,
    created_at DATE          DEFAULT (datetime('now', 'localtime') ),
    updated_at DATE          DEFAULT (datetime('now', 'localtime') ) 
);
```

Exportar datos a csv
```
.mode csv
.separator |
.output usuarios.csv
select * from usuarios;
```

Exportar datos como inserts
```
.mode insert nueva_tabla
.output usuarios.sql
select * from usuarios;
```

Exportar esquema completo
```
.output esquema_db.sql
.schema
```

Exportar esquema de una tabla
```
.output esquema_usuarios.sql
.schema usuarios
```

Backup de la base de datos
```
sqlite3 db.sqlite .dump > dump.sql
```

Restore
```
sqlite3 dbNueva.sqlite < dump.sql
```

Crear y relacionar tablas
```
--
-- File generated with SQLiteStudio v3.2.1 on vie. dic. 13 20:09:13 2019
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: pasajeros
DROP TABLE IF EXISTS pasajeros;

CREATE TABLE pasajeros (
    id       INTEGER       PRIMARY KEY AUTOINCREMENT,
    nombre   VARCHAR (100) NOT NULL,
    vuelo_id INTEGER       REFERENCES vuelos (id) ON DELETE CASCADE
                                                  ON UPDATE CASCADE
);

INSERT INTO pasajeros (id, nombre, vuelo_id) VALUES (3, 'juanra', 2);

-- Table: vuelos
DROP TABLE IF EXISTS vuelos;

CREATE TABLE vuelos (
    id         INTEGER       PRIMARY KEY AUTOINCREMENT,
    origen     VARCHAR (100) NOT NULL,
    destino    VARCHAR (100) NOT NULL,
    duracion   INTEGER       NOT NULL,
    created_at DATE          DEFAULT (datetime('now', 'localtime') ),
    updated_at DATE          DEFAULT (datetime('now', 'localtime') ) 
);

INSERT INTO vuelos (id, origen, destino, duracion, created_at, updated_at) VALUES (2, 'valencia', 'madrid', 30, '2019-12-13 19:44:07', '2019-12-13 19:44:07');
INSERT INTO vuelos (id, origen, destino, duracion, created_at, updated_at) VALUES (3, 'valencia', 'madrid', 30, '2019-12-13 19:44:09', '2019-12-13 19:44:09');

-- Trigger: vuelos_update_trigger
DROP TRIGGER IF EXISTS vuelos_update_trigger;
CREATE TRIGGER vuelos_update_trigger
         AFTER UPDATE OF id,
                         origen,
                         destino,
                         duracion
            ON vuelos
      FOR EACH ROW
BEGIN
    UPDATE vuelos
       SET updated_at = datetime('now', 'localtime') 
     WHERE id = new.id;
END;


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

```
## Programa basico python y sqlite3

```
import sqlite3
import os

esquema_bd = """
CREATE TABLE usuarios (
    id         INTEGER       PRIMARY KEY AUTOINCREMENT,
    nombre     VARCHAR (100) NOT NULL,
    password   VARCHAR (100) NOT NULL,
    created_at DATE          DEFAULT (datetime('now', 'localtime') ),
    updated_at DATE          DEFAULT (datetime('now', 'localtime') ) 
);
"""

trigger_db = """
CREATE TRIGGER usuarios_update_trigger
         AFTER UPDATE OF id,
                         nombre,
                         password
            ON usuarios
      FOR EACH ROW
BEGIN
    UPDATE usuarios
       SET updated_at = datetime('now', 'localtime') 
     WHERE id = new.id;
END;
"""

def main():

    db_file = os.path.join(os.path.dirname(__file__), "db.sqlite")

    db = sqlite3.connect(db_file)

    qAux = db.cursor()

    try:
        _ = qAux.execute("select * from usuarios").fetchone()
    except sqlite3.OperationalError as e:
        if str(e) == "no such table: usuarios":
            qAux.execute(esquema_bd)
            qAux.execute(trigger_db)
        else:
            print("Error:", e)
            exit(1)

    for i in range(1,100000):
        # qAux.execute(f"insert into usuarios (nombre, password) values('juanra{i}', 'clave{i}')")
        qAux.execute("insert into usuarios (nombre, password) values(?,?)",(f'juanra{i}', f'clave{i}') )

    qAux.execute("update usuarios set nombre = 'cambiado' where id=1")

    db.commit()

    id, nombre = qAux.execute("select id, nombre from usuarios").fetchone()
    print(f"El primer registro es {id}: {nombre}")

    db.close()

    exit(0)


if __name__ == "__main__":
    main()
    
```
