from peewee import *

db = SqliteDatabase('students.db')


class Student(Model):
    # A model represents a single item in the database (singular class name)
    username = CharField(max_length=255, unique=True)
    points = IntegerField(default=0)

    # Setting the database to the varaible db.
    class Meta:
        database = db

students = [
        {
            'username': 'mikevaldez92',
            'points': 5000
        },
        {
            'username': 'awesomesauce12',
            'points': 3004
        },
        {
            'username': 'joytotheworld',
            'points': 1500
        },
        {
            'username': 'craigiscool',
            'points': 2012
        },
        {
            'username': 'dave63993',
            'points': 4328
        }
]


def add_students():
    for student in students:
        try:
            Student.create(username=student['username'], points=student['points'])
        except IntegrityError:
            student_record = Student.get(username=student['username'])
            student_record.points = student['points']
            student_record.save()


def top_student():
    # Get all the students, order them descending by points, and then get the first
    student = Student.select().order_by(Student.points.desc()).get()
    return student

if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe=True)
    add_students()
    # Get back the 0th record
    print('Our top student right now is {0.username}'.format(top_student()))
