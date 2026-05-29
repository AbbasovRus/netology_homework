from datetime import datetime

date1 = datetime.strptime("Wednesday, October 2, 2002", "%A, %B %d, %Y")
date2 = datetime.strptime("Friday, 11.10.13", "%A, %d.%m.%y")
date3 = datetime.strptime("Thursday, 18 August 1977", "%A, %d %B %Y")

print(date1)
print(date2)
print(date3)