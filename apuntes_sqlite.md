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


def main():

    db_file = os.path.join(os.path.dirname(__file__), "db.sqlite")

    db = sqlite3.connect(db_file)

    qAux = db.cursor()

    try:
        _ = qAux.execute("select * from usuarios").fetchone()
    except sqlite3.OperationalError as e:
        if e == "no such table: usuarios":
            qAux.execute("create table usuarios (id integer, name text)")
        else:
            print("Error:",e)
            exit(1)
            
    for _ in range(100000):
        qAux.execute("insert into usuarios (name) values('juanra')")

    db.commit()

    db.close()

    print("au")


if __name__ == "__main__":
    main()

```
