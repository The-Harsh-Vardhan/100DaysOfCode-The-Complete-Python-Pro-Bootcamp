import pandas as pd

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250625.csv")
# print(df.head())

fur_color = df["Primary Fur Color"]
# print(fur_color.head())

grey_squirrel_count = len(df[df["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(df[df["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(df[df["Primary Fur Color"] == "Black"])

print(f"Grey = {grey_squirrel_count}")
print(f"Red = {red_squirrel_count}")
print(f"Black = {black_squirrel_count}")

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

my_data = pd.DataFrame(data_dict)
my_data.to_csv("squirrel_count.csv")