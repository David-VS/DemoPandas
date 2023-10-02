import pandas as pd
import openpyxl as op

titanicDS = pd.read_csv("data/titanic.csv")
print(titanicDS)
print(titanicDS["Name"])  # Serie = 1 kolom
print(titanicDS[titanicDS["Age"] < 20])  #filter rijen
print(titanicDS.loc[titanicDS["Age"] < 20, ["Name", "Sex", "Age"]]) #combinatie rijen & kolom

print(titanicDS.groupby("Pclass").count()) #groepen op dezelfde waarde
print(titanicDS["Fare"].max()) #functies op reeks getallen



metingen = {
    "temperatuur": [14, 15, 22, 18],
    "neerslag": [0, 0, 200, 150],
    "tweer": ["zonnig", "zonnig", "lichte neerslag", "zondvloed"]
}

metingenDF = pd.DataFrame(metingen)
print(metingenDF)
print(metingenDF["temperatuur"].mean())
print(metingenDF["neerslag"].max())
print(metingenDF[metingenDF["tweer"] == "zonnig"])
