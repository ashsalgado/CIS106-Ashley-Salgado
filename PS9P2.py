def calculating(hits,bats):

  if bats == 0:
    return 0
  else:
    return hits/bats

count = 0

r = input("Do you want to calculate a player's batting average? (Y/N)?")

while r == "Y":
  lastname = input("Enter the player's last name: ")
  hits = int(input("Enter the number of hits: "))
  bats = int(input("Enter the number of times at bat: "))
  battingaverage = calculating(hits,bats)
  print(lastname, "has a batting average of: ", battingaverage)
  r = input("Do you want to calculate another player's batting average? (Y/N)?")
  count = count + 1

print("You have calculated", count, "players.")