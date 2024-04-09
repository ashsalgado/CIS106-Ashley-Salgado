def exam_average (exam1, exam2, exam3):
  sum = exam1 + exam2 + exam3
  total = 300
  percentage = (sum/total) * 100
  average = (sum/3)
  points = exam1 + exam2 + exam3
  return average, points



lastname = str(input("Enter last name "))
exam1 = float(input("Enter yoru exam score 1 "))
exam2 = float(input("Enter yoru exam score 2 "))
exam3 = float(input("Enter yoru exam score 3 "))

average, points = exam_average(exam1, exam2, exam3)
print("Your last name ", lastname)
print("Your average exam score is ", average)
print("Your total points is ", points)