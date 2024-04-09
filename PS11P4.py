def b_average (score1,score2,score3,handi):
  sum = score1 + score2 + score3
  average = (sum / 3)
  haverage = (sum + handi) / 3
  return average, haverage



lastname = str(input("Enter bowlers last name "))
score1 = float(input("Enter your score 1 "))
score2 = float(input("Enter your score 2 "))
score3 = float(input("Enter your score 3 "))
handi = float(input("Enter your handicap "))
average, haverage = b_average(score1,score2,score3,handi)
print("Your last name ", lastname)
print("Your average score is ", average)
print("Your handicap average is ", haverage)