#program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale:

score = float(input("Enter the score\n"))

if score >=90 and score<=100:
    grade = "A"
elif score >=80 and score <=89:
    grade ="B"
elif score >=70 and score <=79:
    grade ="C"
elif score >=60 and score <=69:
    grade ="D"
else:
    grade ="F"
print (grade)
