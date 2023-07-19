import csv
import random

with open("termal.csv", "w", newline='') as file:
    writer = csv.writer(file, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(346):
        writer.writerow([round(random.uniform(5.9, 6.3), 2), round(random.uniform(4.3, 4.7), 2),round(random.uniform(90.0, 95.0), 2),round(random.uniform(45.0, 50.0), 2),round(random.uniform(0.002, 0.03), 3),round(random.uniform(11.3, 12.5), 2)])