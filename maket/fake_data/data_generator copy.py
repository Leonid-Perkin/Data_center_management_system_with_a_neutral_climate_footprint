import csv
import random

with open("test.csv", "w", newline='') as file:
    writer = csv.writer(file, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    a = 2023
    b = 0
    c = 0
    for i in range(10):
        writer.writerow([a,b,round(c, 2)])
        a+=1
        b+=1
        c-=1.1