from flask_script import Manager
from resume import app, db, Professor, Course

manager = Manager(app)



@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    professor1 = Professor(name='Jiang,Hao', department='ECON')
    professor2 = Professor(name='Sharma,Pratyush Nidhi', department='MISY')
    course1 = Course(course_number="MISY330",title='Database Design and Implementation', description='Design and implementation of enterprise databases in the business environment', professor=professor2)
    course2 = Course(course_number="ECON308",title='Banking and Monetary Policy', description='Nature and economic significance of money, credit and the banking system', professor=professor1)
    course3 = Course(course_number="NTDT200",title='Nutrition Concepts', description='Functions and sources of nutrients, dietary adequacy, energy balance and metabolism with emphasis on health promotion.')
    course4 = Course(course_number="ART180",title='Digital Photography ', description='Introduces the basics of photography as a way to communicate ideas emphasizing content, composition, and technique.')
    db.session.add(professor2)
    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    db.session.add(course4)
    db.session.commit()


if __name__ == '__main__':
        manager.run()
