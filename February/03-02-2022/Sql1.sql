CREATE DATABASE mytest;
use mytest


CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);

show tables

INSERT INTO persons (PersonID, FirstName, Lastname, Address, City)
VALUES (1, 'Tom B. richard', 'Skagen', 'Blr', 'Norway');

INSERT INTO persons (PersonID, FirstName, Lastname, Address, City)
VALUES (3, 'Tom', 'kar', 'Mumbai', 'navimumbai');

INSERT INTO persons (PersonID, FirstName, Lastname, Address, City)
VALUES (2, 'manu', 'Shukla', 'hyd', 'hitech city');


select * from persons

ALTER TABLE persons
ADD Email varchar(255);


ALTER TABLE persons
RENAME COLUMN Email TO Zipcode;

ALTER TABLE persons
DROP COLUMN Zipcode;

ALTER TABLE persons
ADD Phoneno int;

INSERT INTO persons (phoneno)
VALUES (900) WHERE lastname='Skagen';

select * from persons

SELECT * FROM Persons
WHERE PersonID=2;

UPDATE persons SET FirstName = 'rakesh' WHERE personID = 3;

drop table persons

SELECT FirstName, City FROM persons;

SELECT * FROM persons;

SELECT Address FROM persons;

SELECT COUNT(DISTINCT City) FROM persons;

SELECT * FROM persons
WHERE city='navimumbai'
or address= 'blr'

SELECT * FROM persons
WHERE city='navimumbai'
and address= 'mumbai'

SELECT * FROM persons
WHERE NOT City='norway';

SELECT * FROM persons
WHERE NOT City='norway' AND NOT City='navimumbai';

SELECT *FROM persons WHERE CITY IN("Norway","navimumbai")

SELECT *FROM persons WHERE CITY NOT IN("Norway")

SELECT * FROM persons
WHERE city LIKE '%y';


SELECT * FROM persons LIMIT 2;

SELECT firstName, lastName, Address
FROM persons
WHERE Address IS NULL;

SELECT firstName, lastName, Address
FROM persons
WHERE Address IS NOT NULL;

SELECT * FROM persons;

SELECT * FROM persons
ORDER BY address;

SELECT COUNT(personID), City
FROM persons
GROUP BY City;

SELECT COUNT(personID), City
FROM persons
GROUP BY City
ORDER BY COUNT(personID) DESC;

SELECT COUNT(lastname), City
FROM persons
GROUP BY City
HAVING COUNT(lastname) > 2;

SELECT COUNT(lastname), City
FROM persons
GROUP BY ROLLUP (firstname) ;

INSERT INTO persons (PersonID, FirstName, Lastname, Address, City)
VALUES (4, 'umar', 'doshi', 'blr', 'marathali');

INSERT INTO persons (PersonID, FirstName)
VALUES (6, 'hari', 'dash');

INSERT INTO persons (FirstName)
VALUES ('hari') ,('haary') ,('harish'),('dasha');

SELECT Firstname FROM persons;

-- INSERT IGNORE INTO persons
-- VALUES ('norway');

INSERT INTO persons (PersonID, FirstName, Lastname, Address, City)
VALUES (14, 'arun', 'sahu', 'berhampur', 'aska');

 
