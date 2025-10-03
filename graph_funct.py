import plotly.express as px 
from database_class import DatabaseManager
import pandas as pd



def plot_graph():
    database = DatabaseManager()
    data_ds18 = DatabaseManager.read_all_values(database,"ds18")
    print(data_ds18)
    df = pd.DataFrame(data_ds18, columns = ['id', 'aquarium_name', 'snesor_type', 'data_temp', 'date'])    
    print(df)


    fig = px.line(df[-48:], x="date" , y="data_temp") 
    return fig
