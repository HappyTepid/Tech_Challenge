CREATE TABLE Submissions(
   ID INT PRIMARY KEY     NOT NULL,
   FIRST_NAME           TEXT    NOT NULL,
   LAST_NAME           TEXT    NOT NULL,
   POSTCODE            VARCHAR(10)     NOT NULL,
   AMOUNT        FLOAT	NOT NULL,
   REASON         TEXT
);