import pandas
squirrel = pandas.read_csv("census_data.csv")
colors = squirrel["Primary Fur Color"].value_counts(ascending = True)

colors.to_csv("color_count.csv")