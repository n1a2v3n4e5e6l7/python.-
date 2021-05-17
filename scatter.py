import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import csv
 
df = pd.read_csv("data.csv")
#print(df.groupby("level")["attempt"].mean())
mean = df.groupby(['student_id','level'],as_index = False)["attempt"].mean()
print(mean)
fig = px.scatter(mean,x = "student_id",y = "level",size = "attempt",color = "attempt")
#fig = go.Figure(data = [go.Scatter(x ='student_id',y = 'level',color = "attempt")])
fig.show()
