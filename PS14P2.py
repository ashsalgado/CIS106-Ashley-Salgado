class student:
  def __init__(self,first,last,code, credits):
    self.first = first
    self.last = last
    self.code = code
    self.credits = credits
    self.email = first + "." + last + "@company.com"


def computetuition(self):
  if self.code == "I":
    tuition = self.credits * 250
  else:
    tuition = self.credits * 500

  return tuition


student1 = student("James","Jones","I",12)
student2 = student("Mary","Smith","O",9)
tution = student1.computetuition()

print(student1.first,student1.last,student1.code,student1.credits, tuition)
print(student2.first,student2.last,student2.code,student2.credits, tuition