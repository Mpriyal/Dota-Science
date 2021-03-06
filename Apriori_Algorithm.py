import pandas as pd
from apyori import apriori

store_data = pd.read_csv("data/winners.csv")
store_data.head()

records = []
for i in range(0, 1000):
    records.append([str(store_data.values[i,j]) for j in range(0, 5)])

association_rules = apriori(records, min_support=0.001, min_confidence=0.5, min_lift=3, max_length=2, min_length = 2)
association_results = list(association_rules)

print(len(association_results))
for i in range (0, len (association_results)):
    print(association_results[i])