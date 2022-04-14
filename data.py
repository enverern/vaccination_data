import pandas as  pd

df = pd.read_csv("country_vaccination_stats.csv")

df["daily_vaccinations"] = df["daily_vaccinations"].fillna(0)

countries = {}
for i in range(len(df["country"])):
    country = df["country"][i]
    if country in countries:
        countries[country].add(i)
    else:
        countries[country] = {i}
for i in countries.keys():
    """print(min(set(df.loc[list(countries[i]),"daily_vaccinations"].values)))"""
    if max(df.loc[list(countries[i]),"daily_vaccinations"].values)> 0:
        lower = min(set(df.loc[list(countries[i]),"daily_vaccinations"].values).difference({0}))
        for z in list(countries[i]):
            if df.loc[z,"daily_vaccinations"] == 0:
                df.loc[z,"daily_vaccinations"] = lower

df.to_csv("country_vaccination_stats.csv", encoding='utf-8', index=False)
