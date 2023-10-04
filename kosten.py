import pandas as pd

##########
##Inputs##
##########
categories = []
amounts = []
is_inputing = True

data = {
    "category": categories,
    "amount": amounts
}

while is_inputing:
    user_input = input("Add an item? (Y)es:")
    if user_input == "Y" or user_input == "y":
        data["amount"].append(float(input("Quanta costa?")))
        data["category"].append(input("Welke category:"))
    else:
        is_inputing = False

#############
##To Excell##
#############
#pip install openpyxl <- nodig om naar excell om te zetten


data_frame = pd.DataFrame(data)
data_frame.to_excel('data/costs.xlsx', sheet_name="overview", index=False)
data_frame.to_csv('data/costs.csv', index=False)
#########
##Stats##
#########
print(data_frame["amount"].max())
print(data_frame["amount"].mean())
print(data_frame.groupby("category").mean())
print(data_frame.groupby("category").sum())