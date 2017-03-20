#Homework One
#Yuhui Zhong
#Source from:
#EPA United States Environment Protection Agency
#Data Name:
#2017 Data on Cars used for Testing Fuel Economy
#URL:
#https://www.epa.gov/sites/production/files/2016-09/17tstcar.csv


#Importing data analyzing packages ‘pandas’ and ‘numpy’
import pandas as pd
import numpy as np

#downloading file to local folder and save the file path to a vector, please replace the path with your own file location
datapath = 'C:/Users/yzhon_000/Downloads/17tstcar.csv'

#read file by using pd.read_csv
tst_car = pd.read_csv(datapath, sep=',', nrows=4249)

#Selecting few columns in the data frame that are useful for fuel efficiency analyze  
tst_car1 = tst_car[['Vehicle Manufacturer Name','Represented Test Veh Model', 'Test Veh Displacement (L)','Vehicle Type','# of Cylinders and Rotors','Tested Transmission Type', '# of Gears','Drive System Description','Test Fuel Type Cd','Test Category','RND_ADJ_FE']]

#Unify test conditions under same fuel type, test method, car type, and transmission type 
#selecting cases that only using fuel which type is 61
tst_car1 = tst_car1[tst_car1['Test Fuel Type Cd'] == 61]
#selecting cases that vehicles are tested under ‘Federal fuel 2-day exhaust (w/can load)’ condition
tst_car1 = tst_car1[tst_car1['Test Category'] == 'FTP']
#targets’ vehicle type is car, not truck or both
tst_car1 = tst_car1[tst_car1['Vehicle Type'] == 'Car']
#transmission type is fixed as semi-automatic
tst_car1 = tst_car1[tst_car1['Tested Transmission Type'] == 'Semi-Automatic']

#Start import packages for drawing graphs  
import plotly.plotly as py
import plotly.graph_objs as go
import plotly

#using plotly API for sign in and saving file online
plotly.tools.set_credentials_file(username='1992E-zy819', api_key='O8bv21Dc8lZxkRT4k8eh')

#create a new data frame for analyzing relationship between vehicle displacement and fuel efficiency
tst_car_dspl = tst_car1[['Test Veh Displacement (L)','RND_ADJ_FE']]

#generate data structure and display each case as dots 
trace = go.Scatter(
    x = tst_car_dspl['Test Veh Displacement (L)'],
    y = tst_car_dspl['RND_ADJ_FE'],
    mode = 'markers'
)
data = [trace]

#layout arrangement
layout = dict(title = 'Fuel Efficiency VS. Vehicle Displacement',
              yaxis = dict(title = 'MPG'),
              xaxis = dict(title = 'Vehicle Displacement')
             )

#combine content and layout
fig = dict(data=data, layout=layout)

#display first graph and save it
py.iplot(fig, filename='FE_VD_Dots Chart')

#creating a new data frame to analyze relationship between drive system and fuel consumption
tst_car_sys = tst_car1[['Drive System Description','RND_ADJ_FE']]

#calculate mean of fuel consumption group by each drive system
car_sys_group = tst_car_sys.groupby(tst_car_sys['Drive System Description']).mean()

#transfer two columns in the data frame into two lists
car_sys_type = list(car_sys_group.index)
car_sys_fe = list(car_sys_group['RND_ADJ_FE'])

#generate data structure and content
trace2 = go.Bar(
    x = car_sys_type,
    y = car_sys_fe,
    marker = dict(
            color = 'grey'
    )
)
data2 = [trace2]

#arranging the graph’s layout
layout2 = go.Layout(title = 'Fuel Efficiency among Different Drive Systems',
              yaxis = dict(title = 'MPG'),
              bargap = 1.5              
             )

#combining layout and content
fig = go.Figure(data=data2, layout=layout2)

#output graph
py.iplot(fig, filename='bar-chart')
