def loadarrays():
  lname3 = []
  avg = []
  with open("mylife.txt", "r") as f:
    for line in f.readlines(10):
      ln = f.readline().rstrip("\n")
      batting_avg = float(f.readline().rstrip("\n"))
      lname3.append(ln)
      avg.append(batting_avg)
    return lname3, avg

def searchname(lname3, avg, slname):
  foundsub = -1
  for i in range(len(lname3)):
    if lname3[i] == slname:
      foundsub = i


if foundsub == -1:
  print(slname, "not found")
else:
  print(lname3[foundsub], "has batting average of", avg[foundsub])

lname3, avg = loadarrays()

response = input("Do you want to search for a name? (Y or N)")
while response.lower() == "yes":
  slname = input("Enter a name to search for: ")
  searchname(lname3, avg, slname)
  response = input("Do you want to search for a name? (Y or N)")