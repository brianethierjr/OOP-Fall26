Course1 = int(input("Enter Grade for Course 1: "))
Course2 = int(input("Enter Grade for Course 2: "))
Course3 = int(input("Enter Grade for Course 3: "))
Total = int(Course1 + Course2 + Course3)
Percentile = (Total/300)*100

if Percentile < 100 and Percentile >= 90:
    print("Grade A")
elif Percentile < 90 and Percentile >= 80:
    print("Grade B")
elif Percentile < 80 and Percentile >= 70:
    print("Grade C")
elif Percentile < 70 and Percentile >= 60:
    print ("Grade D")
elif Percentile < 60 and Percentile >= 0:
    print("Grade F")
elif Percentile > 100 or Percentile < 0:
    print ("N/A")