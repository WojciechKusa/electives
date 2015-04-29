CREATE FUNCTION delete_course() RETURNS TRIGGER AS '
    BEGIN 
    DELETE FROM student_has_course  WHERE student_has_course.course_idcourse=old.idcourse; 

    DELETE FROM student_has_class  WHERE student_has_class.class_course_idcourse=old.idcourse; 

    DELETE FROM class  WHERE class.course_idcourse=old.idcourse; 

    RETURN old; 
    END; 
' LANGUAGE 'plpgsql';


CREATE TRIGGER delete_course_trigger BEFORE DELETE ON course FOR EACH ROW EXECUTE PROCEDURE delete_course();


