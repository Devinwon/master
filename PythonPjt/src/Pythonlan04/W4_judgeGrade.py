score=float(input("Enter marks:"))
if 70>score>=60:
    grade='D'
elif 80>score>=70:
    grade='C'
elif 90>score>=80:
    grade='B'
elif score>=90:
    grade='A'
print("Grade:"+grade)