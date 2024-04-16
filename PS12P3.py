def loadarrays(lname, score):
  f = open("mtfile.txt", "r")
  for i in range(10):
    ln = f.readline().rstrip("\n")
    score_value = int(f.readline().rstrip("\n"))
    lname3.append(ln)
    score.append(score_value)

def darrays(lname, score): 
  for i in range(10):
    print(lname[i], "has score of", score[i])

def hillow(lname, score):
  hisco = 0 
  hisub = 0
  losco = 999
  losub = 0

  for i in range(10):
    if score[i] > hisco:
      hisco = score[i]
      hisub = i
    elif score[i] < losco:
      losco = score[i]
      losub = i

  print(lname[hisub], "has the highest score of ", score[hisub])
  print(lname[losub], "has the lowest score of ", score[losub])

lname3 = []
score = []
loadarrays(lname3, score)
darrays(lname3, score)
hillow(lname3, score)