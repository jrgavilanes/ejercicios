
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

