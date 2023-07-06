from datetime import datetime, date, timedelta
from random import randint, choice
from sqlalchemy import select
from faker import Faker
from src.models import Lecturer, Group, Student, Discipline, Grade 
from src.db import session


def initial_data():

	disciplines = [
		"Astronomy",
		"Biology",
		"Chemistry",
		"Computer science",
		"Law",
		"Physics",
		"Science",
		"Maths"
	]

	groups = [
		'8.06.051.100.D.22.1',
		'6.03.075.010.19.2',
		'6.06.241.010.20.3'
	]

	NUMBER_LECTURERS = 5
	NUMBER_STUDENTS = 50
	fake = Faker()


	def seed_lecturers():

		for l in range(NUMBER_LECTURERS):
			lecturer = Lecturer(fullname=fake.name())
			session.add(lecturer)
		session.commit()

		
	def seed_disciplines():

		all_lecturers = session.scalars(select(Lecturer.id)).all()
		for discipline in disciplines:
			session.add(Discipline(name=discipline, lecturer_id=choice(all_lecturers)))
		session.commit()
		

	def seed_groups():

		for group in groups:
			session.add(Group(name=group))
		session.commit()
		

	def seed_students():

		all_group = session.scalars(select(Group.id)).all()
		for s in range(NUMBER_STUDENTS):
			student = Student(fullname=fake.name(), group_id=choice(all_group))
			session.add(student)
		session.commit()    


	def seed_grades_book():
		
		start_date = datetime.strptime("2022-09-01", "%Y-%m-%d")
		end_date = datetime.strptime("2023-06-15", "%Y-%m-%d")
		list_dates = get_list_date(start=start_date, end=end_date)
		all_discipline = session.scalars(select(Discipline.id)).all()
		all_student = session.scalars(select(Student.id)).all()
		for day in list_dates:
			random_discipline = choice(all_discipline)
			random_students = [choice(all_student) for _ in range(6)]
			for student in random_students:
				grade = Grade(
						grade=randint(1, 200),
						date_of=day,
						student_id=student,
						discipline_id=random_discipline,
					)
				session.add(grade)
		session.commit()


	def get_list_date(start: date, end: date):

		result = []
		current_date = start
		while current_date <= end:
			if current_date.isoweekday() < 6:
				result.append(current_date)
			current_date += timedelta(1)
		return result


	seed_lecturers()
	seed_disciplines()
	seed_groups()
	seed_students()
	seed_grades_book()

if __name__ == "__main__":
	initial_data()
