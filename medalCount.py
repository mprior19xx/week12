import csv
import matplotlib.pyplot as plt

golds = []
silvers = []
bronzes = []

categories =[]

with open('./data/MedalData.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            categories.append(row)
            line_count += 1

        else:
            if row[7] =="Gold":
                golds.append(row[7])

            elif row[7] == "Silver":
                silvers.append(row[7])

            elif row[7] == "Bronze":
                bronzes.append(row[7])
            line_count += 1

print(len(golds), 'Gold medals were won since \'24')
print(len(silvers), 'Silver medals were won since \'24')
print(len(bronzes), 'Bronze medals were won since \'24')

print('processes', line_count, 'lines of data')

totalMedals = len(golds) + len(silvers) + len(bronzes)

gold_percentage = int(len(golds) / totalMedals * 100)
bronze_percentage = int(len(bronzes) / totalMedals * 100)
silver_percentage = int(len(silvers) / totalMedals * 100)

# chart visualization
labels = "Gold", "Silver", "Bronze"
sizes = [gold_percentage, silver_percentage, bronze_percentage]
colors = ['gold', 'silver', 'chocolate']
explode = (0.2, 0.1, 0.15 )

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("How many medals have been won overall?")
plt.xlabel("Medal Counts")
plt.show()