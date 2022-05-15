import pandas as pd
import plotly.express as px
import csv

df = pd.read_csv("pixle_math.csv")
avg = df.groupby('level')['attempt'].mean()


fig = px.scatter(avg, x = 'student_id', y = ["LEVEL 1", "LEVEL 2", 'LEVEL 3', 'LEVEL 4'], size = "attempt", color = "attempt", as_index = False)
fig.show()