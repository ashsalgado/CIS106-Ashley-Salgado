#input phase 
exam1 = float(input("Enter exam 1 score: "))
exam2 = float(input("Enter exam 2 score: "))
#process phase
total1 = 0.60 * exam1
total2 = 0.40 * exam2
totalscore = total1 + total2
#output phase
print("Total score is", totalscore)