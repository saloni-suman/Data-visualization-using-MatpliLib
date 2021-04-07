from matplotlib import pyplot as plt
import csv
from collections import Counter
plt.style.use("fivethirtyeight")
with open("data.csv") as csv_file:
    csv.reader=csv.DictReader(csv_file)
    lang_counter=Counter()
    #row=next(csv.reader)
    #print(row['LanguagesWorkedWith'].split())
    for row in csv.reader:
        lang_counter.update(row['LanguagesWorkedWith'].split(';'))
#print(lang_counter.most_common(15))
language=[]
popularity=[]
for item in lang_counter.most_common(15):
    language.append(item[0])
    popularity.append(item[1])
language.reverse()
popularity.reverse()

plt.barh(language,popularity)
plt.title("language used by developers")
plt.xlabel("used by people")
plt.ylabel("language used")
plt.show()
