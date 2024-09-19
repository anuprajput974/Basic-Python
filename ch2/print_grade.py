''' TAKE INPUT PERCENTAGE OF A STUDENT AND PRINT THE GRADE ACCORDING TO MARKS:
81-100  very good
61-80   good
41-60   average
<=40    fail'''

marks = float(input("enter the marks"))
percentage = (marks/100)*100
if marks >= 80:
   
    print("very good your percentage is ",percentage)
elif marks >60 and marks < 80:
    print("good your percentage is ",percentage)
elif marks > 40 and marks <= 60 :
    print("your marks are average",percentage)
else:
    print("fail")