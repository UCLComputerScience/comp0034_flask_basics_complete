from app import create_app, db
from app.models import Student, Teacher, Course, Grade


def populate_db():
    """Populates the cscourses.db database if it is empty. The Flask app needs to be running before you execute this code.

    :return: None
    """

    if not Student.query.first():
        s1 = Student(student_id="CS1234567", email='cs1234567@ucl.co.uk', password='test1pass')
        s2 = Student(student_id="CS1234568", email="cs1234568@ucl.co.uk", password="test2pass")
        s3 = Student(student_id="CS1234569", email="cs1234569@ucl.co.uk", password="test3pass")
        s4 = Student(student_id="CS1234570", email="cs1234569@ucl.co.uk", password="test3pass")

        t1 = Teacher(teacher_id="uclcs0002", title="Dr", first_name="Lewis", last_name="Baird")
        t2 = Teacher(teacher_id="uclcs0006", title="Prof", first_name="Elif", last_name="Munro")
        t3 = Teacher(teacher_id="uclcs0010", title="Ms", first_name="Aleyna", last_name=" Bonilla")

        c1 = Course(course_code="COMP0015", name="Introduction to Programming")
        c2 = Course(course_code="COMP0034", name="Software Engineering")
        c3 = Course(course_code="COMP0035", name="Web Development")

        g1 = Grade(grade="B-")
        g2 = Grade(grade="C")
        g3 = Grade(grade="B+")
        g4 = Grade(grade="A+")
        g5 = Grade(grade="A+")
        g6 = Grade(grade="D+")
        g7 = Grade(grade="B")
        g8 = Grade(grade="D-")

        s1.grades.append(g1)
        s1.grades.append(g5)
        s2.grades.append(g2)
        s2.grades.append(g6)
        s3.grades.append(g3)
        s3.grades.append(g7)
        s4.grades.append(g4)
        s4.grades.append(g8)

        c1.grades.append(g1)
        c1.grades.append(g2)
        c1.grades.append(g3)
        c2.grades.append(g4)

        t1.courses.append(c1)
        t2.courses.append(c2)
        t3.courses.append(c3)

        db.session.add_all([s1, s2, s3, s4])
        db.session.add_all([t1, t2, t3])
        db.session.commit()


app = create_app()
app.app_context().push()
populate_db()
