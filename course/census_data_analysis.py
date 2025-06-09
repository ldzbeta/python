import pandas
data=pandas.read_csv("Squirrel_Data.csv")
counts = data["Primary Fur Color"].value_counts()
# print(counts)
output ={
    "Fur Color":["grey","red","black"],
    "Count": counts.values.tolist()
}

df = pandas.DataFrame(output)
df.to_csv("output_data.csv")