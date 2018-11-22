import csv 

categories = []
canada = []
world = []

with open('data/MedalData.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
        	categories.append(row)
        	line_count += 1
        elif row[4] == "CAN":
        	canada.append([int(row[0]), row[5], row[6], row[7]]) # multi dimensional array 
        else:
        	world.append([int(row[0]), row[5], row[6], row[7]])
        line_count += 1

print('total medals for canada:', len(canada))
print('total medals for everyone else:', len(world))

print('processed', line_count, 'rows of data')
print(canada[0])

gold_1924 = []
gold_1948 = []
gold_1972 = []
gold_2002 = []
gold_2014 = []

for medal in canada:
	if medal[0] == 1924 and medal[3] == "Gold":
		gold_1924.append(medal)

	if medal[0] == 1924 and medal[3] == "Gold":
		gold_1948.append(medal)

	if medal[0] == 1924 and medal[3] == "Gold":
		gold_1972.append(medal)

	if medal[0] == 1924 and medal[3] == "Gold":
		gold_2002.append(medal)

	if medal[0] == 1924 and medal[3] == "Gold":
		gold_2014.append(medal)


# filter 2014 based on gender
# plot men vs women (percentages of total)
men = []
women=[]
menMedals =int(len(men)) / len(gold_2014) *100
womenMedals = int(len(women))

for gender in gold_2014:
	if gender[1] == "Men":
		men.append(gender)
	elif gender[1] == 'Women':
		women.append(gender)

# chart visualization
labels = "Men", "Women"
sizes = [menMedals, womanMedals]
colors = ['Blue', 'Pink']
explode = (0.1, 0.1, 0.1)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Canadian men vs women ")
plt.xlabel("Who won more medals")
plt.show()

