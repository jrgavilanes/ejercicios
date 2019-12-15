PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

CREATE TABLE flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);

INSERT INTO flights VALUES(1,'New York','London',415);
INSERT INTO flights VALUES(2,'Shanghai','Paris',760);
INSERT INTO flights VALUES(3,'Istanbul','Tokyo',700);
INSERT INTO flights VALUES(4,'New York','Paris',435);
INSERT INTO flights VALUES(5,'Moscow','Paris',245);
INSERT INTO flights VALUES(6,'Lima','New York',455);

CREATE TABLE passengers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL,
    flight_id INTEGER REFERENCES flights (id) ON DELETE CASCADE
                                              ON UPDATE CASCADE
);
INSERT INTO passengers VALUES(1,'Alice',1);
INSERT INTO passengers VALUES(2,'Bob',1);
INSERT INTO passengers VALUES(3,'Charlie',2);
INSERT INTO passengers VALUES(4,'Dave',2);
INSERT INTO passengers VALUES(5,'Erin',4);
INSERT INTO passengers VALUES(6,'Frank',6);
INSERT INTO passengers VALUES(7,'Grace',6);
INSERT INTO passengers VALUES(8,'juanra',1);

COMMIT;
