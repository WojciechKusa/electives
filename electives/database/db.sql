CREATE TABLE Class_Type (
  idClass SERIAL  NOT NULL ,
  Name TEXT    ,
  MinStudents INTEGER    ,
  MaxStudents INTEGER      ,
PRIMARY KEY(idClass));




CREATE TABLE User_2 (
  idUser_2 SERIAL  NOT NULL ,
  Name TEXT NOT NULL   ,
  Surname TEXT  NOT NULL  ,
  Mail TEXT   UNIQUE NOT NULL,
  Login TEXT  UNIQUE NOT NULL,
  Password_2 TEXT   NOT NULL ,
  Permissions INTEGER   NOT NULL   ,
PRIMARY KEY(idUser_2));




CREATE TABLE Student (
  idStudent SERIAL  NOT NULL ,
  User_2_idUser_2 INTEGER   NOT NULL ,
  FieldOfStudy TEXT  NOT NULL  ,
  Year_2 INTEGER   NOT NULL ,
  Semester INTEGER  NOT NULL    ,
  ID INTEGER   NOT NULL ,
PRIMARY KEY(idStudent)  ,
  FOREIGN KEY(User_2_idUser_2)
    REFERENCES User_2(idUser_2));


CREATE INDEX Student_FKIndex1 ON Student (User_2_idUser_2);


CREATE INDEX IFK_Rel_09 ON Student (User_2_idUser_2);


CREATE TABLE Staff (
  idStaff SERIAL  NOT NULL ,
  User_2_idUser_2 INTEGER   NOT NULL ,
  Department TEXT    ,
  Title TEXT      ,
PRIMARY KEY(idStaff)  ,
  FOREIGN KEY(User_2_idUser_2)
    REFERENCES User_2(idUser_2));


CREATE INDEX Staff_FKIndex1 ON Staff (User_2_idUser_2);


CREATE INDEX IFK_Rel_10 ON Staff (User_2_idUser_2);


CREATE TABLE Course (
  idCourse SERIAL  NOT NULL ,
  Staff_idStaff INTEGER   NOT NULL ,
  Name TEXT    ,
  ID INTEGER    ,
  ECTS INTEGER    ,
  Desription TEXT    ,
  Hours INTEGER    ,
  MinStudents INTEGER    ,
  MaxStudents INTEGER    ,
  Semester INTEGER      ,
PRIMARY KEY(idCourse)  ,
  FOREIGN KEY(Staff_idStaff)
    REFERENCES Staff(idStaff));


CREATE INDEX Course_FKIndex1 ON Course (Staff_idStaff);


CREATE INDEX IFK_Rel_09 ON Course (Staff_idStaff);


CREATE TABLE Student_has_Course (
  Student_idStudent INTEGER   NOT NULL ,
  Course_idCourse INTEGER   NOT NULL   ,
PRIMARY KEY(Student_idStudent, Course_idCourse)    ,
  FOREIGN KEY(Student_idStudent)
    REFERENCES Student(idStudent),
  FOREIGN KEY(Course_idCourse)
    REFERENCES Course(idCourse));


CREATE INDEX Student_has_Course_FKIndex1 ON Student_has_Course (Student_idStudent);
CREATE INDEX Student_has_Course_FKIndex2 ON Student_has_Course (Course_idCourse);


CREATE INDEX IFK_Rel_03 ON Student_has_Course (Student_idStudent);
CREATE INDEX IFK_Rel_04 ON Student_has_Course (Course_idCourse);


CREATE TABLE Class (
  Course_idCourse INTEGER   NOT NULL ,
  Class_Type_idClass INTEGER   NOT NULL ,
  Staff_idStaff INTEGER   NOT NULL ,
  Hours INTEGER    ,
  Instructor TEXT      ,
PRIMARY KEY(Course_idCourse, Class_Type_idClass)      ,
  FOREIGN KEY(Course_idCourse)
    REFERENCES Course(idCourse),
  FOREIGN KEY(Class_Type_idClass)
    REFERENCES Class_Type(idClass),
  FOREIGN KEY(Staff_idStaff)
    REFERENCES Staff(idStaff));


CREATE INDEX Course_has_Class_FKIndex1 ON Class (Course_idCourse);
CREATE INDEX Course_has_Class_FKIndex2 ON Class (Class_Type_idClass);
CREATE INDEX Course_has_Class_FKIndex3 ON Class (Staff_idStaff);


CREATE INDEX IFK_Rel_01 ON Class (Course_idCourse);
CREATE INDEX IFK_Rel_02 ON Class (Class_Type_idClass);
CREATE INDEX IFK_Rel_14 ON Class (Staff_idStaff);


CREATE TABLE Student_has_Class (
  Student_idStudent INTEGER   NOT NULL ,
  Class_Course_idCourse INTEGER   NOT NULL ,
  Class_Class_Type_idClass INTEGER   NOT NULL   ,
PRIMARY KEY(Student_idStudent, Class_Course_idCourse, Class_Class_Type_idClass)    ,
  FOREIGN KEY(Student_idStudent)
    REFERENCES Student(idStudent),
  FOREIGN KEY(Class_Course_idCourse, Class_Class_Type_idClass)
    REFERENCES Class(Course_idCourse, Class_Type_idClass));


CREATE INDEX Student_has_Course_has_Class_FKIndex1 ON Student_has_Class (Student_idStudent);
CREATE INDEX Student_has_Course_has_Class_FKIndex2 ON Student_has_Class (Class_Course_idCourse, Class_Class_Type_idClass);


CREATE INDEX IFK_Rel_10 ON Student_has_Class (Student_idStudent);
CREATE INDEX IFK_Rel_11 ON Student_has_Class (Class_Course_idCourse, Class_Class_Type_idClass);




