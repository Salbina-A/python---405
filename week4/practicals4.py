#1st task
import pandas as pd

Person = {"Name": ["Anahit", "Artur", "Hayk", "Jora", "Liana", "Nairi", "Ruzanna", "Salbina", "Sona", "Tatev", "Tigran", "Vlad"],
		"Surname" : ["Kirakosyan", "Mkrtchyan", "Sahakyan", "Karyan", "Varosyan", "Hakobyan", "Ordyan", "Alaverdyan", "Kirakosyan", "Alaverdyan", "Movsisyan", "Harutyunyan"],
		"Sex" : ["F", "M", "M", "M", "M", "F", "M" , "F", "F", "F", "F", "M"],
		"Status" : ["Student", "Student", "Student", "Student", "Student", "Tutor", "Student", "Student", "Student", "Student", "Student", "Student"]
				}
df = pd.DataFrame(Person, columns = ["Name", "Surname", "Sex", "Status"])
print(df)

#2nd task
import pandas as pd

df = pd.read_csv("netflix_titles.csv")
print(df[(df["release_year"]  > 2015) & (df["cast"].str.contains("Kevin Spacey") | df["cast"].str.contains("Leonardo DiCaprio"))])

#3rd task
import pandas as pd

df = pd.read_csv("netflix_titles.csv")

df_by_director = (df.groupby("director").size())
ser_to_df = df_by_director.to_frame() 
#print(ser_to_df)

final = df.merge(ser_to_df, on = "director")
print(final)



#5th task
import pandas as pd

df = pd.read_csv("netflix_titles.csv")

df1 = df.sort_values(by = ["duration", "date_added"])

print(df1[~df1["cast"].isnull() & (df1["cast"].str.contains("Antonio Banderas"))])

#6th task
import pandas as pd
import datetime 
import matplotlib.pyplot as plt


df = pd.read_csv("netflix_titles.csv")

df["date_added"] = pd.to_datetime(df["date_added"])

date_from = min(df["date_added"])
date_to = max(df["date_added"])
sorted_df = df[(df["date_added"] >= date_from) & (df["date_added"] <= date_to)]


date_month = (pd.to_datetime(sorted_df['date_added']).dt.to_period('M'))
series_to_df = date_month.to_frame() 


total_by_date = (series_to_df.groupby(["date_added"]).size())

total_by_date.plot.hist(color = "green")
plt.show()

total_by_date.plot()
plt.show()

#7th task
import pandas as pd
import datetime 

df = pd.read_csv("netflix_titles.csv")

df["date_added"] = pd.to_datetime(df["date_added"])

date_from = min(df["date_added"])
date_to = max(df["date_added"])



sorted_df = df[(df["date_added"] >= date_from) & (df["date_added"] <= date_to)]


for i in range(len(sorted_df) - 1):
	print(abs(df["date_added"][i] - df["date_added"][i+1])) 
