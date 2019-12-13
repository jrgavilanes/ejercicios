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

