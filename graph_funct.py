import plotly.express as px 
from database_class import DatabaseManager
import pandas as pd



def plot_graph():
    database = DatabaseManager()
    data_ds18 = DatabaseManager.read_all_values(database,"ds18")
    #print(data_ds18)
    df = pd.DataFrame(data_ds18, columns = ['id', 'aquarium_name', 'snesor_type', 'data_temp', 'date'])    
    #print(df)

    fig = px.line(df[-48:], x="date" , y="data_temp", markers=True) 
    fig.update_layout(title=dict(text="Dsb Aquarium Temperature"),xaxis=dict(title=dict(text="Date")),yaxis=dict(title=dict(text="Temperature")),font=dict(family="Courier New, monospace",size=9,color="RebeccaPurple"))
    fig.update_yaxes(showgrid=True)
    fig.update_yaxes(range=[20, 33])
    fig.update_layout(margin=dict(l=20, r=20, t=20, b=20),paper_bgcolor="LightSteelBlue",)

    return fig
