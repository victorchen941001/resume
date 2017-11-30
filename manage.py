from flask_script import Manager
from resume import app, db, Professor, Course

manager = Manager(app)



@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    professor1 = Professor(name='Jiang,Hao', department='ECON')
    professor2 = Professor(name='Sharma,Pratyush Nidhi', department='MISY')
    professor3 = Professor(name='Alisha', department = 'NTDT')
    professor4 = Professor(name='Cox', department = 'Art')
    course1 = Course(number="MISY330",title='Database Design and Implementation', description='Design and implementation of enterprise databases in the business environment', professor=professor2)
    course2 = Course(number="ECON308",title='Banking and Monetary Policy', description='Nature and economic significance of money, credit and the banking system', professor=professor1)
    course3 = Course(number="NTDT200",title='Nutrition Concepts', description='Functions and sources of nutrients, dietary adequacy, energy balance and metabolism with emphasis on health promotion',professor=professor3)
    course4 = Course(number="ART180",title='Digital Photography ', description='Introduces the basics of photography as a way to communicate ideas emphasizing content, composition, and technique',professor=professor4)
    db.session.add(professor1)
    db.session.add(professor2)
    db.session.add(professor3)
    db.session.add(professor4)
    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    db.session.add(course4)
    db.session.commit()


if __name__ == '__main__':
        manager.run()
