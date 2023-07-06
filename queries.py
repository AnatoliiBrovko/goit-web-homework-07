from sqlalchemy import func, desc, select

from src.models import Lecturer, Group, Student, Discipline, Grade
from src.db import session


def query_1():

    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label("averagegrade"))\
        .select_from(Grade)\
        .join(Student)\
        .group_by(Student.id)\
        .order_by(desc('averagegrade')).limit(5).all()
    print(result)


def query_2(subj_id):

    result = session.query(Discipline.name, Student.fullname, func.round(func.avg(Grade.grade), 2).label("averagegrade"))\
        .select_from(Grade)\
        .join(Student).join(Discipline)\
        .filter(Discipline.id == subj_id)\
        .group_by(Student.id, Discipline.name)\
        .order_by(desc('averagegrade')).limit(1).all()
    print(result)


def query_3(subj_id):

    result = session.query(Discipline.name, Group.name, func.round(func.avg(Grade.grade), 2).label("averagegrade"))\
        .select_from(Grade)\
        .join(Student).join(Group).join(Discipline)\
        .filter(Discipline.id == subj_id)\
        .group_by(Group.name, Discipline.name)\
        .order_by(desc('averagegrade')).all()
    print(result)


def query_4():

    result = session.query(func.round(func.avg(Grade.grade), 2).label("averagegrade")).all()
    print(result)


def query_5():

    result = session.query(Lecturer.fullname, Discipline.name)\
        .select_from(Lecturer)\
        .join(Discipline)\
        .group_by(Discipline.name, Lecturer.fullname).all()
    print(result)


def query_6():

    result = session.query(Group.name, Student.fullname)\
        .select_from(Group)\
        .join(Student)\
        .group_by(Group.name, Student.fullname).all()
    print(result)


def query_7(id_group, id_name):

    result = session.query(Group.name,Discipline.name, Student.fullname, Grade.grade)\
        .select_from(Grade)\
        .join(Student).join(Discipline).join(Group)\
        .filter(Discipline.id == id_name, Group.id == id_group)\
        .group_by(Group.name, Discipline.name, Student.fullname, Grade.grade).all()
    print(result)


def query_8(id_lecturer):

    result = session.query(Discipline.name, Lecturer.fullname, func.round(func.avg(Grade.grade), 2).label("averagegrade"))\
        .select_from(Grade)\
        .join(Discipline).join(Lecturer)\
        .filter(Lecturer.id == id_lecturer)\
        .group_by(Lecturer.fullname, Discipline.name).all()
    print(result)


def query_9(id_student):

    result = session.query(Student.fullname, Discipline.name)\
        .select_from(Grade).join(Student)\
        .join(Discipline)\
        .filter(Student.id == id_student)\
        .group_by(Student.fullname, Discipline.name).all()
    print(result)


def query_10(id_student, id_lecturer):

    result = session.query(Student.fullname, Lecturer.fullname, Discipline.name)\
        .select_from(Grade)\
        .join(Student).join(Discipline).join(Lecturer)\
        .filter(Student.id == id_student, Lecturer.id == id_lecturer)\
        .group_by(Student.fullname, Lecturer.fullname, Discipline.name).all()
    print(result)


if __name__=="__main__":
    print("1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.")
    query_1()
    print("\n2. Знайти студента із найвищим середнім балом з певного предмета.")
    query_2(5)
    print("\n3. Знайти середній бал у групах з певного предмета.")
    query_3(5)
    print("\n4. Знайти середній бал на потоці (по всій таблиці оцінок).")
    query_4()
    print("\n5. Знайти, які курси читає певний викладач.")
    query_5()
    print("\n6. Знайти список студентів у певній групі.")
    query_6()
    print("\n7. Знайти оцінки студентів в окремій групі з певного предмета.")
    query_7(1,4)
    print("\n8. Знайти середній бал, який ставить певний викладач зі своїх предметів.")
    query_8(2)
    print("\n9. Знайти список курсів, які відвідує певний студент.")
    query_9(5)
    print("\n10. Список курсів, які певному студенту читає певний викладач.")
    query_10(26,1)







