class1=int(input('Enter score between (0-100'))
class2=int(input('Enter score between (0-100'))
class3=int(input('Enter score between (0-100'))

average=(class1+class2+class3)/3 
if average > 80:
    print("Grade: A")
elif average > 70:
    print("Grade: B")
elif average < 69:
    print("Grade: F")