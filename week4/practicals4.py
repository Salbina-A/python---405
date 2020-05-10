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
print(ser_to_df)

final = df.merge(ser_to_df, on = "director")
print(final)



#5th task
import pandas as pd

df = pd.read_csv("netflix_titles.csv")

df1 = df.sort_values(by = ["duration", "date_added"])

print(df1[~df1["cast"].isnull() & (df1["cast"].str.contains("Antonio Banderas"))])
