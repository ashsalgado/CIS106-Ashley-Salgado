def dl1 (mylist):
  n = int(input("Number of items for your list"))
  for n in range(0,n,1):
    s = int(input("Enter an integer"))
    my_list.append(s)
  return my_list
def displaylist(mylist):
  for item in mylist:
    print(item)

mylist = []  
mylist = dl1(mylist)
print(mylist)

#DL2
mylist.insert(0,99)
print(mylist)
#DL3
mylist[0] = 100
print(mylist)
#DL4
mylist2 = ["500", "600", "700", "800", "900"]
print(mylist2)
mylist.extend(mylist2)
print(mylist)
#DL5
mylist2.remove("700")
print(mylist2)
#DL7
grades = ["A", "B", "C", "A", "A", "C"]
print(grades)
#DL8
print("A appears", grades.count("A"), "times")
#DL9
print("B appears at index", grades.index("B"))
#DL10
if "F" in grades:
  print("F is in grades")
else:
  print("F is not in grades")

#DL11
mylist2.clear()
print(mylist2)
#DL12
del mylist2
#print(mylist2)
#DL13
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
print(players)
#DL14
players.sort()
print(players)
#DL15
players2 = players.copy()
print(players2)
#DL16
players2.reverse()
print(players)
print(players2)