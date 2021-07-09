import statistics
import pandas as pd
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].to_list()

population_mean = statistics.mean(data)

print('the mean is ', population_mean)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index= random.randint(0,len(data)-1) 
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(mean_list)
    print(" Mean of the sampling distribution- ",mean)
    fig=ff.create_distplot([df],["temp"], show_hist = False)
    fig.add_trace(go.Scatter(x=[mean,mean], y = [0,1], mode = "lines", name = "MEAN"))
    fig.show()

def setup():
    mean_list =[]
    for i in range(0,100):
        set_of_mean = random_set_of_mean(30)
        mean_list.append(set_of_mean)
    show_fig(mean_list)

setup()