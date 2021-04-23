class Student:

  def __init__(self,name,year):
    self.name = name
    self.year = year
    self.grades = []

  def add_grade(self,grade):
    if(type(grade) == Grade):
      self.grades.append(grade)

  def get_average(self):
    sum_of_grades = 0
    for grade in self.grades:
      sum_of_grades += grades
    return sum_of_grades/len(self.grades)

    

class Grade:
  minimum_passing = 65

  def __init__(self,score):
    self.score = score

  def is_passing(self):
    if(self.sore >= 65):
      return "Passing"
    else:
      return "Not Passing"

roger = Student('Roger van der Weyden',10)
sandro = Student('Sandro Botticelli',12)
pieter = Student('Pieter Bruegel the Elder',8)

perfect = Grade(100)
pieter.add_grade(perfect)