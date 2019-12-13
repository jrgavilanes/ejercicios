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

Crear y relacionar tablas
```
CREATE TABLE vuelos (
    id         INTEGER       PRIMARY KEY AUTOINCREMENT,
    origen     VARCHAR (100) NOT NULL,
    destino    VARCHAR (100) NOT NULL,
    duracion   INTEGER       NOT NULL,
    created_at DATE          DEFAULT (datetime('now', 'localtime') ),
    updated_at DATE          DEFAULT (datetime('now', 'localtime') )
);

CREATE TRIGGER update_last_time <-- REVISAR
     UPDATE OF origen,
               destino,
               duracion
            ON vuelos
BEGIN
    UPDATE vuelos
       SET updated_at = datetime('now', 'localtime') 
     WHERE id = id;
END;

CREATE TABLE pasajeros (
    id       INTEGER       PRIMARY KEY AUTOINCREMENT,
    nombre   VARCHAR (100) NOT NULL,
    vuelo_id INTEGER       REFERENCES vuelos (id) ON DELETE CASCADE
                                                  ON UPDATE CASCADE
);
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


# $ sqlite3 db.sqlite
# sqlite> .header on
# sqlite> .mode column
# sqlite> select * from usuarios;
# id          name      
# ----------  ----------
#             juanra    
#             juanra    
```
