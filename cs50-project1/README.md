

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
