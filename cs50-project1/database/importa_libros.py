import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("sqlite:///db.sqlite")
db = scoped_session(sessionmaker(bind=engine))


with open("books.csv", newline='') as File:
    reader = csv.reader(File)
    for isbn, titulo, autor, anyo in reader:
        # print(isbn,titulo,autor,anyo)
        db.execute("insert into libros (isbn,titulo,autor,anyo) values (:isbn, :titulo, :autor, :anyo)", {
            "isbn": isbn,
            "titulo": titulo,
            "autor": autor,
            "anyo": anyo,
        })

db.commit()
db.close()