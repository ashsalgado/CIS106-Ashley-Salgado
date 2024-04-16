def displayarrays(lname, score):
  for i in range(0, 10, 1):
    print(lname[i], "has a score of", score[i])

def rdisplay(lname):
  for i in range(9, -1, -1):
    print(lname[i])

lname = ["Adams", "Baker", "Smith", "Davis", "Jones", "Klein, ", "Lopez", "Rodriguez", "Wilson", "Patel")
score = ["95", "90", "85", "80", "75", "70", "65", "60", "55", "50"]


displayarrays(lname, score)
print("reverse order")
rdisplay(lname)