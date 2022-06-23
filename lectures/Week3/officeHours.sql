
-- This is for the class table
SELECT * FROM class;
INSERT INTO class (className, description) VALUES ('Python', 'Intro to the Python language and Flask');
INSERT INTO class (className, description) VALUES ("Web Fundamentals", "Beginner course teaching the basics of HTML, CSS, and JS");

-- This is for the student table
SELECT * FROM student;
INSERT INTO student (firstName, lastName, email, class_id) VALUES ("Jane", "Doe", "jane@doe.com", 1);
INSERT INTO student (firstName, lastName, email, class_id) VALUES ('Bob', 'Ross', 'bob@ross.com', 2);
insert into student (firstName, lastName, email, class_id) values ("Bob", "Smith", "bob@smith.com", 1);
select * from student where class_id=1;
select * from student where firstName="Bob";
select * from student where firstName="bob";