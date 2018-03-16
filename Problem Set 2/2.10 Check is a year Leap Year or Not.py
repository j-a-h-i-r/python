year = int(input())

if year%400 == 0 or (year%4 == 0 and year%100 != 0):
    print("Year is Leap Year")
else:
    print("Year is Not Leap Year")
