# Proyecto 1 cs50

## Enunciado del ejercicio
https://docs.cs50.net/ocw/web/projects/1/project1.html


## Arrancar entorno y ejecutar aplicación

```bash
cd cs50-project1
pipenv shell
pipenv install  # Si es la primera vez
python app.py   # Arrancamos servidor de pruebas
```

## Esquema de la base de datos
```sql
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR UNIQUE NOT NULL,
    password VARCHAR NOT NULL,
    active_session VARCHAR
);

CREATE TABLE libros (
    isbn text primary key,
    titulo text not null,
    autor text not null,
    anyo integer not null
);


CREATE TABLE comentarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario integer not null,
    isbn text not null,
    comentario text not null,
    puntuacion int not null,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    FOREIGN KEY (isbn) REFERENCES libros(isbn),
    UNIQUE(id_usuario,isbn)
);
```