INSERT INTO User_2(Name , Surname, Mail, Login, Password_2, Permissions) 
        VALUES ('Admin', 'Admin', 'admin@agh.edu.pl', 'admin', 'admin', 99);
INSERT INTO User_2(Name , Surname, Mail, Login, Password_2, Permissions) 
        VALUES ('Juliusz', 'Trabka', 'trabka@agh.edu.pl', 'student1', 'password', 1);
INSERT INTO User_2(Name , Surname, Mail, Login, Password_2, Permissions) 
        VALUES ('Maciej', 'Lit', 'lit@agh.edu.pl', 'student2', 'password', 1);
INSERT INTO User_2(Name , Surname, Mail, Login, Password_2, Permissions) 
        VALUES ('Mateusz', 'Molibdenowy', 'molibdenowy@agh.edu.pl', 'staff1', 'password', 2);
INSERT INTO User_2(Name , Surname, Mail, Login, Password_2, Permissions) 
        VALUES ('Janusz', 'Tytanowy', 'tytanowy@agh.edu.pl', 'staff2', 'password', 2);
INSERT INTO User_2(Name , Surname, Mail, Login, Password_2, Permissions) 
        VALUES ('Tadeusz', 'Wolframowy', 'wolframowy@agh.edu.pl', 'staff3', 'password', 2);


INSERT INTO Class_Type(Name, MinStudents, MaxStudents) VALUES ('Lecture', 7, 150);
INSERT INTO Class_Type(Name, MinStudents, MaxStudents) VALUES ('Laboratory class', 7, 15);
INSERT INTO Class_Type(Name, MinStudents, MaxStudents) VALUES ('Class', 10, 30);
INSERT INTO Class_Type(Name, MinStudents, MaxStudents) VALUES ('Seminar', 7, 20);
INSERT INTO Class_Type(Name, MinStudents, MaxStudents) VALUES ('Project class', 7, 15);


INSERT INTO Student(User_2_idUser_2, FieldOfStudy, Year_2, Semester, ID) VALUES (2, 'Applied Computer Science', 2, 3, 1222);
INSERT INTO Student(User_2_idUser_2, FieldOfStudy, Year_2, Semester, ID) VALUES (3, 'Theoretical Physics', 4, 7, 2222);


INSERT INTO Staff(User_2_idUser_2, Department, Title) VALUES (4, 'Department of Computer Science', 'Ph.D');
INSERT INTO Staff(User_2_idUser_2, Department, Title) VALUES (5, 'Department of Theoretical Physics', 'D.Sc');
INSERT INTO Staff(User_2_idUser_2, Department, Title) VALUES (6, 'Department of Computer Science', 'B.Sc');


INSERT INTO Course(Staff_idStaff, Name, ID, ECTS, Desription, Hours, MinStudents, MaxStudents, Semester) 
        VALUES (1, 'Quantum Physics', 101, 8, 'Fajny opis kursu. wow wow', 120, 15, 60, 0);
INSERT INTO Course(Staff_idStaff, Name, ID, ECTS, Desription, Hours, MinStudents, MaxStudents, Semester) 
        VALUES (2, 'Introduction to databases', 102, 4, 'Fajny opis kursu2222. wow wow', 60, 15, 30, 1);


INSERT INTO Student_has_Course(Student_idStudent, Course_idCourse) VALUES (1, 1);
INSERT INTO Student_has_Course(Student_idStudent, Course_idCourse) VALUES (1, 2);
INSERT INTO Student_has_Course(Student_idStudent, Course_idCourse) VALUES (2, 1);


INSERT INTO Class(Course_idCourse, Class_Type_idClass, Staff_idStaff, Hours, Instructor) VALUES (1, 1, 2, 60, 'D.Sc. Prof2');
INSERT INTO Class(Course_idCourse, Class_Type_idClass, Staff_idStaff, Hours, Instructor) VALUES (1, 3, 2, 30, 'D.Sc. Prof2');
INSERT INTO Class(Course_idCourse, Class_Type_idClass, Staff_idStaff, Hours, Instructor) VALUES (1, 2, 1, 30, 'Ph.D. Prof1');
INSERT INTO Class(Course_idCourse, Class_Type_idClass, Staff_idStaff, Hours, Instructor) VALUES (2, 1, 1, 30, 'Ph.D. Prof1');
INSERT INTO Class(Course_idCourse, Class_Type_idClass, Staff_idStaff, Hours, Instructor) VALUES (2, 2, 1, 30, 'Ph.D. Prof1');


INSERT INTO Student_has_Class(Student_idStudent, Class_Course_idCourse, Class_Class_Type_idClass) VALUES (1, 1, 1);
INSERT INTO Student_has_Class(Student_idStudent, Class_Course_idCourse, Class_Class_Type_idClass) VALUES (1, 1, 2);
INSERT INTO Student_has_Class(Student_idStudent, Class_Course_idCourse, Class_Class_Type_idClass) VALUES (1, 1, 3);
INSERT INTO Student_has_Class(Student_idStudent, Class_Course_idCourse, Class_Class_Type_idClass) VALUES (2, 1, 1);
INSERT INTO Student_has_Class(Student_idStudent, Class_Course_idCourse, Class_Class_Type_idClass) VALUES (2, 1, 2);
INSERT INTO Student_has_Class(Student_idStudent, Class_Course_idCourse, Class_Class_Type_idClass) VALUES (2, 1, 3);
INSERT INTO Student_has_Class(Student_idStudent, Class_Course_idCourse, Class_Class_Type_idClass) VALUES (1, 2, 1);
INSERT INTO Student_has_Class(Student_idStudent, Class_Course_idCourse, Class_Class_Type_idClass) VALUES (1, 2, 2);



