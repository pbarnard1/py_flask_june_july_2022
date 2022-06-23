-- Office hours class database class table
SELECT * FROM officehours.class;
SELECT * FROM class left join student on class.id = student.class_id where class.id = 1;
SELECT * FROM class join student on class.id = student.class_id where class.id = 3; -- will show only the rows that both have data
SELECT * FROM class left join student on class.id = student.class_id where class.id = 3; -- will return all rows for the 1st tabel and any that match for the second

-- office hours class database student table
SELECT * FROM officehours.student;
SELECT * FROM student left join class on student.class_id = class.id where student.id = 2;
SELECT * FROM student left join class on class.id = student.class_id where student.id = 2;