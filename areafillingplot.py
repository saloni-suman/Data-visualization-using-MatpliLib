import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter
data=pd.read_csv("data.csv")
ids=data['Responder_id']
lang_response=data['LanguagesWorkedWith']
lang_counter=Counter
for response in lang_response:
    lang_counter.update(response.split(';'))
language=[]
popularity=[]                           
for item in lang_counter.most_common(3):
    lanuage.append(item[0])
    popularity.append(item[1])
print(language)
print(popularity)                            



