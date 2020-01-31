from app import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_num = db.Column(db.Integer, nullable=False)
    email = db.Column(db.Text)
    password = db.Column(db.Text)
    grades = db.relationship('Grade', backref='students')

    def __repr__(self):
        return '<Student {}>'.format(self.student_id)


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacher_num = db.Column(db.Text, nullable=False)
    title = db.Column(db.Text)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    courses = db.relationship('Course', backref='teachers')

    def __repr__(self):
        return '<Teacher {} {}>'.format(self.first_name, self.last_name)


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.Integer, nullable=False)
    name = db.Column(db.Text, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)
    grades = db.relationship('Grade', backref='courses')

    def __repr__(self):
        return '<Course {}>'.format(self.code, self.name)


class Grade(db.Model):
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False, primary_key=True)
    grade = db.Column(db.Text)

    def __repr__(self):
        return '<Grade {}>'.format(self.grade)
